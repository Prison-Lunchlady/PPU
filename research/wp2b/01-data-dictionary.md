# WP2B Data Dictionary

Date: 2026-09-30. Research use only.

## Observation contract

| Field | Meaning |
|---|---|
| series_key | Stable PPU research identifier |
| date | Native source observation/reference date |
| value | Source numeric observation; no automatic fill |
| unit | Source unit or explicit normalized unit |
| frequency | Native source frequency |
| source_series_id | Publisher/distributor series ID |
| source_agency | Originating authority; intermediary named separately |
| source_url | Retrieval endpoint |
| vintage_status | Current-published, release-vintage, derived, or unavailable |
| retrieved_utc | Acquisition timestamp |
| source_sha256 | Hash of retrieved source payload where machine retrieval succeeds |

## Core series contract

| series_key | Source ID | Frequency | Unit | Data role |
|---|---|---|---|---|
| cpi_u_nsa | BLS CUUR0000SA0 | monthly | CPI index, 1982-84=100 | PPU benchmark history |
| treasury_3m_discount | DTB3 | daily business | percent, discount basis | bill/short-rate environment |
| treasury_5y_nominal | DGS5 | daily business | percent, investment basis | nominal duration environment |
| treasury_10y_nominal | DGS10 | daily business | percent, investment basis | nominal duration environment |
| tips_5y_real_yield | DFII5 | daily business | percent | TIPS-era real-yield environment |
| tips_10y_real_yield | DFII10 | daily business | percent | TIPS-era real-yield environment |
| effective_federal_funds_rate | DFF | daily | percent | funding/policy environment |
| sofr | SOFR | daily business | percent | modern secured overnight funding |

## Non-negotiable data rules

- Do not forward-fill market observations merely to make a stress test run.
- Do not treat ex-post nominal yield minus CPI inflation as an observed tradable TIPS real yield.
- Do not fabricate TIPS history before the instrument/data series exists.
- Keep current-published history distinct from release-vintage history.
- Keep raw facts separate from any later WP2C transformations.
- A yield series is not a bond total-return series. WP2C must use an explicit pricing/roll model before turning yield changes into reserve P&L.
