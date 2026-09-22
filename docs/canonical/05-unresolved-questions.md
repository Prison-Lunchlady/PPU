# Unresolved Questions

## Current controlling handoff — SRC019, 2026-09-21
Gate 0, Gate 1A and Gate 1B retain APPROVED WITH CONDITIONS. **Gate 1C: APPROVED WITH CONDITIONS; WP1C revision 0.1 accepted for continued development**, as reported directly by Brad in [SRC019](../../evidence/gate1c-approval-wp1d-authorization.txt). This is not a separately retrieved primary-review transcript. Conditions explicitly provided are preserved; no missing condition is invented or waived.

**WP1D — Reserve Architecture: COMPLETE FOR REVIEW. Gate 1D: AWAITING REVIEW / NOT APPROVED. Next authorized Work Package: NONE. WP1E and all later packages NOT AUTHORIZED.** Earlier dated handoffs below are history where superseded by this explicit disposition. [Gate 1D submission](../../reviews/gate1d/Gate-1D-submission.md).

Q021/Q022/Q023/Q024/Q025 remain OPEN; **Q023 is a production-activation blocker**. Treasury contingency-methodology conflict and institutional dependence remain OPEN. No fallback benchmark or holder true-up adopted. No selected capital instrument, compensation, optimal ratio, mint/redemption/AP design, legal entity/priority, production custodian or blockchain. Draft constitution remains unratified except explicitly approved decisions. WP1D numerical reserves/limits remain hypotheses pending review and calibration.


Version 0.1 • Recorded 2026-09-19 America/Chicago

Entries OPEN except Q001/Q019 CLOSED and Q020 NO LONGER APPLICABLE, as documented below. Q003 is CLOSED for the narrow v0.1 benchmark selection by Gate1A; Q021 remains OPEN and target mechanics remain pending Gate1B. Stable IDs do not imply approval. Brad controls authorization; future package owners are unassigned.

| ID | Question / uncertainty | Provenance | Resolution evidence and route |
|---|---|---|---|
| Q-001 | Full remainder of SRC003 recovered? | User-supplied full response, normalized prefix match and 24-article/post-analysis coverage | CLOSED. See reviews/source-recovery-reconciliation.md. Does not approve Gate 0 or ratify draft. |
| Q-002 | Who owns, funds and is compensated for the first-loss layer; can it scale? | D005; Phase 0 central unresolved question | Capital Structure Specification, WP1E; stress validation Phase 2 |
| Q-003 | What standardized purchasing power does PPU promise and which benchmark is defensible? | D003, H001; WP1A report | CLOSED for bounded v0.1 benchmark selection, D011/D012 and SRC013. No closure of target mechanics, intended-user fit Q021, universal-optimality or future-scope questions |
| Q-004 | What are base date, index, daily interpolation, rounding, stale/discontinued-index and deflation rules? | Draft I–IV; roadmap 1B | Formal Target Calculation Specification, WP1B |
| Q-005 | What exactly is the liability and what claims have seniority? | Draft V, XV; H008 | WP1C plus Phase 3 legal evidence |
| Q-006 | When queued redemptions enter Q, do their tokens leave S, and at what target/time is the obligation fixed? | Article V equation plus prose; L = S × T + Q is operator shorthand, not a source quotation | Explicit mutually exclusive accounting states in WP1C/1F; no double-count assumption |
| Q-007 | What reserve assets, duration, valuation, haircuts, concentration and liquidity limits are defensible? | Draft VI–IX; H003 | WP1D and Phase 2 |
| Q-008 | Is first-loss capital a financing/claim layer, and how are its underlying reserve assets represented without counting twice? | Roadmap WP2A lists first-loss capital among assets; draft VI describes a distinct layer | Clarify accounting convention in WP1C/1E before WP2A implementation |
| Q-009 | Which capital instruments, dilution, withdrawal, recapitalization and insolvency waterfall work? | Phase 0 alternatives; roadmap 1E | WP1E and Phase 3 |
| Q-010 | Who mints/redeems, in what units, fees, settlement windows and form; does arbitrage work in stress? | Draft XII–XIV; H005–006 | WP1F and Phase 2 |
| Q-011 | Which principles are protected; which parameters may change; how are emergency, migration and index-contingency powers bounded? | Recovered XVIII–XXI; H007 | Source recovered; specify later in WP1G |
| Q-012 | What jurisdiction, classification, ownership, segregation, bankruptcy, AML/KYC, tax and accounting structure is feasible? | R007/R012; roadmap Phase 3 | Counsel questions and legal/institutional deliverables, Phase 3 |
| Q-013 | How are off-chain reserves, liabilities, prices, liens and oracle freshness credibly verified? | Draft XV–XVII; R008/R011 | Later oracle, attestation and reconciliation specifications |
| Q-014 | Which blockchain, bridge policy and software design faithfully enforce the monetary requirements? | Initial proposal; roadmap Phase 4 | Deferred until Phase 4; no chain selection in WP0A |
| Q-015 | Can global/24-hour settlement coexist with business-day reserve settlement and limited reserve-layer access? | Initial global goal versus draft IX/XIV | WP1F and Phase 3 operational analysis |
| Q-016 | What exact package definitions and approval criteria apply in Phases 3–8 where the roadmap does not assign package IDs, and to Phases 7–8 without numbered gate headings? | Roadmap structural gap | Define before those phases are authorized; never invent roadmap provisions |
| Q-017 | Where should an off-device/shared canonical copy live if needed? | Local persistence implementation | Explicitly authorized migration/sync choice; current local record remains authoritative here |
| Q-018 | What are the precise boundaries, precedence and actions for provisional collateral modes, including insolvency? | Draft VII ranges share boundaries and several tests can disagree | WP1D/1E/1F and Phase 2; document before implementation |

