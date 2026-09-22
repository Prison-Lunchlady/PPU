# PPU Liability Model — WP1C

**Current disposition (SRC019): WP1C revision0.1 APPROVED WITH CONDITIONS for continued development.** [User authority](../../evidence/gate1c-approval-wp1d-authorization.txt). Original submission text below is historical. No legal/transaction/claim-replacement facts are certified; Q023/Q025 remain OPEN. WP1D-only authority is now complete for review, not approval of any later package.


Revision 0.1, 2026-09-21. **RECOMMENDATION / PENDING GATE 1C.** Gate 1B revision 0.3 is accepted for continued development within SRC018 conditions, not production certification. This model defines monetary-claim accounting; it does not select a legal issuer, accounting standard, reserve, capital instrument or redemption architecture.

## Scope and evidence boundary

One ledger scope is one explicitly identified PPU version/obligor perimeter and one unit of account. USD is the reporting denomination for that version's approved target. The model assumes a complete, authenticated, finalized record of recognized claims. It cannot establish that real-world completeness, legal enforceability, transaction finality or beneficial ownership. Multiple legal entities or versions require separate ledgers and explicit consolidation/elimination rules; never multiply aggregated units by one version's target.

Gate 1A remains exactly: **PPU v0.1 targets U.S. urban consumer-price-indexed purchasing power using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted (CUUR0000SA0).** Gate 1B accepts its specified daily development path, fixed first releases, UTC timing, 18-place binding target, no floor, symmetry and committed-plan finality. Use that binding 18-place decimal as an exact rational input for liability multiplication. This does not select token granularity, payment precision, base date, settlement asset or a production oracle. Display rounding cannot discharge a residual claim.

## Mutually exclusive claim states

| Economic state | Quantity / unit | Measurement | Transition requirement |
|---|---|---|---|
| LIVE | n PPU units, whether user-held, contract-held or lost-key-held | n × T(t) | Remains a liability until an explicit recognized replacement/discharge event |
| REQUESTED, not accepted | r PPU units, economically reserved for a request | r × T(t) | Request alone does not fix a dollar promise or extinguish anything; cancellation restores LIVE |
| ACCEPTED_INDEXED | q PPU units removed from LIVE/REQUESTED | q × T(t) | Binding accepted indexed obligation replaces those units once; no duplicate bearer entitlement |
| ACCEPTED_FIXED | f USD remaining face obligation; original units tracked separately for reconciliation | f, fixed by an explicitly supplied pricing event | Replaces corresponding original units once; not automatically reindexed |
| DISCHARGED | historical evidence of settled/released portions | zero remaining PPU obligation for that portion only | Requires proof of effective discharge, not merely payment initiation, burn, queue removal or an optimistic receipt |

This is an **economic partition**, not a decision to burn, lock, escrow, transfer or invalidate tokens at a particular technical step. If acceptance leaves a independently spendable token claim alive, exclusion from LIVE would undercount: either replacement is not effective or the system has created two obligations. Record the discrepancy and both apparent obligations until resolved; do not repair the books by assuming missing authorization. A future implementation must prove single entitlement before representing the modeled transition.

Pending funding/deposit claims, fees owed to third parties, custodial expenses, borrowed assets and other enforceable obligations are separately inventoried. A received refundable deposit can create an obligation even before PPU exists. Do not call it zero because it is outside token supply. Unknown amount/status is an explicit reconciliation exception; it is not a zero or a selected contingent true-up. No production completeness assertion follows from this model.

## Liability equations and dimensions

For version v at finalized observation time t:

`N_v = LIVE units + REQUESTED units`

`Qidx_v = sum(remaining units of accepted indexed claims)`

`Qfix_v = sum(remaining USD face of accepted fixed claims)`

`L_PPU,v(t) = (N_v + Qidx_v) × T_v(t) + Qfix_v`

`L_PPU,total(t) = sum_v L_PPU,v(t)` after any demonstrable duplicate representation is eliminated **once**. Bridged/wrapped tokens backed by the same underlying entitlement are representations, not automatic new liabilities of this obligor; a separate issuer promise can be a separate entity's liability. Whether either relation actually holds is a verification/legal dependency, not an assumption justified by a bridge label.

