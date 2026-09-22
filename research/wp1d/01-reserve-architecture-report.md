# Reserve Architecture Research Report
WP1D revision 0.1 • 2026-09-21 • RECOMMENDATION, pending Gate 1D. Source authority SRC019. Research only; no purchase, launch, legal conclusion or later-package authorization.

## Finding and scope
A segmented cash/bill/short-TIPS architecture is a defensible **candidate to test**, not demonstrated sustainable backing. No allocation here eliminates the conflict between inflation exposure, real-rate losses, settlement liquidity and negative net real carry. With a persistent negative net real return, finite capital can be exhausted even without a run. If viability requires perpetual external subsidy, that must be explicit at WP1E/Phase 2, not hidden inside a reserve yield assumption. Q023 independently prevents production activation regardless of the assets.

The approved liability is `L_PPU,v=(N_v+Qidx_v)*T_v+Qfix_v`, with version/obligor separation and effective replacement Q025 unresolved. Preserve monetary face, asset value, recovery value, legal seniority and statutory accounting as different quantities. This package recommends eligibility and analytical controls, not a capital instrument, return distribution, optimal ratio, fees, APs, redemption terms, entity, bankruptcy priority, production custodian or blockchain.

## Established evidence and interpretation
Treasury describes bills as nominal instruments paid at face on maturity and TIPS as inflation-adjusted principal with a floor at original principal on maturity. TIPS are issued at 5/10/30-year terms; a short remaining-maturity portfolio requires secondary selection, not an invented short TIPS auction. The floor does not guarantee a secondary purchase price or a forced-sale price. [S01–S02](11-sources.md).

Federal Reserve research identifies TIPS liquidity premia during the financial crisis and dealer-capacity pressure in March 2020 Treasury trading. Consequently, low sovereign credit risk is not sufficient evidence of realizability at a deadline. Repo margin and collateral do not remove closeout and settlement risks; FDIC coverage is conditional and limited, not blanket reserve insurance. [S03–S06](11-sources.md).

Treasury actually invoked a CPI contingency in 2025. Its liability is therefore not identical to PPU's fixed-vintage/impairment liability in all states. No Treasury fallback is imported into PPU. [S07](11-sources.md). Government concentration and CPI institutional dependence cannot be diversified away merely by mixing Treasury instruments.

## Recommended candidate, competing designs and falsifiers
Compare cash/bill-heavy A, mixed B, larger-liquidity C and TIPS-heavy D before alternative additions. B is a useful central **test case**, not a selected allocation. A reduces rate risk but fails prolonged inflation/net-real-carry tests; D reduces some index sensitivity mismatch but increases sale losses and availability dependence. C buys time at the expense of cash drag. No candidate is uniformly best across the synthetic cases. [Structures](03-candidate-structures.md), [calculations](scenario-results.json).

For a deliberately common A=120 and L=100 comparison, inflation+liquidity factors cash 1, bills .97, TIPS .90 and target +15% give assets A=117.12, B=113.76, C=116.16, D=110.88. Indexed liabilities are 115: buffers +2.12, -1.24, +1.16, -4.12. Positive starting overcollateralization fails for B and D. These are operator stress assumptions, not observed 1970s or COVID returns and not a 120% recommendation. Any realized loss, expense or liability increase uses economic buffer; no capital instrument is presumed available to replenish it.

## What would defeat this direction
An unsupported liquidity promise, inability to verify single asset ownership, incompatible legal access, repeated roll losses, procyclical forced sales, or a negative residual under reasonable stresses can defeat the candidate. Do not cure that result by recognizing fictitious assets, reducing gross claims, assuming central-bank access, adopting a new benchmark or forecasting new buyers. A simpler direct bill/TIPS portfolio may be preferable for users who do not need transfer/programming functionality; demand and the value of that functionality remain unproved Q021.

## Unresolved limits and package routing
WP1E must confront sustainable funding, expense drag and residual loss absorption without counting contributed cash twice. WP1F must determine outflow timing, fixed/indexed accepted claims, run incentives and pricing/discharge facts. Phase 2 must fit/reject parameters using historical instruments, joint shocks, transaction costs and Monte Carlo/adversarial paths. Phase 3 must establish actual ownership, legal access, insurance, priority and enforceability. Later technical work must authenticate complete off-chain evidence. None starts here. No chosen assets or successful tests cure Q023.

See the [Gate submission](../../reviews/gate1d/Gate-1D-submission.md) for current status and review coverage. Roadmap and unratified draft constitution retain original text; their WP1D implications are mapped in the package register and this report, not silently ratified.

## Qualification of headline comparisons after review
The40 original return-factor comparisons are gross of operating expenses and incremental execution costs. Positive gross buffers are not net-survival results. The expanded640 joint cases add both costs and a run;216 run cases expose post-redemption proportional shortfall;560 joint alternative comparisons measure incremental buffer against the same shocked baseline. Exact code and declared input limits are reviewed in the package, but no scenario magnitudes are calibrated or claimed historical.
