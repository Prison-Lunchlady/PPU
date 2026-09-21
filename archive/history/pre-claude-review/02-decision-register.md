# Decision Register
Version 0.1 • Recorded 2026-09-19 America/Chicago

Inherited IDs and statuses are preserved below. Source: [Phase 0 response](../../../evidence/phase0-source.md); governing process: [roadmap](07-development-roadmap.md). Historical decision dates were not explicitly stated; this is a recording date, not an invented approval date.

## Inherited entries

**PPU-D001 — Project purpose**

PPU will be treated as a monetary research and engineering project, not as an immediate token-launch project.

**Status:** Accepted.

This follows the roadmap's explicit statement that token issuance is not the initial objective.

---

**PPU-D002 — Development sequencing**

Economic architecture will be designed before blockchain selection and production contract development.

**Status:** Accepted.

The roadmap places monetary architecture and economic simulation before legal architecture, technical design, and testnet implementation.

---

**PPU-D003 — Custom purchasing-power index**

PPU will **not assume** that a proprietary index is superior to CPI.

CPI-U, TIPS methodology, C-CPI-U, PCE, alternatives, and potential future global indexes must first be researched under Work Package 1A.

**Status:** Open hypothesis.

---

**PPU-D004 — Alternative reserve assets**

Gold, Bitcoin, commodities, equities, and tokenized RWAs will not automatically become core reserve assets.

They must demonstrate improved monetary resilience relative to the Treasury/TIPS baseline after volatility, liquidity, correlation, custody, drawdown, legal, and basis-risk effects are included.

**Status:** Accepted research methodology.

---

**PPU-D005 — First-loss capital**

Overcollateralization requires a distinct capital structure and cannot simply be assumed to arise from ordinary PPU minting.

**Status:** Critical unresolved architecture question.

This receives its own Work Package because we need to determine who supplies that capital, how it is compensated, how dilution and recapitalization work, and what happens during insolvency.



## Decision metadata and reconsideration
| ID | Alternatives considered | Evidence and rationale | Tradeoff / reconsideration trigger |
|---|---|---|---|
| PPU-D001 | Research-first versus immediate token launch | Adopted roadmap Purpose; accepted in Phase 0 state | Slower commercialization; reconsider only by explicit project scope approval, never inferred from readiness |
| PPU-D002 | Economics-first versus chain/contract-first | Roadmap phases 1–5; architecture must drive software | Defers platform implementation; documented sequencing defect may justify a proposed roadmap revision |
| PPU-D003 | CPI-U, TIPS method, C-CPI-U, PCE, proprietary and future global indexes | Phase 0 open hypothesis; no comparative validation completed | Benchmark tradeoffs untested; WP1A evidence required before selection |
| PPU-D004 | Treasury/TIPS baseline versus immediate alternative-asset inclusion | Roadmap WP1D and WP2E; resilience must include risk/custody/legal/basis effects | May omit useful diversifiers initially; reconsider with comparative stress evidence |
| PPU-D005 | Protocol equity, retained earnings, subscribed junior capital, reserve-company equity, subordinated token, combinations, lower ratios if justified | Phase 0 capital example and roadmap WP1E; funding cannot be assumed | Economics/ownership unresolved; WP1E and Phase 2 evidence needed; no final structure selected |

For D003 and D005, there is no final decision. Their original placement in the Decision Register must not be interpreted as acceptance.

## WP0A implementation decisions
**PPU-D006 — Durable local records.** Date: 2026-09-19. Status: implemented documentation choice within WP0A. Question: where does canonical state live? Alternatives: chat-only; edits to synced sources; maintained ppu-work folder with preserved evidence. Decision: use this folder and ten indexed Markdown files. Evidence: current user request and parent AGENTS.md read-only restriction. Rationale: handoff and traceability. Tradeoff: no automatic cloud synchronization or off-device backup. Reconsider if an explicitly authorized shared persistence mechanism is selected.

**PPU-D007 — Preserve epistemic status.** Date: 2026-09-19. Status: implemented documentation choice. Alternatives: silently ratify “shall” clauses; drop draft; preserve draft with hypothesis and completeness labels. Decision: preserve text and qualify it using later Phase 0 state. Evidence: latest Phase 0 response explicitly calls it a draft/hypothesis set. Tradeoff: normative wording remains historical and must be read with its status. Reconsider on explicit constitutional approval with complete source evidence.

**PPU-D008 — Fail closed on source completeness and gate authority.** Date: 2026-09-19. Status: implemented documentation choice. Alternatives: reconstruct missing articles; mark complete despite truncation; hold. Decision: hold Gate 0 pending recovery and reconciliation; user approval remains separate. Evidence: reader truncated=true and login-only browser; user's preservation request and gate restriction. Tradeoff: WP0A cannot honestly be declared complete yet. Reconsider after Q-001 is resolved.

## New entry template
ID; date; status; question; alternatives; source/evidence IDs; final decision or explicitly none; rationale; tradeoffs; reconsideration trigger; author; approval evidence when needed; supersedes/superseded-by; affected hypotheses/risks/packages.

