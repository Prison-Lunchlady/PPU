# PPU Protocol State
Record revision 0.3 • 2026-09-19 America/Chicago • Primary project state

**Phase:** 1 — Monetary Architecture; Phase 0 COMPLETE  
**Current package:** WP1A — Purchasing-Power Standard  
**Package status:** COMPLETE FOR REVIEW; awaiting Gate 1A  
**WP0A:** COMPLETE  
**Review Gate 0:** APPROVED WITH CONDITIONS  
**Review Gate 1A:** AWAITING REVIEW / NOT APPROVED  
**Authorized scope completed:** WP1A only; next authorized package NONE  
**Next planned package:** WP1B — Target Calculation; NOT AUTHORIZED

Brad's [approval and conditions](../../evidence/gate0-approval-wp1a-authorization.md) close Q019. Permanent conditions: SRC003 is authoritative user-confirmed recovery, not a formal platform export; unresolved architectural tensions remain unresolved; WP1A authorization does not extend to later packages. The approved Gate 0 record is retained in evidence/gate0-approved/ and the prior archive.

## Current architecture and status
PPU is a research hypothesis for a programmable, redeemable monetary unit tied to standardized purchasing power. Working target T_t = B × I_t / I_0, B = USD 1 on a defined base date. Wallet balances preferably do not rebase with inflation. WP1A recommends the narrower U.S. urban consumer-price-indexed promise and CPI-U NSA all-items U.S. City Average underlying benchmark, pending Gate 1A. TIPS-style daily interpolation remains unvalidated and unselected; WP1B is not authorized. See [proposed standard](../../research/wp1a/06-recommended-standard.md).

Candidate reserves: cash, bills, qualifying Treasury repo and short-duration TIPS, supported by distinct first-loss capital. Senior redemption claims, settled collateralized minting and redemption/burning are intended to constrain supply. AP arbitrage is an unvalidated market-price anchor. Alternative assets remain research candidates; no chain is chosen. Global token settlement does not establish global basket coverage or 24/7 off-chain redemption.

## Constitution and preserved decisions
[Draft Constitution / Hypothesis Set](../constitution/08-draft-constitution.md) now contains all Articles I–XXIV. [Full source](../../evidence/PPU_full_recovered_source.txt) also preserves both post-constitution analysis sections. Q-001 is CLOSED on user-provided recovery evidence and prefix/coverage checks; this is not independent retrieval of the original platform export.

D001–D005 retain inherited statuses; D006–D008 are documentation controls; D009 records source acceptance only. [Decision Register](02-decision-register.md). No monetary principle was changed or ratified.

Newly visible draft provisions cover voluntary migration instead of forced new terms; enumerated governance prohibitions; temporary risk-reducing emergency powers; narrowly justified and shorter redemption pauses; objective index contingency; reserve-backed supply elasticity without emissions or arbitrary supply; blockchain neutrality; and unvalidated numerical parameters. Exact wording is in the draft, with [reconciliation](../../reviews/wp0a/source-recovery-reconciliation.md) identifying open tensions.

## Rejected proposals and reasons
All monetary rejections here are inherited **draft-level positions**, not new approvals.
| Proposal | Source reason/limitation |
|---|---|
| Nominal USD 1 floor | Article I: asymmetric guarantee requires funding |
| Core CPI | Article III: preserve basket including food/energy |
| Proprietary v0.1 index; C-CPI-U settlement target; PCE target | Intro/III: methodology/governance/hedge or revision concerns; later D003 keeps comparison open |
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
[H001–H008](04-active-hypotheses.md) preserve stable IDs. H001 has conditional research support for the narrowed promise, not ratification or validated hedge performance. H002–H008 remain unvalidated. Recovered analysis reinforces H004 capital scalability: 1:1 minting dilutes overcollateralization; economic resemblance to a narrow bank with equity is an analogy, not legal classification.
[Questions](05-unresolved-questions.md): capital incentives, benchmark/contingency, liability states, insolvency versus protected claims, emergency limits, version coexistence and enforceable reserves remain unresolved.
[R001–R020](03-risk-register.md) preserved; source gap R016 is closed, while economic/governance/oracle/legal risks remain open. Legal classification, reserve ownership, bankruptcy and redemption enforceability remain Phase 3 questions.

## Roadmap and review handoff
Roadmap v0.1 remains byte-identical. Phase 2 will compare Treasury/TIPS baselines at 105/110/115/120/125/130% collateralization, varying duration/liquidity, before alternatives; no simulation was started. “108–112%” is only an illustrative efficiency possibility from the source, not a selected range.
[WP0A report](../../reviews/wp0a/WP0A-report.md), [coverage](../../reviews/wp0a/handoff-coverage.md), [historical validation](../../reviews/wp0a/validation.json) and prior submission manifest document Gate 0's approved package. Brad's subsequent direct approval records primary review and conditions without claiming a retrieved transcript. No original source or monetary clause is ratified by this process approval.

WP1A research adds explicit measurement-trust, timing and contractual-vintage limits, including actual 2025 Treasury substitution. The no-forecast/protected-index versus hedge-continuity tension remains open for WP1B/1G. No reserve, capital, collateral, mint/redemption, AP, chain, software, legal-entity or governance design decision has been made. Phase-level Gate 1 is NOT REACHED.

Current handoff: [WP1A completion report](../../reviews/gate1a/WP1A-completion-report.md), [Gate 1A submission](../../reviews/gate1a/Gate-1A-submission.md), [review reconciliation](../../reviews/gate1a/reviewer-reconciliation.md). R021/R022 and Q021 record new distinct limitations; existing tensions and monetary questions remain unresolved. Exact series/base identity is documented without selecting target mechanics. Recommendation depends on acceptance of the explicit priority rule, not on preserving the old draft.

