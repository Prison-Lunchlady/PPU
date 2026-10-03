# WP2B Acquisition Validation Report

Retrieved UTC: 2026-10-03T13:58:38+00:00
Normalized panel SHA256: `dd728aa4ca1592dda6aa48389046b3fd47bad4181aede69cb8160f81f2d60ba0`
Rows: 92286 across 8 series
Overall validation passed: **True**

| Series | Rows | Start | End | Staleness days | Coverage guards | Missing markers excluded |
|---|---:|---|---|---:|---|---:|
| CPIAUCNS | 1363 | 1913-01-01 | 2026-08-01 | 63 | True | 1 |
| DTB3 | 18179 | 1954-01-04 | 2026-10-01 | 2 | True | 787 |
| DGS5 | 16173 | 1962-01-02 | 2026-10-01 | 2 | True | 711 |
| DGS10 | 16173 | 1962-01-02 | 2026-10-01 | 2 | True | 711 |
| DFII5 | 5942 | 2003-01-02 | 2026-10-01 | 2 | True | 250 |
| DFII10 | 5942 | 2003-01-02 | 2026-10-01 | 2 | True | 250 |
| DFF | 26391 | 1954-07-01 | 2026-10-01 | 2 | True | 0 |
| SOFR | 2123 | 2018-04-03 | 2026-10-01 | 2 | True | 95 |

## Acceptance checks

- Unique series/date keys: **True**
- All series nonempty: **True**
- All per-series coverage guards passed: **True**
- Fabricated rows recorded: **0**
- Vintage label for this panel: **current_published**
- No forward fill, backfill or interpolation is performed.
- TIPS and SOFR begin only where the official source publishes observations.
- Every date-bounded payload is individually SHA-256 hashed in source-hashes.json.

## Limits

- This panel does not reconstruct the first-release CPI vintages required for protocol-faithful WP1B replay; Q033 remains open.
- Yield series are not total-return series.
- Alternative market-price series with unresolved redistribution terms remain omitted.
