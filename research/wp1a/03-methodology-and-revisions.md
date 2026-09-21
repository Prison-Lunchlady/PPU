# Benchmark Methodology and Revision Analysis
WP1A • 2026-09-19 • Facts, interpretation and open implementation requirements

## Measurement construction
**Established facts:** CPI-U is not a permanently fixed physical basket. Expenditure weights are updated annually using lagged Consumer Expenditure information; most elementary indexes use geometric means, while upper aggregation uses a modified Laspeyres approach. Sampling, product replacement and quality adjustment are part of the measurement process. [BLS calculation handbook](https://www.bls.gov/opub/hom/cpi/calculation.htm).

The final C-CPI-U uses monthly contemporaneous expenditure weights and a Törnqvist construction to account for substitution across categories. BLS describes final data as posted 10–12 months after initial release. That is a release-vintage rule, not a guaranteed fixed delay from every observation date; consult the actual publication schedule. **Source discrepancy observed September 19, 2026:** the [chained CPI FAQ, Q9](https://www.bls.gov/cpi/additional-resources/chained-cpi-questions-and-answers.htm) describes three interim revisions, while the current [August 2026 Table 5 footnote 1](https://www.bls.gov/news.release/cpi.t05.htm) says four revisions. This package does not reconcile that publication wording into a fabricated exact count. The comparison relies on provisional/final vintages and roughly year-long finalization, not the disputed count.

PCE uses Fisher chain weighting and covers spending financed on people's behalf as well as directly by them. Its weights are not permanently fixed. These choices make it a different economic object, not merely a more accurate release of CPI. [BEA formula](https://www.bea.gov/help/faq/1006), [BEA comparison](https://www.bea.gov/help/faq/555). BEA's revision study documents changes in monthly PCE estimates as source information develops. Freezing a preliminary value would make PPU track a specified vintage, not necessarily the subsequently published historical PCE path. [BEA revision analysis](https://apps.bea.gov/scb/issues/2024/08-august/0824-revisions-to-gdp-gdi.htm).

## Three distinct clocks
1. **Observation and weight age:** some prices and expenditure information refer to earlier periods; monthly labels are not real-time shopping quotes.
2. **Publication lag:** CPI for a reference month is normally published in the following month; actual dates vary. Use the [BLS calendar](https://www.bls.gov/schedule/news_release/cpi.htm), not a claimed universal number of days.
3. **Contractual reference lag:** Treasury's first-of-month reference uses CPI for the third preceding month and interpolates toward the next month's reference. Thus April 1 references January CPI, ordinarily released in February. This is additional intentional timing, not a three-month BLS publication delay. Treasury also specifies decimal treatment and unrevised vintages. These are existing Treasury rules, **not rules selected for PPU**. [31 CFR 356, Appendix B, I.B](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-II/subchapter-A/part-356).

**Interpretation:** interpolation smooths the reference between already measured points; it neither observes today's price level nor removes lag. The whole CPI production process has no single precise age that can be inferred from the interpolation label.

## Revision and outage distinctions
NSA CPI-U is ordinarily final for routine release purposes, but errors can be corrected. Seasonally adjusted CPI is recalculated with annually updated seasonal factors, revising the prior five years. NSA avoids that recurring vintage problem, not all error risk. [BLS FAQ](https://www.bls.gov/cpi/questions-and-answers.htm), [BLS seasonal adjustment](https://www.bls.gov/cpi/seasonal-adjustment/).

A July 2026 BLS correction involved June Tampa-area electricity/energy data. This is evidence that correction procedures operate, **not** evidence that national all-items CPI-U changed in that incident. [BLS correction notice](https://www.bls.gov/cpi/notices/2026/electricity-correction-202606.htm).

The 2025 appropriations lapse prevented October CPI collection/publication. BLS discusses carry-forward inputs for subsequent compilation; that does not create a published October headline CPI. Treasury separately announced **325.604** for October 2025 under its contingency provisions on November 26, to remain binding for its obligations even if BLS later reports an October value. These are distinct statistical and contractual actions. [BLS shutdown FAQ](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm), [Treasury announcement](https://home.treasury.gov/news/press-releases/sb0324).

HICP permits revisions, so “official” does not imply immutable; the scope excludes imputed housing rent. CPIH serves a different housing-inclusive UK concept. Neither is silently assigned NSA CPI-U's revision properties. [Eurostat metadata](https://webgate.ec.europa.eu/eurostat/cache/metadata/en/prc_hicp_esms.htm), [ONS definition](https://www.ons.gov.uk/datasets/cpih01/editions/time-series/versions/66).

**Persistent historical gap:** October 2025 national all-items CPI is absent from the published series as of this review, not awaiting an ordinary delayed release. November commodity/service comparisons used October inputs carried forward from September, so those comparisons span the missing collection interval; do not characterize every CPI component identically. For affected monthly series, the 2025 annual average uses eleven published months, reducing comparability with normal twelve-month averages. This is a documented gap and compilation limitation, not proof of a deliberately distorted statistic. No missing CPI value is invented here. [BLS historical table](https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm), [shutdown FAQ Q2/Q5/Q10](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm).

Truflation's current methodology distinguishes frozen published values from revised observations and carries forward lower-frequency data. Daily publication does not establish daily measurement of every component. Immutable storage is not equivalent to one unrevisable economic truth. These are provider claims, not an independent operational audit. [TruCPI-US methodology v1.4, March 26, 2026](https://ddsvqvocwuhvopwpzmgo.supabase.co/storage/v1/object/public/site-files/indexes/1774868881730-TruCPI-US%20Index%20-%202026%20-%20Methodology%20v1.4%20%282026-03-26%29.pdf).

## Illustrative significance of lag — not a backtest
For a hypothetical smooth annual price increase r and a stylized three-month-old measure, current price / lagged price − 1 = (1+r)^(3/12) − 1.

| Hypothetical annual rate | Current level above three-month-old level |
|---|---:|
| 3% | 0.742% |
| 10% | 2.411% |
| 20% | 4.664% |

If prices instead jump 10% immediately and the target has not responded, unchanged nominal target buys 1/1.10 − 1 = **−9.091%** less of the affected basket. This simplified scenario isolates timing. It is not the exact TIPS lag profile, PPU performance, a forecast or an approved tolerance. Under falling prices the direction can reverse. Actual tolerances and shock tests belong to WP1B requirements and Phase 2 validation.

## Reproducibility boundary and handoff
Public output verification: identify series, observation month, release timestamp/vintage and preserved value. Deterministic transformation: calculate the same answer from those fixed inputs using a complete specification. Independent statistical reconstruction: repeat sampling and estimation from underlying observations. Only the first is presently established as a practical public-data operation; the second needs WP1B; the third is constrained by confidential statistical data. [BLS confidentiality framework](https://www.bls.gov/bls/cipsea-report.htm).

WP1B must resolve base reference, observation vintage, publication authentication, arithmetic, day convention, corrections, missing values, prolonged outages and negative inflation behavior. WP1G must resolve any methodology/contingency authority. WP1A neither picks those rules nor treats Treasury's choices as automatically inherited. The old draft's “no forecasts” position versus Treasury extrapolation is a newly evidenced tension, preserved for those packages.
