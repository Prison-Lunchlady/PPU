# Decision Register
Version 0.1 • Recorded 2026-09-19 America/Chicago

Inherited IDs and statuses are preserved below. Source: [Phase 0 response](../../evidence/phase0-source.md); governing process: [roadmap](../roadmap/07-development-roadmap.md). Historical decision dates were not explicitly stated; this is a recording date, not an invented approval date.

## Inherited entries

**PPU-D001 — Project purpose**

**Date:** UNKNOWN (inherited).

PPU will be treated as a monetary research and engineering project, not as an immediate token-launch project.

**Status:** Accepted.

This follows the roadmap's explicit statement that token issuance is not the initial objective.

---

**PPU-D002 — Development sequencing**

**Date:** UNKNOWN (inherited).

Economic architecture will be designed before blockchain selection and production contract development.

**Status:** Accepted.

The roadmap places monetary architecture and economic simulation before legal architecture, technical design, and testnet implementation.

---

**PPU-D003 — Custom purchasing-power index**

**Date:** UNKNOWN (inherited).

PPU will **not assume** that a proprietary index is superior to CPI.

CPI-U, TIPS methodology, C-CPI-U, PCE, alternatives, and potential future global indexes must first be researched under Work Package 1A.

**Status:** Open hypothesis.

---

**PPU-D004 — Alternative reserve assets**

**Date:** UNKNOWN (inherited).

Gold, Bitcoin, commodities, equities, and tokenized RWAs will not automatically become core reserve assets.

They must demonstrate improved monetary resilience relative to the Treasury/TIPS baseline after volatility, liquidity, correlation, custody, drawdown, legal, and basis-risk effects are included.

**Status:** Accepted research methodology.

---

**PPU-D005 — First-loss capital**

**Date:** UNKNOWN (inherited).

Overcollateralization requires a distinct capital structure and cannot simply be assumed to arise from ordinary PPU minting.

**Status:** Critical unresolved architecture question.

This receives its own Work Package because we need to determine who supplies that capital, how it is compensated, how dilution and recapitalization work, and what happens during insolvency.



## Decision metadata and reconsideration
| ID | Alternatives considered | Evidence and rationale | Tradeoff / reconsideration trigger |
|---|---|---|---|
| PPU-D001 | Research-first versus immediate token launch | Adopted roadmap Purpose; accepted in Phase 0 state | Slower commercialization; reconsider only by explicit project scope approval, never inferred from readiness |
| PPU-D002 | Economics-first versus chain/contract-first | Roadmap phases 1–5; architecture must drive software | Defers platform implementation; documented sequencing defect may justify a proposed roadmap revision |
| PPU-D003 | CPI-U, TIPS method, C-CPI-U, PCE, proprietary and future global indexes | WP1A comparison now supports a conditional recommendation in D011; no accepted selection | Reopen if scope or contrary evidence changes; Gate 1A disposition pending |
| PPU-D004 | Treasury/TIPS baseline versus immediate alternative-asset inclusion | Roadmap WP1D and WP2E; resilience must include risk/custody/legal/basis effects | May omit useful diversifiers initially; reconsider with comparative stress evidence |
| PPU-D005 | Protocol equity, retained earnings, subscribed junior capital, reserve-company equity, subordinated token, combinations, lower ratios if justified | Phase 0 capital example and roadmap WP1E; funding cannot be assumed | Economics/ownership unresolved; WP1E and Phase 2 evidence needed; no final structure selected |

For D003 and D005, there is no final decision. Their original placement in the Decision Register must not be interpreted as acceptance.

## WP0A implementation decisions
**PPU-D006 — Durable local records.** Date: 2026-09-19. Status: implemented documentation choice within WP0A. Question: where does canonical state live? Alternatives: chat-only; edits to synced sources; maintained ppu-work folder with preserved evidence. Decision: use this folder and ten indexed Markdown files. Evidence: current user request and parent AGENTS.md read-only restriction. Rationale: handoff and traceability. Tradeoff: no automatic cloud synchronization or off-device backup. Reconsider if an explicitly authorized shared persistence mechanism is selected.

