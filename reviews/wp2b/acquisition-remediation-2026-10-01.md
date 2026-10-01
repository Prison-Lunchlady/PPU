# WP2B Acquisition Remediation Record — 2026-10-01

Package: WP2B — Historical Data Environment  
Disposition: **REVISION REQUIRED — repository persistence remediation remains**  
WP2C authorization: **BLOCKED**

## What changed

The prior bulk FRED graph-CSV path was replaced on the remediation branch with the lower-bandwidth official FRED static table distribution path:

`https://fred.stlouisfed.org/data/<SERIES_ID>.txt`

The revised acquisition script preserves current-published vintage labels, does not forward-fill/backfill/interpolate, does not fabricate unavailable TIPS or SOFR history, hashes each retrieved source payload, produces a normalized long-form panel, and generates a machine validation record plus a human-readable validation report.

## Successful acquisition evidence

GitHub Actions run: **36872043428**  
Branch/head: `work/wp2b-remediation-2026-10-01` @ `099b0d87974898912ccccdb8904cdd10bad5e758`  
Conclusion: **SUCCESS**

The workflow's executed checks reported:

- series_count: **10**
- normalized row_count: **9,685**
- unique_series_date: **true**
- all_series_nonempty: **true**
- all_fabricated_rows_zero: **true**
- vintage_label: **current_published**
- normalized panel SHA256: `91d6c0acc02ca57382ce515e59716739cdff30200604d8fde67657a1e671509e`

Generated outputs existed and passed nonempty checks inside the run:

- `research/wp2b/data/core-observations.csv`
- `research/wp2b/data/source-hashes.json`
- `reviews/wp2b/validation.json`
- `reviews/wp2b/WP2B-acquisition-validation.md`

Workflow artifact: **11167391560** (`wp2b-remediation-output`)  
Artifact ZIP SHA256: `11cbb227277868e648b975f10e922027ee7c9cca0dec03d4bfd6f47a85fd05ec`

The artifact contains the generated panel, per-source payload hashes/provenance, validation JSON and human-readable validation report.

## Why WP2B is still not complete

The generated files were successfully produced and preserved as a GitHub Actions artifact, but they are not yet committed into the repository tree. The Actions token for the successful run had read-only Contents permission, and the connector safety layer did not permit creating a self-writing workflow. The local container/Python extraction path was also unavailable in this run, so the artifact could not be safely unpacked and re-committed through the connector.

Therefore the package still fails the standing condition that the historical observation panel, provenance hashes and validation report be **inspectable and version-controlled in the repository**. An expiring Actions artifact is evidence of successful generation, not a substitute for canonical persistence.

Do not merge or mark WP2B COMPLETE from this record alone.

## Data limitations preserved

- CPI in the generated panel is current-published history, not a complete first-release-vintage archive. **Q033 remains OPEN.**
- Yield observations remain yields, not total-return observations.
- Pre-existence TIPS/SOFR periods are not silently backcast.
- License/provenance-limited alternative market histories remain excluded. **Q034 remains OPEN.**
- **Q023 remains the monetary production-activation blocker.**

## Next bounded work

WP2B repository-persistence remediation only. Persist the exact generated panel/provenance/validation outputs into a version-controlled work branch, verify their hashes against the successful run, then re-review WP2B. Do not begin WP2C until that condition is met.

Claude/Anthropic was not available as a callable connector in this run; no Claude review or endorsement is claimed.
