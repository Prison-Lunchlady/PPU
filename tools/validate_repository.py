"""Offline integrity, navigation, privacy-pattern and scope checks for the import."""
from pathlib import Path
import hashlib, json, re, sys, zipfile, gzip, base64
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
checks = 0
def check(ok, label):
    global checks
    checks += 1
    if not ok: errors.append(label)
def digest(b): return hashlib.sha256(b).hexdigest().upper()
provenance = json.loads((ROOT/'archive/import-provenance.json').read_text())
amended = {'README.md','CHANGELOG.md','docs/workspace-guide.md'} | {x['repository_path'] for x in provenance['files'] if x['repository_path'].startswith('docs/canonical/')}
for item in provenance['files']:
    p = ROOT/item['repository_path']
    check(p.is_file(), 'Missing: '+item['repository_path'])
    if p.is_file() and item['repository_path'] not in amended:
        check(digest(p.read_bytes()) == item['repository_sha256'], 'Unchanged import hash: '+item['repository_path'])
current=json.loads((ROOT/'reviews/gate1d/submission-manifest.json').read_text(encoding='utf-8'))
for item in current['files']:
    p=ROOT/item['path']
    check(p.is_file() and digest(p.read_bytes())==item['sha256'], 'Current submission hash: '+item['path'])
review_core=json.loads((ROOT/'reviews/gate1d/stage4-lossless-core.json').read_text(encoding='utf-8'))
for item in review_core['files']:
    decoded=gzip.decompress(base64.b64decode(item['gzip_base64']))
    check(digest(decoded)==item['sha256'],'Lossless submitted byte hash: '+item['path'])
    now=(ROOT/item['path']).read_bytes()
    # Only post-review administrative disclosure/findings may be prepended/appended to
    # these two records. Material research/model files must remain byte-exact.
    append_only=item['path'] in ('reviews/gate1d/Gate-1D-submission.md','reviews/gate1d/claude-reconciliation.md')
    check(now==decoded or (append_only and (now.startswith(decoded) or now.endswith(decoded))), 'Current submitted core or administrative review metadata: '+item['path'])
authority=json.loads((ROOT/'evidence/gate1c-wp1d-source-provenance.json').read_text(encoding='utf-8'))
check(digest((ROOT/'evidence/gate1c-approval-wp1d-authorization.txt').read_bytes())==authority['repository_sha256'],'SRC019 source provenance hash')
for name in ['07-development-roadmap.md', 'evidence/PPU_full_recovered_source.txt']:
    item = next(x for x in provenance['files'] if x['source_path']==name)
    check(item['original_sha256']==digest((ROOT/item['repository_path']).read_bytes()), 'Verbatim source: '+name)
with zipfile.ZipFile(ROOT/'archive/PPU-WP1A-Gate1A-package-public-copy.zip') as baseline:
    draft = baseline.read('ppu-work/08-draft-constitution.md')
    item = next(x for x in provenance['files'] if x['source_path']=='08-draft-constitution.md')
    check(digest(draft)==item['original_sha256'], 'Archived draft verbatim')
    expected = draft.decode('utf-8-sig').replace('\r\n','\n').replace('(evidence/PPU_full_recovered_source.txt)','(../../evidence/PPU_full_recovered_source.txt)').replace('(reviews/source-recovery-reconciliation.md)','(../../reviews/wp0a/source-recovery-reconciliation.md)')
    check((ROOT/item['repository_path']).read_text(encoding='utf-8-sig')==expected, 'Draft changes limited to two navigation links')
link_count=0
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts: continue
    s=p.read_text(encoding='utf-8-sig')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',s):
        if re.match(r'^[a-zA-Z]+:|^#',target): continue
        link_count+=1
        path=unquote(target.split('#')[0])
        check((p.parent/path).exists(), 'Broken link: '+str(p.relative_to(ROOT))+' -> '+target)
state=(ROOT/'docs/canonical/01-protocol-state.md').read_text(encoding='utf-8-sig')
gates=(ROOT/'docs/canonical/10-review-gate-register.md').read_text(encoding='utf-8-sig')
check('**Review Gate 0:** APPROVED WITH CONDITIONS' in state, 'Gate 0 state')
check('**Review Gate 1A:** APPROVED WITH CONDITIONS' in state, 'Gate 1A state')
check('**Current package:** WP1D — Reserve Architecture' in state and 'COMPLETE FOR REVIEW' in state, 'WP1D state')
check('Status: **APPROVED WITH CONDITIONS** under SRC018' in gates and '## Gate1B' in gates, 'Gate 1B approved with conditions')
check('## Controlling Gate1C disposition — SRC019' in gates and '**Review Gate 1C:** APPROVED WITH CONDITIONS' in state, 'Gate 1C approved with conditions')
check('Status: **AWAITING REVIEW / NOT APPROVED**. WP1D' in gates and '## Gate1D' in gates, 'Gate 1D review pending')
check('WP1E NOT AUTHORIZED' in state, 'Successor authorization')
standard='PPU v0.1 targets U.S. urban consumer-price-indexed purchasing power using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted (CUUR0000SA0).'
for path in ['README.md','docs/canonical/01-protocol-state.md','docs/canonical/02-decision-register.md','docs/canonical/10-review-gate-register.md','evidence/gate1a-approval-2026-09-21.txt']:
    check(standard in (ROOT/path).read_text(encoding='utf-8'), 'Exact approved wording: '+path)
