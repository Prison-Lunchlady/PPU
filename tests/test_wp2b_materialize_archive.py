"""Offline regression tests for the fixed, versioned WP2B archive snapshot."""
import importlib.util
import pathlib
import shutil
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('wp2b_materialize', ROOT / 'tools/wp2b_materialize_archive.py')
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class WP2BArchiveMaterializationTests(unittest.TestCase):
    def setUp(self):
        self.workdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.workdir.cleanup)
        self.base = pathlib.Path(self.workdir.name)
        self.target = self.base / 'core-observations.csv'

    def test_exact_materialization_and_idempotence(self):
        result = mod.materialize(target=self.target)
        self.assertEqual(result['action'], 'materialized')
        self.assertEqual(result['row_count'], 92286)
        self.assertEqual(result['series_count'], 8)
        self.assertEqual(mod.git_blob_sha(self.target), mod.EXPECTED_GIT_BLOB)
        second = mod.materialize(target=self.target)
        self.assertEqual(second['action'], 'already_verified')

    def test_corrupted_archive_rejected_without_output(self):
        altered = self.base / 'corrupted.zip'
        data = bytearray(mod.ARCHIVE.read_bytes())
        data[-20] ^= 1
        altered.write_bytes(data)
        with self.assertRaisesRegex(ValueError, 'archive size/SHA256'):
            mod.materialize(archive=altered, target=self.target)
        self.assertFalse(self.target.exists())

    def test_mismatched_existing_panel_refuses_overwrite(self):
        self.target.write_text('fake history\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'refusing overwrite'):
            mod.materialize(target=self.target)
        self.assertEqual(self.target.read_text(), 'fake history\n')

    def test_committed_provenance_tamper_is_rejected(self):
        tmp_repo = self.base / 'repo'
        for name in mod.MEMBERS:
            if name == 'research/wp2b/data/core-observations.csv':
                continue
            f = tmp_repo / name
            f.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, f)
        bad = tmp_repo / 'research/wp2b/data/source-hashes.json'
        bad.write_bytes(bad.read_bytes() + b'\n')
        with mock.patch.object(mod, 'ROOT', tmp_repo):
            with self.assertRaisesRegex(ValueError, 'exact separately committed evidence missing or mismatched'):
                mod.materialize(target=self.target)
        self.assertFalse(self.target.exists())


if __name__ == '__main__':
    unittest.main()
