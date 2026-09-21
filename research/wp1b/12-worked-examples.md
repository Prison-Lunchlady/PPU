# Worked Numerical Examples

All synthetic except the explicitly identified Treasury example and BLS/Treasury 2025 comparison. Exact executable outputs in [model-validation.json](model-validation.json); reproduction: `python test_reference_model.py` from this directory (standard library).

1. Normal, I0=300, S=300, E=303, 30-day April: day1=1; day16=1+(15/30)(3/300)=1.005000000000000000; day30=1.009666666666666667; next month day1=1.010000000000000000. No rounding feeds the next endpoint.
2. High inflation: S=300, E=330 gives day16=1.05, next start1.10. Endpoints363,399.3,439.23 continue uncapped. A target rising correctly does not ensure funded liabilities.
3. Deflation: 300→294→288 gives .98 and .96 at subsequent month starts. No nominal floor or balance rebase.
4. Missing October analogue: E(December)=324.800. E(January)=324.122 if admitted. January16 J=324.800+(15/31)(−.678)=324.4719354838709677…; with illustrative I0=324.800, T≈0.998989949150. This does not impute October.
5. Correction: original February303 stays in April's committed plan after a correction to302. April16 remains1.005; an unresolved hold fixes May endpoint303. No historical redemption/accounting recalculation is prescribed.
6. Rebase: old-base CPI303 and officially exact new-base101 with K=3 yield identical normalized index303. If K was guessed from rounded outputs, equivalence is unproven and admission must hold. I0 stays300.
7. External vector: Treasury April15,1996:154.40+(14/30)(154.90−154.40)=154.633333…; five-place reference154.63333. PPU would retain exact rational internally instead of Treasury's intermediate rounding. [Treasury rule](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-II/subchapter-A/part-356).
8. Half-even 18-place rounding: exact1+0.5×10^−18→1.000000000000000000; exact1+1.5×10^−18→1.000000000000000002. Maximum absolute one-target quantization error is 0.5×10^−18 dollars. It is not the error bound for summing many separately rounded transaction amounts.
9. Leap February: 29 days, S300,E329; day29 index328, next start329. Local clock changes never add/remove a target day.
10. Strict cutoff: for April2026, C=March31 00:00UTC. Receipt at C is late. Publication March30 plus delayed protocol receipt March31 does not qualify retroactively.

Lag scenario values and the two denominators are preserved in model-validation.json. Rounding examples are arithmetic validation, not assurance about measurement, assets, contracts or software security.

## Long-gap recovery grid
With n missing expected observations, the next expected observation is n+1monthly intervals after the last admitted endpoint. At0%annual, all slopes are0 (multiples undefined). At3%annual, recovery increases for n=2/3/6 are0.741707%/0.990163%/1.739215%, and slope multiples against one ordinary month from the same start/day count are3.0074/4.0148/7.0520. At20%annual, increases are4.663514%/6.265857%/11.221580%, multiples3.0462/4.0928/7.3298. Exact high-precision synthetic fixture values, daily steps and pre-recovery real shortfalls are in model-validation.json. No missing observation is filled in.
The separate six *price changes* example in03 is not six missing observations plus recovery; the interval count is stated deliberately. Actual delays/freeze duration can be unbounded.