**PPU-D007 — Preserve epistemic status.** Date: 2026-09-19. Status: implemented documentation choice. Alternatives: silently ratify “shall” clauses; drop draft; preserve draft with hypothesis and completeness labels. Decision: preserve text and qualify it using later Phase 0 state. Evidence: latest Phase 0 response explicitly calls it a draft/hypothesis set. Tradeoff: normative wording remains historical and must be read with its status. Reconsider on explicit constitutional approval with complete source evidence.

**PPU-D008 — Fail closed on source completeness and gate authority.** Date: 2026-09-19. Status: implemented documentation choice. Alternatives: reconstruct missing articles; mark complete despite truncation; hold. Decision: hold Gate 0 pending recovery and reconciliation; user approval remains separate. Evidence: reader truncated=true and login-only browser; user's preservation request and gate restriction. Tradeoff: WP0A cannot honestly be declared complete yet. Reconsider after Q-001 is resolved.

## New entry template
ID; date; status; question; alternatives; source/evidence IDs; final decision or explicitly none; rationale; tradeoffs; reconsideration trigger; author; approval evidence when needed; supersedes/superseded-by; affected hypotheses/risks/packages.

## PPU-D009 — Acceptance of user-supplied recovered source
Date: 2026-09-19. Status: implemented documentation choice within authorized WP0A. Question: may supplied full text supplement partial SRC003? Alternatives: retain gap; invent ending; accept supplied source after alignment/coverage checks. Decision: supplement SRC003 with byte-preserved full file; retain partial history. Evidence: user source-recovery authorization, file and reviews/source-recovery-reconciliation.md. Rationale: normalized prefix matches and all user-identified sections are present through the stated response ending. Tradeoff: user-supplied recovery, not an independently retrieved original platform export; old opaque citation markers absent in new file. Reconsider on conflicting source evidence. No monetary ratification or gate approval.

D008 history: original hold was appropriate while truncated; recovery under its stated reconsideration trigger closes Q001. D003 remains open despite original CPI language; D002 and adopted roadmap supersede the original suggestion to build a model immediately. D004/D005 retain their original meaning. D009 adds no monetary decision.

## WP1A amendments — 2026-09-19
**PPU-D010 — Gate 0 disposition and bounded authorization.** Status: ACCEPTED user process decision. Evidence: [direct authorization](../../evidence/gate0-approval-wp1a-authorization.md). Brad approved Gate 0 WITH CONDITIONS, declared Phase 0/WP0A COMPLETE and authorized WP1A only. Conditions permanently preserve SRC003 recovery provenance, architectural tensions and boundaries. Q019 CLOSED. No alternative or operator discretion overrides this direct authorization; progression requires a new explicit user decision.

**PPU-D011 — Proposed purchasing-power standard.** Status: RECOMMENDATION / PENDING GATE 1A; no final decision. Question: what does PPU promise and which benchmark fits? Alternatives: CPI-U, C-CPI-U, PCE, TIPS transformation, regional indexes, PPP and private/proprietary indexes. Recommendation: qualified U.S. urban consumer-price-indexed standard using CPI-U NSA all-items U.S. City Average; proprietary controlling index deferred/excluded from v0.1 on present evidence. Rationale: conceptual fit plus public identifiable outputs, manageable vintages and a practical hedge research path. Tradeoffs: imperfect cost-of-living fit, lag, institutional measurement trust, geographic basis and contingent hedge mismatch. Evidence: [WP1A report](../../research/wp1a/01-purchasing-power-standard-research-report.md) and [proposed standard](../../research/wp1a/06-recommended-standard.md). Reconsider if intended population/promise differs, vintage/lag proves unacceptable, or another benchmark shows net benefit. Author: current operator; approval: NONE. Affected: D003, H001, Q003/Q004/Q021, R005/R006/R021/R022. Does not supersede draft source or choose target mechanics.

D003 current disposition: comparative research completed; proprietary superiority unsupported. Its recommendation is pending review under D011, not silently accepted. D008's historical source hold is discharged; it does not negate D010's explicit Gate 0 approval.

D011 review amendment: the priority rule is explicit and pending user/primary acceptance: meaningful fit to the proposed population first, then manageable vintages and practical matching over incremental substitution fidelity. This is a project judgment, not established demand. The selected series ID is CUUR0000SA0; its published base 1982–1984=100 does not choose a PPU base date. Claude's findings and operator dispositions are in wp1a/reviewer-reconciliation.md.