Report `L_other_known` separately with its measurement basis and ranking unknowns. A gross known-obligation subtotal `L_PPU + L_other_known` is not necessarily a complete balance sheet or a statutory carrying value. If inventory, price, scope or measurement is incomplete, report `TOTAL_UNDETERMINED` alongside calculable components. Never net reserves, junior contributions or uncertain recoveries against the gross PPU monetary obligation.

The old shorthand `L=S×T+Q` is valid only when S excludes economically replaced accepted claims and Q is **measured currency**, not raw queue units. This revision resolves its accounting ambiguity as a proposed definition; it does not choose the queue's pricing terms. Physical on-chain totalSupply can differ from N and is not by itself the liability quantity.

## Indexed versus fixed accepted obligations — leave architecture open

| Queue contract | Upon effective acceptance of q at time a | Later time t | Main tradeoff |
|---|---|---|---|
| Indexed until discharge | Move q from N to Qidx; aggregate unchanged | q×T(t) remains exposed to inflation and deflation | Holder keeps index exposure during queue delays; amount to discharge is not fixed at acceptance |
| Fixed USD at a | Move q from N to a new face f=q×T(a); aggregate unchanged at a | f stays fixed; no future target remeasurement | Removes later index exposure; acceptance may offer a deflation exit option, depending on actual terms/access |

Neither branch is selected. A fixed face priced at a different time than the effective replacement may create a valuation jump; record the explicit difference, not a fictitious conservation result. The executable model uses equal pricing/replacement time solely for conservation examples. Queue acceptance time, price-fix time, debit time and legal discharge time are distinct fields in the proposed production evidence schema even if a synthetic test makes them equal.

Mixed queues are measurable only when every accepted claim carries explicit contract type and provenance. An unspecified type or price is an error. Historical finality of target plans does not decide which plan prices a redemption. A holder must not choose a historical timestamp after observing inflation; this is a later transaction-rule question. Target predictability can be used to attempt timing trades; it is not proof of riskless profit or universal superiority of daily interpolation.

## Inflation, deflation and quantity changes

With states and fixed faces unchanged, `ΔL = (N+Qidx)×ΔT`. No-floor symmetric deflation reduces indexed obligations; fixed accepted USD faces do not fall. This difference is contractual denomination, not a hidden nominal floor on PPU itself. No balance rebase is needed.

For simultaneous state/price changes between two snapshots, exact decomposition is:

`ΔL = I_old×ΔT + T_new×ΔI + ΔQfix`, with `I=N+Qidx`.

This includes the cross term through T_new and must not be replaced by two old-price products. A fixed-acceptance event at the current target transfers exposure from I to Qfix without changing aggregate face at that instant. A new recognized PPU claim adds n×T; this recognition is **not authorization to mint** and establishes nothing about assets backing it. A transfer between holders changes no aggregate quantity. A tender/request changes availability, not aggregate liability. Effective final discharge reduces remaining obligations by the face discharged. Token burning without discharge is not the same event.

Partial discharge of fixed face d reduces Qfix by d and leaves f−d; partial indexed discharge of q units reduces Qidx by q and has reporting value q×T(discharge). Which payment amount/asset legally satisfies it is not decided. Initiated, failed, reversible, blocked or disputed payments remain outstanding unless effective discharge is established. A final payment reversal that legally revives a claim would require an explicit new recognition/correction event, not rewriting history; this interface is not implemented as a production reversal rule.

Unaccepted request cancellation conserves units and liability. Cancellation of an already fixed accepted obligation is **not defined here**: restoring original units at a changed T changes face value; returning f/T units changes unit count and may face precision constraints. Arbitrarily picking either hides a monetary transfer. Do not execute accepted-claim cancellation without separately authorized conversion/discharge rules. Expiry, confiscation, insolvency haircut and claim forgiveness are likewise not silently assumed.

## Seniority and recoverability

