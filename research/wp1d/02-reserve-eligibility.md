# Reserve Eligibility Specification
Revision 0.1 • Proposed research constraints, pending Gate 1D. No asset is production-approved.

## Conditional baseline eligibility
| Asset | Candidate role | Evidence required before eligible credit | Exclusion / failure |
|---|---|---|---|
| USD cash deposit | Operational settlement cash | Bank identity, deposit owner, account type, balance/finality, withdrawal access, verified insurance category/limits, setoff/lien rights | Not central-bank money; uninsured balance and common banking exposure need counterparty stresses; blocked account gets zero horizon credit |
| Direct Treasury bill | Dated liquidity / nominal sleeve | CUSIP, beneficial title, settled units, maturity, dirty market bid, custody and delivery calendar | No credit from unsettled purchases, pledged units, unverified title or assumed weekend sale |
| Short Treasury reverse repo, PPU as cash lender | Dated nominal receipt | Receivable amount/interest/term, Treasury-only collateral, margin, enforceable control and closeout, independent valuation, counterparty exposure | No borrowing against PPU reserve, no collateral double count, no renewal assumption; term repo inaccessible before payment/legally available closeout |
| Direct short remaining-duration TIPS | Partial inflation-matching sleeve | CUSIP, dated principal, Treasury index ratio separately from PPU target, clean+accrued valuation convention, remaining cash flows, duration/key-rate sensitivity, market depth | No maturity-floor sale guarantee, no stale/matrix quote treated as executable, no assumed protection from real-yield increases |

Every candidate must satisfy unit/currency identification, a common as-of time, complete ownership and encumbrance inventory, independent price evidence, conservative stressed conversion and availability, concentration tests, and auditable custody reconciliation. Unknown is not a passing eligibility result. Ledger inventory retains excluded assets and paired obligations; excluding an asset never extinguishes its creditor. Securities lending, rehypothecation, leveraged overlays, lending reserve assets for unrelated yield, opaque affiliates and unbacked receivables are excluded from the proposed baseline.

## Segmentation and constraints
1. Settlement sleeve: usable USD by actual payment deadline, including operating cash. Access is scenario-dependent; cash at a failed bank is not immediate liquidity.
2. Dated liquidity sleeve: short bills and qualifying reverse-repo maturities arranged across relevant horizons. Trading proceeds count only after executable sale and settlement delay.
3. Inflation sleeve: direct short TIPS with measurable cash flows, real-rate sensitivity and divergence from the PPU target.
4. Exception inventory: encumbered, disputed, stale, unsettled or inaccessible positions; disclose gross balances, no silent deletion or unexplained reserve credit.

Capital is a financing/economic layer across these assets, not a fifth asset sleeve. Proposed baseline prohibits investing a separately imagined equity amount on top of assets already financed by it.

## Limits pending calibration
Test bills remaining maturity <=1 year; baseline short-TIPS test bracket 0–2 years, contrasted with 5/10 years. These are candidate risk constraints, not tolerable-loss certification. Require issuer, banking group, custodian, settlement agent, repo counterparty and CUSIP concentration reports; a numerical cap is NOT invented before access and loss budgets exist. A Treasury-only portfolio remains sovereign-concentrated. See [parameters](10-parameters.md) for explicit statuses and rejection criteria.

Funds, tokenized Treasury wrappers and stablecoins are not automatically equivalent to direct holdings. Their own redemption, expenses, intermediate claims, liquidity, encumbrance and issuer/chain/bridge risk require separate eligibility. No alternative asset becomes eligible merely by an attractive backtest.