check('C-CPI-U and PCE are live research comparators' in state,'Live comparators')
check('Treasury contingency-methodology conflict stays OPEN' in state,'Open Treasury conflict')
check('does not establish demonstrated user demand' in state,'Demand remains unproven')
check('2025 CPI data gap is a mandatory WP1B design input' in state,'Mandatory 2025 gap')
model=json.loads((ROOT/'research/wp1b/model-validation.json').read_text(encoding='utf-8'))
check(model['pass'] and len(model['checks'])==159 and not model['failed'],'159 model checks')
fresh=json.loads((ROOT/'research/wp1b/revalidation.json').read_text(encoding='utf-8'))
check(fresh['passed']==12 and not fresh['failed'],'12 new invariant checks')
impairment=json.loads((ROOT/'research/wp1b/impairment-validation.json').read_text(encoding='utf-8'))
check(impairment['passed']==49 and not impairment['failed'],'49 impairment and comparative counterexample checks')
policy=(ROOT/'research/wp1b/18-benchmark-impairment-policy.md').read_text(encoding='utf-8')
for dimension in ['Inflation and deflation','Transacting holders','Liability uncertainty','Reserve consequences','Manipulation / governance','Gate 1A compatibility','Historical finality','Oracle / authentication','Potential arbitrage','Principal failure modes']:
    check('| '+dimension+' |' in policy,'Three-alternative matrix: '+dimension)
check('BENCHMARK_IMPAIRED' in policy and 'PERSISTENT_UNRESOLVED' in policy and 'STRUCTURAL_CONFIRMED' in policy,'Explicit separate impairment causes')
check('activation blocker' in policy,'Structural remedy remains activation blocker')
check('SRC019' in state,'Current approval and WP1D authority')
liability=json.loads((ROOT/'research/wp1c/liability-validation.json').read_text(encoding='utf-8'))
check(liability['passed']==58 and not liability['failed'],'58 WP1C accounting checks')
reserve=json.loads((ROOT/'research/wp1d/validation.json').read_text(encoding='utf-8'))
check(reserve['passed']==139 and not reserve['failed'],'139 WP1D diagnostic assertions')
scenarios=json.loads((ROOT/'research/wp1d/scenario-validation.json').read_text(encoding='utf-8'))
check(scenarios['passed']==20 and not scenarios['failed'],'20 WP1D reproduction and scenario assertions')
check('production-activation blocker' in state and 'Q-023' in state,'Structural remedy remains open activation blocker')
check('not a formal platform export' in state, 'SRC003 provenance')
check(not list(ROOT.glob('LICENSE*')), 'No license added')
patterns={
 'credential':r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----)',
 'local_account':r'C:[\\/]+Users[\\/]+[^\\/\s]+',
 'private_chat_url':r'https://(?:chatgpt.com|claude.ai)/[^\s)"<>]+',
 'email':r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',
 'assigned_secret':r'(?i)(?:api_key|access_token|client_secret|password)\s*[:=]\s*[\"\x27][A-Za-z0-9_+/=-]{16,}'
}
scanned=0
def scan(name,b):
    global scanned
    if Path(name).suffix=='.pdf':
        import io
        from pypdf import PdfReader
        reader=PdfReader(io.BytesIO(b))
        s='\n'.join(p.extract_text() or '' for p in reader.pages)+'\n'+str(reader.metadata)
    else:
        try:s=b.decode('utf-8-sig')
        except UnicodeDecodeError:
            check(False,'Unscanned binary: '+name);return
    scanned+=1
    for label,pattern in patterns.items():check(not re.search(pattern,s), 'Privacy/secret pattern '+label+': '+name)
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts:continue
    name=p.relative_to(ROOT).as_posix()
    if p.suffix=='.zip':
        check(digest(p.read_bytes())==provenance['public_copy_sha256'],'Public-copy ZIP hash')
        with zipfile.ZipFile(p) as z:
            for n in z.namelist():scan(name+'!'+n,z.read(n))
    else:scan(name,p.read_bytes())
report={'scope':'Gate 1C conditional approval and WP1D research submission; final Claude review unavailable; no production certification or independent economic validation','checks':checks,'wp1b_model_policy_checks':220,'wp1c_accounting_checks':58,'wp1d_diagnostic_assertions':139,'wp1d_reproduction_scenario_assertions':20,'local_markdown_links_checked':link_count,'files_and_archive_entries_scanned':scanned,'status':'PASS' if not errors else 'FAIL','errors':errors,'gate0':'APPROVED WITH CONDITIONS','wp1a':'COMPLETE','gate1a':'APPROVED WITH CONDITIONS','wp1b':'REVISION 0.3 ACCEPTED FOR CONTINUED DEVELOPMENT','gate1b':'APPROVED WITH CONDITIONS','wp1c':'REVISION 0.1 ACCEPTED WITH CONDITIONS','gate1c':'APPROVED WITH CONDITIONS','wp1d':'COMPLETE FOR REVIEW','gate1d':'AWAITING REVIEW / NOT APPROVED','wp1e':'NOT AUTHORIZED','Q023':'OPEN; PRODUCTION-ACTIVATION BLOCKER','privacy_scan_limit':'Pattern scan plus PDF text/metadata extraction; not proof against every possible secret format. Historical manifests apply to original bytes; current submission manifest applies to current maintained files.'}
(ROOT/'reviews/repository-validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
sys.exit(bool(errors))
