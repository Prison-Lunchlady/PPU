#!/usr/bin/env python3
"""Restore, but never silently modify, the exact verified WP2B observation panel.

Offline tool: does not fetch markets, revise any observations, call GitHub, or
advance a review gate. The archive is an immutable 2026-10-03 research snapshot.
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'research/wp2b/data/wp2b-verified-artifact-37128007402.zip'
OUTPUT = ROOT / 'research/wp2b/data/core-observations.csv'
ZIP_SIZE = 488039
ZIP_SHA256 = 'e4b6c54fdcfc40d3fc7d7e4e6234c87e649a504083acb7d794e013412f445386'
EXPECTED_GIT_BLOB = '527f09cff7ccea44ec029c0799a86b5c16ab4648'
MEMBERS = {
    'research/wp2b/data/core-observations.csv': (15783569, 'dd728aa4ca1592dda6aa48389046b3fd47bad4181aede69cb8160f81f2d60ba0'),
    'research/wp2b/data/source-hashes.json': (55638, '662ebe89a46b3b425bbcc05146b4fcb4bdc9cd732d0ad604931146191f6a7d58'),
    'reviews/wp2b/validation.json': (5252, 'add0af1ac7d83d17cc3c461307ebc3941112553fa5eda21b36a14b55b34d4ed6'),
    'reviews/wp2b/WP2B-acquisition-validation.md': (1561, 'ed4e20c9798c857546f3449d7c2bf08268d1329527667eb1931d95412e720066'),
}
SERIES = {
    'CPIAUCNS': ('cpi_u_nsa', 1363, '1913-01-01', '2026-08-01'),
    'DTB3': ('treasury_3m_discount', 18179, '1954-01-04', '2026-10-01'),
    'DGS5': ('treasury_5y_nominal', 16173, '1962-01-02', '2026-10-01'),
    'DGS10': ('treasury_10y_nominal', 16173, '1962-01-02', '2026-10-01'),
    'DFII5': ('tips_5y_real_yield', 5942, '2003-01-02', '2026-10-01'),
    'DFII10': ('tips_10y_real_yield', 5942, '2003-01-02', '2026-10-01'),
    'DFF': ('effective_federal_funds_rate', 26391, '1954-07-01', '2026-10-01'),
    'SOFR': ('sofr', 2123, '2018-04-03', '2026-10-01'),
}
HEADER = [
    'series_key', 'date', 'value', 'unit', 'frequency', 'source_series_id',
    'source_agency', 'distributor', 'retrieval_method', 'vintage_status', 'retrieved_utc',
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def hash_file(path: Path, algorithm: str = 'sha256') -> str:
    dig = hashlib.new(algorithm)
    with path.open('rb') as src:
        for chunk in iter(lambda: src.read(128 * 1024), b''):
            dig.update(chunk)
    return dig.hexdigest()


def git_blob_sha(path: Path) -> str:
    sha = hashlib.sha1()
    sha.update(f'blob {path.stat().st_size}\0'.encode('ascii'))
    with path.open('rb') as src:
        for chunk in iter(lambda: src.read(128 * 1024), b''):
            sha.update(chunk)
    return sha.hexdigest()


def verify_panel(path: Path) -> dict:
    counts = {sid: 0 for sid in SERIES}
    first = {}
    last = {}
    seen = set()
    with path.open('r', encoding='utf-8', newline='') as src:
        reader = csv.DictReader(src)
        require(reader.fieldnames == HEADER, 'unexpected panel header/schema')
        for row in reader:
            sid = row['source_series_id']
            require(sid in SERIES, f'unexpected series {sid}')
            expected_key, _, _, _ = SERIES[sid]
            require(row['series_key'] == expected_key, f'{sid}: incorrect stable series key')
            require(row['vintage_status'] == 'current_published', f'{sid}: incorrect vintage label')
            require(row['retrieval_method'] == 'date_bounded_fred_graph_csv', f'{sid}: unexpected retrieval method')
            require(row['distributor'] == 'FRED', f'{sid}: incorrect distributor')
            date = dt.date.fromisoformat(row['date']).isoformat()
            value = row['value']
            require(value not in ('', '.'), f'{sid}: missing/blank value')
            require(math.isfinite(float(value)), f'{sid}: nonfinite value')
            pair = (sid, date)
            require(pair not in seen, f'duplicate series/date: {pair}')
            seen.add(pair)
            counts[sid] += 1
            first[sid] = min(first.get(sid, date), date)
            last[sid] = max(last.get(sid, date), date)
    for sid, (_, wanted_count, wanted_first, wanted_last) in SERIES.items():
        require((counts[sid], first.get(sid), last.get(sid)) ==
                (wanted_count, wanted_first, wanted_last), f'{sid}: snapshot coverage mismatch')
    require(sum(counts.values()) == 92286, 'unexpected total observation count')
    return {'row_count': sum(counts.values()), 'series_count': len(counts), 'series_rows': counts}


def materialize(archive: Path = ARCHIVE, target: Path = OUTPUT) -> dict:
    require(archive.is_file(), f'archive missing: {archive}')
    require(archive.stat().st_size == ZIP_SIZE and hash_file(archive) == ZIP_SHA256,
            'archive size/SHA256 differs from binding Actions artifact')

    with zipfile.ZipFile(archive, 'r') as zipped:
        names = zipped.namelist()
        require(len(names) == len(MEMBERS) and set(names) == set(MEMBERS),
                'archive member names/count differ from binding artifact')
        for name, (expected_size, expected_sha) in MEMBERS.items():
            info = zipped.getinfo(name)
            require(info.file_size == expected_size, f'{name}: uncompressed size mismatch')
            dig = hashlib.sha256()
            byte_count = 0
            with zipped.open(info) as member:
                for block in iter(lambda: member.read(128 * 1024), b''):
                    byte_count += len(block)
                    require(byte_count <= expected_size, f'{name}: oversized member')
                    dig.update(block)
            require(byte_count == expected_size and dig.hexdigest() == expected_sha,
                    f'{name}: content SHA256 mismatch')
            if name != 'research/wp2b/data/core-observations.csv':
                committed = ROOT / name
                require(committed.is_file() and committed.stat().st_size == expected_size and
                        hash_file(committed) == expected_sha,
                        f'{name}: exact separately committed evidence missing or mismatched')

        source = json.loads(zipped.read('research/wp2b/data/source-hashes.json'))
        validation = json.loads(zipped.read('reviews/wp2b/validation.json'))
        panel_sha = MEMBERS['research/wp2b/data/core-observations.csv'][1]
        require(source['normalized_panel_sha256'] == panel_sha, 'provenance panel hash mismatch')
        require(validation['global_checks']['normalized_panel_sha256'] == panel_sha,
                'validation panel hash mismatch')
        require(validation['global_checks']['row_count'] == 92286 and
                validation['global_checks']['series_count'] == len(SERIES),
                'validation rows/series mismatch')
        require(validation['global_checks']['vintage_label'] == 'current_published',
                'validation incorrectly claims a first-release vintage')

        if target.exists():
            require(target.stat().st_size == MEMBERS['research/wp2b/data/core-observations.csv'][0] and
                    hash_file(target) == panel_sha and git_blob_sha(target) == EXPECTED_GIT_BLOB,
                    'existing standalone panel does not match binding artifact; refusing overwrite')
            results = verify_panel(target)
            results.update({'action': 'already_verified', 'git_blob_sha': EXPECTED_GIT_BLOB})
            return results

        target.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = None
        try:
            with tempfile.NamedTemporaryFile(mode='wb', dir=target.parent,
                                             prefix='.wp2b-restore-', delete=False) as tmp:
                tmp_path = Path(tmp.name)
                with zipped.open('research/wp2b/data/core-observations.csv') as member:
                    for block in iter(lambda: member.read(128 * 1024), b''):
                        tmp.write(block)
                tmp.flush()
                os.fsync(tmp.fileno())
            require(hash_file(tmp_path) == panel_sha and git_blob_sha(tmp_path) == EXPECTED_GIT_BLOB,
                    'restored panel does not match both SHA256 and Git blob SHA1')
            results = verify_panel(tmp_path)
            require(not target.exists(), 'target appeared during verification; refusing overwrite')
            os.replace(tmp_path, target)
            tmp_path = None
            results.update({'action': 'materialized', 'git_blob_sha': EXPECTED_GIT_BLOB})
            return results
        finally:
            if tmp_path is not None:
                tmp_path.unlink(missing_ok=True)


if __name__ == '__main__':
    print(json.dumps(materialize(), indent=2, sort_keys=True))