The draft Article V places PPU obligations ahead of surplus claims. Model that only as a **proposed economic ordering for stress analysis**, not a legally perfected priority or ratification of capital architecture. For comparison, treat LIVE, REQUESTED and both accepted PPU forms as one candidate economic class; queue entry does not automatically gain seniority. Whether accepted settlement debts rank differently must be stated as a separate branch and reviewed, never inferred from their fixed-dollar denomination.

Relative to actual taxes, secured creditors, custodians, insolvency costs, set-off rights and third-party claims, legal ranking is UNKNOWN pending later legal/entity work. No pari-passu legal conclusion or selected waterfall is made. Intended seniority does not determine timing/access or guarantee full recovery. `L_PPU` is a contractual reference exposure, not liquidation proceeds, market token value, fair value or recoverable amount. Keep gross obligation and hypothetical recovery separate; no reserve shortfall automatically reduces the stated claim.

Illustrative A=90, PPU face=100: a 10 shortfall is not a 90 liability. If hypothetical junior capital already absorbed losses, counting it again as an extra asset is wrong. This is an accounting warning, not a selected capital layer, ratio or balance-sheet simulation. Reserve eligibility/value and first-loss funding remain WP1D/WP1E and Phase 2 dependencies.

## Benchmark impairment and unknown remedy

Under the accepted temporary carry/finality development rules, an available binding target remains a mathematical input during BENCHMARK_IMPAIRED. Show `L_reference` with `benchmark_status=BENCHMARK_IMPAIRED`; do not call it current CPI purchasing-power coverage, fair settlement value or solvency proof. An impairment flag neither erases obligations nor creates a compensation payable, new index, automatic haircut, redemption stay or governance power.

**Q-023 is OPEN: production-activation blocker.** No structural remedy has been approved; no holder true-up is recognized merely from the contemplated possibility. At the same time, if actual law or an actual promise later creates a claim, absence from this hypothetical model does not make that real claim zero. That is an unresolved legal/completeness dependency, not a legal classification here. Q021/Q022/Q024 and institutional dependence remain OPEN.

If no representable binding target exists, return `INDEXED_COMPONENT_UNDETERMINED`; separately report known fixed faces. Do not substitute zero, a market quote, latest uncommitted CPI or Treasury's replacement. The Treasury contingency-methodology conflict remains OPEN. The structural-remedy issue is not resolved by making a liability column numerically calculable.

## Evidence and invariant checklist

Proposed event records identify version/perimeter, unique claim and event IDs, economic event kind, predecessor claim, original/remaining units or currency, explicit queue denomination, accepted terms identifier, pricing timestamp and immutable target reference, effective finalized time, partial discharge evidence and reconciliation status. Deterministic replay assumes those facts; it does not authenticate them. Duplicate identical events are idempotent; conflicting reuse of an ID is rejected. Out-of-order events require explicit validated ordering, not operator backdating.

Core invariants: every economic unit belongs to exactly one active claim state; replacement removes its predecessor once; no negative quantities/faces; no over-discharge; residual fractions retained; same event cannot discharge twice; request/acceptance conserve face under equal-price examples; no transfer-only supply change; no assets or hypothetical true-ups netted into monetary face. See [model/tests](liability_model.py), [test suite](test_liability_model.py) and [results](liability-validation.json).

## Primary-source anchors and limits

[IFRS Conceptual Framework](https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/conceptual-framework-for-financial-reporting.pdf) provides a conceptual obligation-based lens; [IFRS 9 overview](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/) distinguishes contractual recognition. These are methodological references, not a conclusion that PPU is subject to IFRS or that this nominal exposure is statutory measurement. Legal cancellation/discharge and current electronic-payment recognition details require later professional analysis; no accounting exception is applied by this research model. Governing project sources are the adopted roadmap and unchanged draft Article V, qualified by SRC018 and current registers.

## Recommendation to Gate 1C

Accept/revise/reject the disjoint economic-state ledger, typed accepted-obligation alternatives, dimensional equation, gross-versus-recovery distinction and explicit dependency inventory as the WP1C research artifact. Do not approve a fixed-versus-indexed queue, legal ranking, physical burn timing, payment finality, collateral or capital mechanism by approving this accounting framework. Q005/Q006 remain review-pending for model definitions and open for their legal/transaction terms. No WP1D work begins without Brad's authorization.
