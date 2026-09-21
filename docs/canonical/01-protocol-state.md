# PPU Protocol State
Record revision 0.6 • 2026-09-21 America/Chicago • Primary project state

**Phase:** 1 — Monetary Architecture; Phase 0 COMPLETE  
**Current package:** WP1B — Target Calculation  
**Package status:** WP1B impairment revision COMPLETE FOR REVIEW; Gate 1B REVISION REQUIRED; REVISED SUBMISSION AWAITING PRIMARY REVIEW / NOT APPROVED  
**WP0A:** COMPLETE  
**Review Gate 0:** APPROVED WITH CONDITIONS  
**Review Gate 1A:** APPROVED WITH CONDITIONS; WP1A COMPLETE  
**Authorized scope completed:** WP1B only; next authorized package NONE  
**Next planned package after WP1B:** WP1C — Liability Model; NOT AUTHORIZED

Brad's [approval and conditions](../../evidence/gate0-approval-wp1a-authorization.md) close Q019. Permanent conditions: SRC003 is authoritative user-confirmed recovery, not a formal platform export; unresolved architectural tensions remain unresolved; WP1A authorization does not extend to later packages. The approved Gate 0 record is retained in evidence/gate0-approved/ and the prior archive.

## Current architecture and status
PPU is a research hypothesis for a programmable, redeemable monetary unit tied to standardized purchasing power. Working target T_t = B × I_t / I_0, B = USD 1 on a defined base date. Wallet balances preferably do not rebase with inflation. Gate 1A approves the narrowly defined U.S. benchmark promise and CPI-U NSA all-items U.S. City Average underlying benchmark only. Target mechanics are authorized for WP1B research, not accepted. The current adapted daily interpolation candidate remains pending Gate 1B. See [proposed standard](../../research/wp1a/06-recommended-standard.md).

Candidate reserves: cash, bills, qualifying Treasury repo and short-duration TIPS, supported by distinct first-loss capital. Senior redemption claims, settled collateralized minting and redemption/burning are intended to constrain supply. AP arbitrage is an unvalidated market-price anchor. Alternative assets remain research candidates; no chain is chosen. Global token settlement does not establish global basket coverage or 24/7 off-chain redemption.

## Constitution and preserved decisions
[Draft Constitution / Hypothesis Set](../constitution/08-draft-constitution.md) now contains all Articles I–XXIV. [Full source](../../evidence/PPU_full_recovered_source.txt) also preserves both post-constitution analysis sections. Q-001 is CLOSED on user-provided recovery evidence and prefix/coverage checks; this is not independent retrieval of the original platform export.

D001–D005 retain inherited statuses; D006–D008 are documentation controls; D009 records source acceptance only. [Decision Register](02-decision-register.md). The underlying benchmark is now explicitly approved only as bounded by SRC016; no broader draft ratification is implied.

Newly visible draft provisions cover voluntary migration instead of forced new terms; enumerated governance prohibitions; temporary risk-reducing emergency powers; narrowly justified and shorter redemption pauses; objective index contingency; reserve-backed supply elasticity without emissions or arbitrary supply; blockchain neutrality; and unvalidated numerical parameters. Exact wording is in the draft, with [reconciliation](../../reviews/wp0a/source-recovery-reconciliation.md) identifying open tensions.

## Rejected proposals and reasons
All monetary rejections here are inherited **draft-level positions**, not new approvals.
| Proposal | Source reason/limitation |
|---|---|
| Nominal USD 1 floor | Article I: asymmetric guarantee requires funding |
| Core CPI | Article III: preserve basket including food/energy |
| Historical draft index rejection language | Superseded as current comparator status: C-CPI-U and PCE remain live research comparators under SRC016 |
| Alternative assets automatically in required core reserve | VIII and post-analysis: survival, liquidity and liability coverage before returns |
| Rehypothecation, hidden leverage, double-counting, unrelated use of reserves | VIII/XIX: backing and claim protection |
| Experimental surplus distribution | X: costs/liquidity/collateral/first-loss priorities |
| Unbacked issuance or opportunistic target/index rewrite | XI/XIX/XXI: explicit impairment and objective contingency |
| Unsettled or promised collateral minting | XII: confirmed settlement required |
| Forced migration, confiscation, junior governance claims ahead of PPU | XVIII/XIX: holder terms and seniority protections |
| Unlimited/permanent emergency rule changes; liquidity shortage erasing claims | XX: reduce risk without new monetary power |
| Supply schedules, mining emission, automatic founder allocation or price-only expansion | XXII: elasticity arises from backed mint/redemption |

