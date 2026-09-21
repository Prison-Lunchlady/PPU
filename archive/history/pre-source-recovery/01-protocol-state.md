# PPU Protocol State
Version 0.1 • Recorded 2026-09-19 America/Chicago • Primary project state

**Phase:** 0 — Project Infrastructure  
**Current package:** WP0A — Canonical Project Structure  
**Package status:** Deliverables created; preservation verification blocked on Q-001  
**Review Gate 0:** HOLD / not approved  
**Next authorized work:** WP0A source recovery and reconciliation only  
**Next planned package:** WP1A — Purchasing-Power Standard; NOT AUTHORIZED

## Purpose and current architecture
PPU (Purchasing Power Unit, placeholder name) is a research and engineering investigation into an open, programmable monetary unit preserving an explicitly standardized basket's purchasing power. Economic viability, legal enforceability and production feasibility are unproven.

Working target: T_t = B × I_t / I_0, with B = USD 1.00; I_0 is the base-date reference index, I_t the current reference index. A cumulative 18% index increase yields a USD 1.18 target. Preferred balances do not rebase merely with inflation; supply expands by collateralized minting and contracts by redemption/burning. A market price near this target is a hypothesis, not a guarantee.

Working reserve hypothesis: cash, Treasury bills, qualifying short-term Treasury repo and short-duration TIPS; a distinct first-loss capital layer; PPU claims senior to reserve-surplus claims. CPI-U NSA and TIPS-style daily reference interpolation are candidates, not settled choices. Minting requires collateral, liquidity, oracle and settled-reserve checks. Redemption is intended to anchor price through arbitrage. Governance and emergency powers should be narrowly constrained, with emergency actions generally reducing risk.

Bitcoin, gold, equities, commodities, XRP and other RWAs remain research candidates; no reserve weights or blockchain have been selected. Global/24-hour token settlement does not establish global basket coverage or 24-hour off-chain reserve redemption.

## Constitution and decisions
Current constitution: [Draft Constitution / Hypothesis Set v0.1](08-draft-constitution.md); recovered text is incomplete from Article XVIII onward. No monetary principles were amended or ratified in WP0A.

[Decision Register](02-decision-register.md) preserves PPU-D001–D005: research-first purpose; economics-before-software sequencing; custom-index question open; evidence-first alternative-reserve methodology; first-loss structure unresolved. PPU-D006–D008 record documentation controls only.

Rejected organizational alternatives: chat-only state; treating assistant draft wording as approved policy; automatic gate progression; invented missing source text. Monetary alternatives remain candidates unless the source explicitly states otherwise.

## Equations, definitions and evidence status
Operator shorthand for Article V's equation plus prose (S and Q are notation introduced here, not source symbols): L = S × T + Q, with S circulating PPU and Q accepted unsettled redemption obligations. The treatment of queued tokens must be defined to avoid double counting (Q-006).
Draft GCR = gross eligible reserve value / L.
Draft RARV = sum of market value × (1 − haircut) minus senior non-PPU liabilities.
Draft RACR = RARV / L.
If collateralization C = 1.20 and liabilities grow by ΔL, required reserve growth is C × ΔL, including (C − 1) × ΔL of junior capital. This is an illustrative arithmetic relationship, not a funding solution.
All thresholds and calculation details remain provisional; see the draft.

**Simulations, validated datasets, stress-test results, contracts, selected chain and legal opinions:** none produced or validated in WP0A. No real funds, assets or token issuance.

## Open research and risks
[H-001–H-008](04-active-hypotheses.md) all remain unvalidated.
[Questions](05-unresolved-questions.md) cover capital ownership/incentives, index, calculation, liabilities, reserves, access, governance, oracle, legal and technical design.
[Risk Register](03-risk-register.md) preserves all fifteen initial risks. Critical areas include inflation-liability mismatch, capital scalability, runs, enforceable reserve claims, oracles, governance, regulation and contract failure.
Legal classification, jurisdiction, custody, bankruptcy priority, reserve ownership and enforceable redemption are unresolved Phase 3 questions; early dependencies must be recorded without assuming a legal conclusion.

## Gate handoff
All ten records and the unmodified roadmap are available. Self-review identified and dispositioned structural issues; Q-006, Q-008, Q-015 and Q-018 remain deferred and unresolved in the [review](../../../reviews/wp0a/wp0a-structural-review.md). After user sign-in, Claude Opus 5 High completed an independent AI documentation review. Its fourteen findings and reasoned dispositions are in [reconciliation](../../../reviews/wp0a/claude-opus-reconciliation.md). No Claude re-review of the revised files or qualified human review is claimed.

Blocking preservation gap: full earlier constitution ending unavailable through the bounded reader; browser source also requires sign-in. Recover its ending, reconcile all added articles, refresh preservation checks and submit Gate 0 again. Brad has not approved any progression.

## Draft-level rejected proposals and reasons
These preserve historical positions in the unratified [draft](08-draft-constitution.md), not newly accepted monetary decisions. Later Phase 0 open hypotheses continue to qualify them.

| Proposal rejected in draft | Stated reason or limitation | Article |
|---|---|---|
| Automatic USD 1 floor | Asymmetric deflation guarantee requiring separate funding | I |
| Core CPI excluding food/energy | Basket purchasing power includes these costs; objective is not policy forecasting | III |
| Proprietary index controlling v0.1 | Draft selects external CPI-U; later D003 keeps comparative superiority open | III; D003 |
| Alternative/risky assets in required v0.1 core collateral | Initial low-credit-risk, transparency and liquidity criteria; historical returns alone insufficient | VIII; D004 |
| Rehypothecation, unrelated pledges, secret leverage, double counting | Explicit prohibitions protecting available backing; no separate empirical proof supplied | VIII |
| Surplus distribution while experimental | Priority to costs, liquidity, collateral and first-loss capital | X |
| Unbacked issuance or retrospective inflation redefinition | Draft requires explicit recognition/resolution of impairment | XI |
| Minting against unsettled/anticipated collateral or promises | Draft requires confirmed settlement and post-mint backing | XII |

Handoff coverage: [requirement map](../../../reviews/wp0a/handoff-coverage.md). Full-response recovery, primary-conversation review evidence and Brad approval remain outstanding.