## Preserved capital example and alternatives
At USD 1 billion liabilities and 120% backing, USD 1.2 billion reserves imply USD 200 million junior capital. Doubling liabilities to USD 2 billion at the same ratio implies USD 2.4 billion reserves and another USD 200 million junior capital beyond backing the new USD 1 billion monetary claims. This illustration is not an approved collateral requirement.

Candidates preserved from the Phase 0 state: permanent protocol equity; retained reserve earnings; separately subscribed junior capital; regulated reserve-company equity; subordinated capital token; combinations; lower required ratios if simulations justify them. No candidate selected.

## Assumptions about the records
A-001: Later Phase 0 status qualifies earlier normative draft language.
A-002: Local maintained files satisfy the persistence implementation portion; automatic remote sync is not assumed.
A-003: Missing source text is unknown, not absent from the original.
A-004: Historical citation tokens are leads, not independently verified evidence.
A-005: Draft thresholds remain illustrative until authorized research and review.

## Additional review-control questions
**Q-019 — Primary architecture-conversation review.** CLOSED 2026-09-19. Brad's [direct Gate 0 approval](../../evidence/gate0-approval-wp1a-authorization.md) explicitly references preceding primary review and supplies the conditional disposition. This resolves the evidence/approval question for Gate 0; no independent primary-review transcript retrieval or extra veto is claimed. Does not close monetary questions or approve Gate 1A.

**Q-020 — Irrecoverable-source disposition.** NO LONGER APPLICABLE after supplied-source recovery; reopen only if provenance fails. Historical contingency: Continue recovery under existing authorization. If SRC003 cannot be recovered, only Brad can explicitly revise preservation scope, accept a permanently documented gap, or defer affected material. None selected; conditional acceptance would not mean complete preservation, and no WP1G work is authorized.

## Detailed unresolved matters recovered from XVIII–XXIV and analysis
- Q004/Q011: objective unusability criteria, successor hierarchy, prolonged unavailability and hedge preservation versus protected target terms.
- Q005/Q009/Q011: Article XIX prohibits ordinary governance retroactively reducing claims, while Article VII contemplates pro-rata insolvency resolution. Distinguish ex ante resolution from discretionary impairment; do not resolve here.
- Q010/Q011/Q015: precise emergency expiry/renewal process, maximum mint/redemption pauses, shorter security-only redemption restriction, and preservation of orderly claims during contract quarantine.
- Q011/Q012/Q014: how voluntary migration, staying in a prior version or redeeming works with continuing reserve/custody obligations; no forced new terms. Governance limits versus legal requirements remain open.
- Q002/Q007/Q009: can retained income/funded junior capital support growth, and is 120% excessive or insufficient? Stress-test alternatives later; 108–112% is not an approved range.
- Q012: narrow-bank analogy is not classification advice; legal status remains unknown.

Q019 closure rests on the later express approval, not the earlier source-confirmation statement.

## WP1A additions and preserved dependencies
**Q-021 — Intended user population and scope fit. OPEN.** Does the bounded U.S. urban consumer-price promise meet intended users' needs, especially globally? WP1A recommends that scope without demand evidence; Brad/primary review assesses fit. Reopen benchmark recommendation if another population or constant-utility goal is required. R005/D011.

Q004/Q011: actual 2025 Treasury contingency exposes observed-data/no-forecast versus same-hedge-convention conflict. Binding vintage, corrections, lag tolerance, missing-data behavior and successor treatment remain WP1B/1G decisions; no automatic Treasury inheritance.
Q013: public published-value verification is distinct from full independent CPI reconstruction; delivery mirrors do not create measurement independence. Later oracle requirements must preserve this boundary; R022.
Q007: no direct hedge for alternatives was established in this research; existence/cost of custom derivatives and matched-portfolio performance remain untested, WP1D/Phase 2. All capital, insolvency, emergency, version-continuity and legal questions remain OPEN.