Organizational alternatives rejected: invented source text, chat-only state, implicit ratification and automatic gate progression.

## Equations, definitions and results
Operator shorthand for Article V's equation plus prose: L = S × T + Q, where S is circulating supply and Q is accepted unsettled redemptions; token/queue exclusion must avoid double counting (Q006).
GCR = gross eligible reserve value / L; RARV = sum of market value × (1 − haircut) minus senior non-PPU liabilities; RACR = RARV / L.
At C = 1.20, reserve growth C × ΔL includes junior capital (C − 1) × ΔL. The recovered dilution example uses L and the added “1” in common million-dollar units; it is illustrative, not a funding solution.
**Simulations, validated datasets, contracts, legal opinions, production capital and deployed tokens: none created in WP0A.**

## Hypotheses, questions and risks
[H001–H008](04-active-hypotheses.md) preserve stable IDs. H001 has conditional research support; the underlying benchmark has explicit bounded Gate 1A approval, not universal optimality or validated hedge performance. H002–H008 remain unvalidated. Recovered analysis reinforces H004 capital scalability: 1:1 minting dilutes overcollateralization; economic resemblance to a narrow bank with equity is an analogy, not legal classification.
[Questions](05-unresolved-questions.md): capital incentives, benchmark/contingency, liability states, insolvency versus protected claims, emergency limits, version coexistence and enforceable reserves remain unresolved.
[R001–R020](03-risk-register.md) preserved; source gap R016 is closed, while economic/governance/oracle/legal risks remain open. Legal classification, reserve ownership, bankruptcy and redemption enforceability remain Phase 3 questions.

## Roadmap and review handoff
Roadmap v0.1 remains byte-identical. Phase 2 will compare Treasury/TIPS baselines at 105/110/115/120/125/130% collateralization, varying duration/liquidity, before alternatives; no simulation was started. “108–112%” is only an illustrative efficiency possibility from the source, not a selected range.
[WP0A report](../../reviews/wp0a/WP0A-report.md), [coverage](../../reviews/wp0a/handoff-coverage.md), [historical validation](../../reviews/wp0a/validation.json) and prior submission manifest document Gate 0's approved package. Brad's subsequent direct approval records primary review and conditions without claiming a retrieved transcript. No original source or monetary clause is ratified by this process approval.

WP1A research adds explicit measurement-trust, timing and contractual-vintage limits, including actual 2025 Treasury substitution. The no-forecast/protected-index versus hedge-continuity tension remains open for WP1B/1G. No reserve, capital, collateral, mint/redemption, AP, chain, software, legal-entity or governance design decision has been made. Phase-level Gate 1 is NOT REACHED.

Historical WP1A handoff: [WP1A completion report](../../reviews/gate1a/WP1A-completion-report.md), [Gate 1A submission](../../reviews/gate1a/Gate-1A-submission.md), [review reconciliation](../../reviews/gate1a/reviewer-reconciliation.md). R021/R022 and Q021 record new distinct limitations; existing tensions and monetary questions remain unresolved. Exact series/base identity is documented without selecting target mechanics. Recommendation depends on acceptance of the explicit priority rule, not on preserving the old draft.


## Gate 1A approval and WP1B control
Earlier local authorization is retained as SRC013. The current [approval and WP1B authorization](../../evidence/gate1a-approval-2026-09-21.txt) is SRC016 and controls the exact wording below. Preserved conditions include: (1) approved promise is **PPU v0.1 targets U.S. urban consumer-price-indexed purchasing power using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted (CUUR0000SA0).** No individual/global guarantee. (2) U.S. scope is a v0.1 choice; regional/global alternatives are future research. (3) only benchmark approved, no target mechanics. (4) WP1B may recommend reopening Gate1A. (5) externally administered measurement, not trustless/decentralized. (6) Q021 OPEN. (7) selection is not universal optimality.
Gate1A's historical submission and all canonical records before this update are preserved in evidence/gate1a-approved/ and the unchanged WP1A ZIP. Approval evidence is Brad's direct instruction referring to primary review; no independently retrieved review transcript is claimed.
WP1B handoff proposes exact target, base, timing, finality, contingencies, symmetric deflation, oracle requirements and test cases only. Capital, reserve composition, thresholds, APs, liability design, general governance, legal entities, production and WP1C are outside this authorization. Existing insolvency/protected-claims, emergency/redemption, successor/migration and no-forecast/hedge-continuity tensions remain unresolved.


