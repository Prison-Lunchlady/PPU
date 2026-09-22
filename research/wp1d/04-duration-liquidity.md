# Duration and Liquidity Analysis
Revision 0.1 • proposed measurement and diagnostic tests, not finalized risk appetite.

## Rate exposure
TIPS respond to real discount rates as well as indexed principal. Nominal bills respond to nominal yields; rolling short maturities trades smaller current price sensitivity for reinvestment risk. Measure modified duration, convexity and key-rate exposures by asset, sleeve and entire reserve. Weighted duration is not a substitute for a maturity cash-flow schedule or a stressed executable bid.

Local diagnostic `ΔP/P ≈ -Dmod*Δy` uses years times annual yield change (e.g.300bp=.03). It is not a large-shock valuation. The executable comparison uses exact semiannual zero-coupon repricing `P1/P0=((1+y0/2)/(1+y1/2))^(2m)`, holding maturity m fixed for an instantaneous shock. This is an educational proxy, not a real coupon TIPS including index accretion, cash-flow timing, convexity of coupons or the maturity option. Scenarios use explicit total-return factors instead of multiplying this rate diagnostic into an already stressed TIPS return; no same-loss double counting.

At2% initial yield and+300bp, the exact10-year zero loses about25.54%; the2-year loses about5.73%. Calculate precise outputs in [results](scenario-results.json). A10-year duration is not made appropriate by10-year expected holder loyalty: claims may be transferable/redeemable and fixed claims need nominal funding. Test 0.5/2/5/10-year proxies and±100/300/500bp; these do not prove a safe2-year ceiling.

Proposed limit concept: for each joint stress s, allowed rate exposure must leave nonnegative conditional economic buffer **and** enough deadline liquidity, after unrelated costs and liability changes. A preliminary bound `sum(MV*Dmod)*dy <= explicit loss budget` can screen small shocks only; use full cash-flow repricing for final limits. WP1E/Phase2 must establish the budget and probability/tail tolerances; no universally tolerable duration is determined here.

## Horizon test
For every cutoff h and joint scenario s, `available_USD(h,s) >= due_outflows(h,s)+operating_cash(h,s)+explicit_uncertainty_margin(h,s)`. Test intraday/24h/72h/7d/30d, weekends/holidays, market closures and settlement delays. Only one use of each asset is allowed: sale proceeds and maturity proceeds are mutually exclusive. No new issuance, counterparty renewal, borrowed reserves or lender-of-last-resort funding in the base stress. Haircuts cannot create liquidity when access is zero.

Minimum liquidity is a function of outflow commitments, not a chosen universal reserve percentage. With immediately usable20, demand30 and operating2, gap=-12 even if total assets120. If60 of bill sale proceeds arrive in24h, they do not meet a23h deadline. WP1F must supply actual terms; until then publish multiple outflow branches, including100% eligible demand, and never promise an inferred deadline.

## Sequential run counterexample
Initial cash20+securities100, gross face100. Demand80 with20% sale discount requires selling75 marked securities, generates60 cash, destroys15 value, pays80 and leaves25 assets against20 remaining face: buffer5, not20. Demand100 would consume100 marked securities and leave0 assets/0 face; demand130 leaves30 unpaid in the illustrative larger-liability branch. An unpaid balance is still owed. Repeated partial sales can make remaining holders worse off; no seniority/fee/gate mechanism is adopted to cure it.

Report a cumulative-demand curve across0/20/40/60/80/100% and sales discounts0/2/10/20/25/30%, including cash inaccessible and deadline-limited sales. The model is a one-shot aggregate accounting illustration, not a behavioral bank-run equilibrium or live order-book model. Timing, acceptance access and adverse selection stay WP1F/Phase2 dependencies.

## Review correction and expanded run test
The first20%-discount example proves absolute loss of buffer, **not by itself deterioration of remaining-holder coverage**:25assets/20face=1.25, greater than initial1.20. At25%discount demand80 leaves20assets/20face; at30% leaves100/7assets against20face, coverage5/7≈.714286. The expanded216-case curve varies starting assets102/120, cash10/20/40, discounts0/2/10/20/25/30%, and demand0–100%. Its loss/remaining-liability columns prevent mistaking shrinking absolute capital for worsening proportional coverage. These examples establish possibility, not a universal early-exit incentive.

Joint640-case diagnostics first apply the supplied cash/bill/TIPS mark-return factors, recognize operating expense0/2/5/15 USD million, then sell assets to meet80% or100% of indexed USD face plus those expenses at incremental2/20%discount. Costs are sensitivity assumptions, not empirically normal fees. Deadline availability remains a distinct test; joint sales assume sale access and do not prove actual execution within a promised deadline. Forty gross portfolio cases exclude these additional costs and cannot support a net-survival claim.

Repo maturity comparison uses0/10/20% reserve share with24/168/720h term versus0/24/72/168/720h horizon. Only contractual receipts actually available by the cutoff count; delayed/defaulted receipts must be moved to the appropriate inaccessible branch. No automatic renewal/closeout funding.

## Final review reconciliation of liquidity channels
Current joint grid tests80% **and100%** demand with operating expense0/2/5/15. Expense is an additional recognized USD obligation included in total requested cash, so expense exceeding initial cash can itself force a sale. The model reports aggregate remaining obligations including unpaid expense; it does not assign priority or decide which particular claimant gets paid.

Repo comparison now holds total assets120 fixed: cash20, bills100 minus substituted repo principal. Bill baseline sale settles at24h with1%incremental cost. At20%repo share and7day maturity,72h available cash95.24 versus119 for bills; at7days119.24. This shows the opportunity cost of displacing liquid bills and possible avoided sale cost, without assuming renewal. Zero-share baseline appears once per horizon;35distinct rows avoid repeating the zero-share baseline.

In the asset snapshot, a declared scenario maturity receipt is used if available by the deadline, otherwise an eligible sale route may be used; the two routes never sum. Maturity receipt amount explicitly reflects scenario default/access, not an automatically guaranteed par amount. This is a snapshot route choice, not a transaction execution plan. Market value and sale/receipt availability stay separate. Remaining unsold assets in a run are reported both at their post-shock mark and at further stressed liquidation value; neither is a legal recovery guarantee.