## WP1B research disposition
**Q-004:** RESEARCH ANSWER COMPLETE / GATE1B REVIEW PENDING. Candidate formula/base/timing/rounding/deflation/outage/revision/successor policy in wp1b/01–15. No target mechanism approved. Actual future genesis date is an activation parameter, not chosen here.
**Q-021 remains OPEN.** Research has not established intended user demand or tolerance for delayed coverage, freezes and prospective recovery. Gate1A explicitly preserves this question.
Q011 remains OPEN: constrained index hold/clearance requirements proposed; substantive successor and voluntary migration versus protected terms not resolved. General governance/emergency/insolvency topics remain for later packages.
Q013/Q014 remain OPEN: authenticated first-publication capture, path independence, truthful monitoring, canonical timestamps/finality and chain outage execution must be proven later. Exact offline arithmetic is not this evidence.
**Q-022 — Lag and prolonged-freeze acceptability. OPEN.** Can intended users and later architecture tolerate the proposed ~2.5-month stylized age, arbitrary outage length, first-vintage error and catch-up exposure? Gate1B assesses the proposed qualification; later WP1D/1F/Phase2 quantify matching/liquidity/transaction implications. If unacceptable, reopen target or Gate1A. Distinct from Q021 population fit, and from mechanical Q004.
All other unrelated questions remain at inherited dispositions. No capital, reserves, liability accounting, APs, emergency redemption, legal classification or software-selection answer is implied.


Gate1B submission explicitly recommends primary review of Gate1A promise wording; Q003's earlier narrow benchmark-selection closure is not reversed by operator opinion. Q004 remains GATE1B REVIEW PENDING and Q021/Q022 remain OPEN. No unrelated question is closed.


## Current approval reconciliation — 2026-09-21

Q003 closes only the bounded underlying benchmark selection. Q004 target mechanics are researched but awaiting Gate 1B; Q004/Q011 Treasury contingency conflict remains explicitly OPEN; Q013 retains its distinct verification and institutional-dependence question. Q021 user demand/fit and Q022 lag/freeze acceptability remain OPEN. No unrelated unresolved question is closed by SRC016.

## Benchmark impairment revision — 2026-09-21
Q004 remains GATE 1B REVISION REVIEW PENDING. Q022 remains OPEN: compensation and permanent-failure acceptability have not been resolved by relabeling a freeze. Q004/Q011 Treasury contingency conflict remains OPEN.

**Q-023 — What pre-agreed economic remedy makes structural benchmark failure acceptable? OPEN; activation blocker.** Compare the policy ranking and scope implications in D014. A threshold is not a remedy. Accepting the narrow research revision does not select settlement, migration, guarantee or liability treatment. Gate 1B primary disposition first; later packages only after explicit authorization.

**Q-024 — Can a deterministic continuous-holder adjustment be both measurable and collectible without hidden transfer options? OPEN.** Missing originals, lot rules, custody, negative collection, normalization H, funding and prior-claim coexistence need explicit acceptance if B is pursued. The comparison does not settle any WP1C liability architecture. Q021 user fit, Q013 authentication and every unrelated question retain their prior status.


## Gate 1B approval and WP1C review disposition
Q004: accepted development elements are bounded by SRC018; production configuration and later dependencies remain OPEN. Q005/Q006: WP1C definitions researched, GATE 1C REVIEW PENDING; legal ranking, fixed/indexed acceptance terms, pricing time, cancellation and physical token/discharge mechanics remain OPEN. Q008 accounting-versus-capital distinction described, capital architecture unresolved.
Q021 OPEN; Q022 OPEN; **Q023 OPEN — production-activation blocker**; Q024 OPEN. Institutional-dependence and Treasury contingency conflict remain OPEN. No unrelated unresolved question closed.

**Q-025 — What proves a single effective claim replacement and final partial/full discharge? OPEN.** Required facts include scoped ownership/obligor perimeter, predecessor invalidation/replacement, accepted terms, authenticated pricing/effective times, unpaid refunds/other claims and reversal treatment. The model assumes these facts; WP1F, Phase 3/4 and any intervening authorized package must establish them. No work in those packages is authorized here.


## Current Gate 1C / WP1D disposition
Q005/Q006 economic definitions accepted for continued development under SRC019; legal priority, effective replacement, fixed/indexed accepted terms, timestamps, cancellation and payment mechanics remain OPEN. Q007 reserve matching researched but not proven; Q008 capital economics unresolved. Q021 OPEN; Q022 OPEN; Q023 OPEN — production-activation blocker; Q024 OPEN; Q025 OPEN. Treasury contingency conflict OPEN. No unrelated question closed.

**Q-026 — Which reserve duration/liquidity/haircut bounds survive joint calibrated shocks and actual outflow terms? OPEN.** WP1D offers candidate measurements and counterexamples, not empirical bounds. Route WP1F/Phase2, capital-budget dependency WP1E.

**Q-027 — What funds persistent net real carry deficits, expenses and run losses without fictitious or discretionary backing? OPEN.** WP1D shows finite-buffer exhaustion; sustainable first-loss funding/instrument/compensation WP1E, performance Phase2.

**Q-028 — What proves enforceable reserve title, disjoint encumbrances/claims and deadline access across custodians? OPEN.** Nominal ownership labels and positive market assets are insufficient. Phase3/later technical verification; concentration/closeout tests Phase2. Do not close Q025 using asset evidence alone.