## Prior Gate1B handoff — superseded by SRC017
WP1B COMPLETE FOR REVIEW; Gate1B AWAITING REVIEW / NOT APPROVED. [Completion report](../../research/wp1b/WP1B-completion-report.md), [submission](../../research/wp1b/Gate-1B-submission.md), [target candidate](../../research/wp1b/01-target-specification.md), [review reconciliation](../../research/wp1b/reviewer-reconciliation.md).159offline arithmetic/replay checks and31published Treasury daily values passed; integrity checks in wp1b/validation.json. No production/security/solvency certification.
Recommendation: adapt daily indexing with fixed vintages and explicit fallback. **Recommend primary reopening of Gate1A promise wording** for indefinite tracking suspension, no makeup and narrowly scoped human holds if this candidate is accepted. Benchmark selection remains approved with its existing conditions; no operator amendment has occurred. Q021 and Q022 remain OPEN. WP1C NOT AUTHORIZED; Phase1 IN PROGRESS; Phase Gate1 NOT REACHED.


## Controlling Gate 1A disposition — 2026-09-21

Gate 1A: **APPROVED WITH CONDITIONS**. WP1A: COMPLETE. Brad's current direct instruction is [SRC016](../../evidence/gate1a-approval-2026-09-21.txt); it controls over earlier wording. This approval records the conditions stated by Brad, without claiming independent retrieval of the primary review transcript.

Approved standard, exactly:

> PPU v0.1 targets U.S. urban consumer-price-indexed purchasing power using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted (CUUR0000SA0).

This is neither each holder's individual cost of living nor universal global purchasing power. It does not establish demonstrated user demand; Q021 remains OPEN.

No target-calculation mechanics are approved: base date, base index value, TIPS Reference CPI timing, publication lag, interpolation, rounding, corrections, missing observations, prolonged outages, deflation treatment and successor-index rules all remain proposals for Gate 1B. Oracle architecture, reserves, collateralization, capital structure, minting, redemption, governance and blockchain selection remain unapproved later-package dependencies.

The 2025 CPI data gap is a mandatory WP1B design input. The Treasury contingency-methodology conflict stays OPEN; possible future TIPS holdings cannot automatically determine PPU fallback. CPI-U institutional dependence and public reconstruction limitations persist. C-CPI-U and PCE are live research comparators, not rejected or failed alternatives. Historical draft rejection language does not control their current research status.

The prior Draft Monetary Constitution / Hypothesis Set remains unratified except for decisions explicitly approved through the roadmap. Gate 0's provenance, unresolved-tension and package-boundary conditions remain binding. Only WP1B was authorized by this instruction; stop at Gate 1B, with no WP1C or later authorization.

## Current impairment-policy revision — SRC017

Brad returned Gate 1B as REVISION REQUIRED. The narrowly authorized revision is complete for resubmission, not approval. [Policy comparison and state specification](../../research/wp1b/18-benchmark-impairment-policy.md) evaluates indefinite freeze, contingent continuous-holding true-up and fully precommitted structural fallback across all ten requested dimensions. Temporary carry is recommended conditionally; permanent freeze is not defended as fulfilled purchasing-power preservation. Structural economic remedy remains an activation-blocking unresolved requirement.

`BENCHMARK_IMPAIRED` distinguishes authenticated structural notices from persistent symptoms, latches disclosure and necessary data ineligibility, and never automatically substitutes a benchmark or creates compensation. Original arithmetic, fixed vintages, symmetry, UTC timing and finality remain unchanged. 159 prior checks, 12 prior independent checks and 49 new impairment/counterexample checks pass (220 total). Treasury contingency conflict remains OPEN; C-CPI-U/PCE remain live comparators. Gate 1A wording is unchanged. Stop at Gate 1B; WP1C NOT AUTHORIZED.
