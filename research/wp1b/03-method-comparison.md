# Daily / Monthly Target Method Comparison

All choices below retain CPI-U; Gate 1A did not choose the transformation. These are analytical alternatives, not historical backtest results.

| Commitment axis | Daily shape | Monthly shape | Release step |
|---|---|---|---|
| Fixed advance cutoff |Recommended candidate; known path for24h+Ddays |Same evidence/cutoff, known boundary step; less interpolation lag |Possible scheduled step after a known release, adds admission delay |
| Reactive to receipt |Requires a prospective catch-up window and freezes already elapsed values |Monthly implementation may still reserve a boundary; advance knowledge can be short |Immediate admitted-value step, lowest response delay, greatest release-time ordering exposure |

Precommitment creates the predictable path; daily/monthly determines its shape. They are not synonymous. The recommendation remains conditional after considering both axes;17 records the argument with the TIPS matching benefit removed.

| Method | Strength | Adversarial failure / cost | Disposition |
|---|---|---|---|
| Release-time step to newest CPI | Lowest contractual delay beyond publication; simple ratio | Release/oracle ordering changes transaction values; discontinuity equals whole observed change; outage recovery jump; still not spot prices | Credible alternative if lag dominates; not recommended under current finality/matching priority |
| Monthly step at UTC month start to M−2 | Known fixed change time, no interpolation | Known entire monthly jump concentrates exposure around a boundary; no within-month measured information gained; no ordinary TIPS daily path | Closest fallback alternative; reject provisionally, not mathematically inferior |
| Normal TIPS daily formula with frozen monthly plans | Exact preknown daily increments; ordinary mathematical index matching; fewer contingent timestamp decisions | Adds lag; known daily carry; missing data break matching; catch-up slope | Recommend adaptation in 01 |
| Copy all TIPS conventions | Maximum contractual convention similarity to a TIPS position | Imports forecasts, Secretary's replacement judgment, separate rounding and maturity floor issues | Reject direct copying |
| Continuous per-second interpolation | Spreads same increment more finely | More timing surface; no new price evidence; differs from TIPS day convention | Reject added precision without measurement benefit |
| Latest-release daily catch-up over arbitrary window | Lower apparent lag than TIPS | Window choice and midmonth re-planning complicate obligations; can cancel previously promised path | Defer/reject for v0.1 |
| Nowcast / forecast | Attempts current-price estimate | Model error, revisions, discretion, extra data and manipulation channels | Reject absent evidence of superior net architecture |

For synthetic 300→330: a monthly step moves 10% at one boundary; a 30-day interpolation moves 1/300 of base value per day (USD 0.003333… with I0=300), reaching USD 1.10 at the next boundary. Both are predictable and expose issuance/redemption timing economics. Daily interpolation reduces single-boundary concentration, not free arbitrage or capital needs. Later WP1F must test transaction timing; this report does not fix fees, collateral or redemption rights.

Reason for recommendation is contractual exposure distribution plus ordinary TIPS formula compatibility, not visual smoothness. A material cost is approximately 2.5 months of price-observation age in a stylized midpoint convention. If users prioritize prompt index reflection over this compatibility, monthly/release steps deserve reconsideration. Q021 has no demand evidence and remains OPEN.

## Common shock comparison — adverse to the recommendation

Synthetic prices jump from300 to330 on January1,2026 and remain there; January CPI is330 and is assumed published/admitted February13 at00UTC solely for day-grid comparison (not an actual BLS release time). Previous monthly CPI=300; I0=300. Compare through March31,90days; source evidence is identical for all methods, and none forecasts.

| Method | First reflection / full reflection | Sum of daily purchasing-power shortfalls over90days |
|---|---|---|
| Release step |February13 / February13 |43/11=3.909091 shortfall-days |
| Month-start M−2 step |March1 / March1 |59/11=5.363636 shortfall-days |
| Recommended daily M−3→M−2 |March2 / April1 |75/11=6.818182 shortfall-days |

Shortfall for a day is1−T/1.1. A shortfall-day sums that dimensionless fraction over one day, not a dollar cost, return or welfare estimate. This counterexample shows daily interpolation is *worse* on prompt purchasing-power restoration. Recommendation therefore depends on valuing distributed contractual changes and ordinary TIPS reference compatibility enough to accept that disadvantage. It is not a dominant solution. Reverse the shock to show analogous delayed nominal declines under deflation. No observed demand or hedge-cost evidence resolves the weighting; Gate1B must explicitly assess it.

Six missed monthly increases of5% imply a next observed level1.05^6=1.340095640625 times the old endpoint. One31day catch-up month moves about0.010970827117 of the original base per day. Issuance blocking does not remove holder incentives to time redemptions, particularly before known deflation. These are quantified dependencies for WP1C/1F/Phase2, not resolved arbitrage economics. A faster step or slower recovery changes these costs; no cap is selected here.
