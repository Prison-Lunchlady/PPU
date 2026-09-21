# PPU Protocol State
Record revision 0.2 • 2026-09-19 America/Chicago • Primary project state

**Phase:** 0 — Project Infrastructure  
**Current package:** WP0A — Canonical Project Structure  
**Package status:** COMPLETE for submission; subject to user review  
**Review Gate 0:** AWAITING REVIEW / NOT APPROVED  
**Next authorized package:** NONE; WP0A review corrections only if requested  
**Next planned package:** WP1A — Purchasing-Power Standard; NOT AUTHORIZED

## Current architecture and status
PPU is a research hypothesis for a programmable, redeemable monetary unit tied to standardized purchasing power. Working target T_t = B × I_t / I_0, B = USD 1 on a defined base date. Wallet balances preferably do not rebase with inflation. CPI-U NSA with TIPS-style lagged daily interpolation is the starting hypothesis, not a validated benchmark selection.

Candidate reserves: cash, bills, qualifying Treasury repo and short-duration TIPS, supported by distinct first-loss capital. Senior redemption claims, settled collateralized minting and redemption/burning are intended to constrain supply. AP arbitrage is an unvalidated market-price anchor. Alternative assets remain research candidates; no chain is chosen. Global token settlement does not establish global basket coverage or 24/7 off-chain redemption.

## Constitution and preserved decisions
[Draft Constitution / Hypothesis Set](08-draft-constitution.md) now contains all Articles I–XXIV. [Full source](../../../evidence/PPU_full_recovered_source.txt) also preserves both post-constitution analysis sections. Q-001 is CLOSED on user-provided recovery evidence and prefix/coverage checks; this is not independent retrieval of the original platform export.

D001–D005 retain inherited statuses; D006–D008 are documentation controls; D009 records source acceptance only. [Decision Register](02-decision-register.md). No monetary principle was changed or ratified.

Newly visible draft provisions cover voluntary migration instead of forced new terms; enumerated governance prohibitions; temporary risk-reducing emergency powers; narrowly justified and shorter redemption pauses; objective index contingency; reserve-backed supply elasticity without emissions or arbitrary supply; blockchain neutrality; and unvalidated numerical parameters. Exact wording is in the draft, with [reconciliation](../../../reviews/wp0a/source-recovery-reconciliation.md) identifying open tensions.

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
[H001–H008](04-active-hypotheses.md) remain unvalidated. Recovered analysis reinforces H004 capital scalability: 1:1 minting dilutes overcollateralization; economic resemblance to a narrow bank with equity is an analogy, not legal classification.
[Questions](05-unresolved-questions.md): capital incentives, benchmark/contingency, liability states, insolvency versus protected claims, emergency limits, version coexistence and enforceable reserves remain unresolved.
[R001–R020](03-risk-register.md) preserved; source gap R016 is closed, while economic/governance/oracle/legal risks remain open. Legal classification, reserve ownership, bankruptcy and redemption enforceability remain Phase 3 questions.

## Roadmap and review handoff
Roadmap v0.1 remains byte-identical. Phase 2 will compare Treasury/TIPS baselines at 105/110/115/120/125/130% collateralization, varying duration/liquidity, before alternatives; no simulation was started. “108–112%” is only an illustrative efficiency possibility from the source, not a selected range.
[WP0A report](WP0A-report.md), [coverage](../../../reviews/wp0a/handoff-coverage.md), [validation](../../../reviews/wp0a/validation.json) and submission manifest support Gate 0 review. Prior Claude review was reconciled; it has not reviewed this recovered-source revision. Primary PPU/user confirmation supplies source provenance, not Gate 0 approval. Brad's approval and primary review of this revised package remain pending.
