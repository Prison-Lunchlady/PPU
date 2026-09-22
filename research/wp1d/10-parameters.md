# Parameter and Assumption Register
Revision0.1 • all numerical portfolio/risk parameters below remain HYPOTHESES or synthetic inputs, not accepted values.

| ID | Parameter/assumption | Status, rationale and falsification |
|---|---|---|
| P1D01 | Common assets120/liabilities100 USD million | Scale-only comparative assumption; not optimal ratio or loss budget |
| P1D02 | Cash/bill/TIPS weights A20/80/0 B20/40/40 C40/40/20 D10/20/70 | Tradeoff probes, no selected allocation; fail if stress/availability infeasible |
| P1D03 | TIPS remaining horizon0–2 years candidate; test0.5/2/5/10 | Secondary-market availability/cost unverified; duration is not remaining maturity |
| P1D04 | Bills<=1year; repo overnight/7/30-day test buckets | Nominal exposures, terms illustrative; cannot count receipts before access |
| P1D05 | Real-yield shifts±100/300/500bp from2% | Synthetic instantaneous diagnostics, not forecasts or calibrated tails |
| P1D06 | Inflation-.10/+.02/+.10/+.15 and stress returns | Regime analogues only; extreme-.90/+200% arithmetic tests not forecasts |
| P1D07 | Liquidity0/24/72h,7/30d; demand up to100%;cost0/2/10/20% | Must become term-specific; no queue/fee policy chosen |
| P1D08 | Complete title/claims/price evidence | Explicit assumption; fail coverage assertion if missing, Q025/Phase3 |
| P1D09 | No borrowing, renewal, new inflow or official rescue | Conservative base stress; conditional source must be separately authorized/tested |
| P1D10 |20% of liability fixed for branch comparison | Not selected queue type; other proportions must be tested later |
| P1D11 |5% alternative addition with adverse tails | Counterexamples, not historical empirical distribution/correlation model |
| P1D12 | Negative net real carry-2% for10years | Falsifier of permanent finite-buffer sufficiency; WP1E economics open |
| P1D13 | Pricing convention, quote freshness, concentration caps, operational margin | UNCALIBRATED; no production eligibility without evidence/limits |
| P1D14 | Joint shock factors and incremental discounts disjoint | Test loss reconciliation; cannot apply observed distressed price twice |
| P1D15 | Secured-asset/claim allocation known | Conditional calculation only; full inventory also needed; legal netting unknown |

Rejected shortcuts: treat Treasury as risk-free liquidity; use TIPS maturity floor as current-price floor; use totalSupply as liability; count capital again; assume guaranteed rollover; turn a quoted margin into cash; backfill CPI with Treasury substitute; select fixed/indexed claims to make the portfolio pass; calibrate safe limits from this small suite.

Facts versus inferences: product terms/historical mechanisms in [sources](11-sources.md) are external evidence; weights, shocks and accounting diagnostics are operator assumptions; tests establish identities under those inputs only. Review opinions are attributed in [reconciliation](../../reviews/gate1d/claude-reconciliation.md); Brad controls Gate decisions.
