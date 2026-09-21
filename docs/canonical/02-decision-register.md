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

**PPU-D011 — Purchasing-power standard.** Status: UNDERLYING BENCHMARK APPROVED WITH CONDITIONS at Gate 1A. Target mechanics and broader claims are not approved. The following paragraph preserves the research recommendation; the bounded disposition below controls. Question: what does PPU promise and which benchmark fits? Alternatives: CPI-U, C-CPI-U, PCE, TIPS transformation, regional indexes, PPP and private/proprietary indexes. Recommendation: qualified U.S. urban consumer-price-indexed standard using CPI-U NSA all-items U.S. City Average; proprietary controlling index deferred/excluded from v0.1 on present evidence. Rationale: conceptual fit plus public identifiable outputs, manageable vintages and a practical hedge research path. Tradeoffs: imperfect cost-of-living fit, lag, institutional measurement trust, geographic basis and contingent hedge mismatch. Evidence: [WP1A report](../../research/wp1a/01-purchasing-power-standard-research-report.md) and [proposed standard](../../research/wp1a/06-recommended-standard.md). Reconsider if intended population/promise differs, vintage/lag proves unacceptable, or another benchmark shows net benefit. Author: current operator; approval: Brad for underlying benchmark only, SRC013. Affected: D003, H001, Q003/Q004/Q021, R005/R006/R021/R022. Does not supersede draft source or choose target mechanics.

D003 current disposition: comparative research completed; proprietary superiority unsupported. Its recommendation is pending review under D011, not silently accepted. D008's historical source hold is discharged; it does not negate D010's explicit Gate 0 approval.

D011 review amendment: the priority rule is explicit and pending user/primary acceptance: meaningful fit to the proposed population first, then manageable vintages and practical matching over incremental substitution fidelity. This is a project judgment, not established demand. The selected series ID is CUUR0000SA0; its published base 1982–1984=100 does not choose a PPU base date. Claude's findings and operator dispositions are in wp1a/reviewer-reconciliation.md.

## Gate 1A disposition and WP1B recommendation
**PPU-D012 — Gate 1A approval and bounded WP1B authorization.** Date:2026-09-19. Status: ACCEPTED user process decision. Evidence:SRC013, direct instruction; all seven standing conditions preserved in Protocol State and Gate Register. WP1A COMPLETE, Phase1 IN PROGRESS, WP1B authorized only. No operator alternatives override explicit authority.
D011's accepted content is exactly the narrow benchmark promise in SRC013. This supersedes earlier pending-review references to that selection only. D003 comparative research is complete and proprietary superiority unsupported; future regional/global research remains possible. No permanent constitutional exclusivity or target mechanics are ratified. The original source/draft is unchanged.
**PPU-D013 — Adapted target candidate.** Date:2026-09-19. Status: RECOMMENDATION / PENDING GATE1B. Alternatives: release steps, monthly steps, TIPS wholesale, continuous interpolation and forecasts. Recommend monthly precommitted daily path, fixed first vintage, exact arithmetic, carry missing endpoints, prospective recovery, symmetric deflation and constrained index holds. Evidence:wp1b/01–15, source registry and model tests. Tradeoff: additional lag, no purchasing-power coverage during freeze, contingency hedge basis and human semantic authority. Reconsider if lag, outage exposure, security prerequisites or protected-term compatibility prove unacceptable; may reopen D011/Gate1A. Affects H002,Q004/Q011/Q013,R006/R008/R009/R021; no approval implied.


D013 review reconciliation: v0.2 remains RECOMMENDATION/PENDING GATE1B. Twenty independent-review findings reconciled;159checks. Recommend reopening Gate1A promise wording for indefinite tracking suspension/no makeup/human holds if this candidate is accepted. This does not revoke D011, select a different benchmark or ratify mechanics. User-fit Q021 and lag/freeze acceptability Q022 remain open.


## Controlling Gate 1A disposition — 2026-09-21

Gate 1A: **APPROVED WITH CONDITIONS**. WP1A: COMPLETE. Brad's current direct instruction is [SRC016](../../evidence/gate1a-approval-2026-09-21.txt); it controls over earlier wording. This approval records the conditions stated by Brad, without claiming independent retrieval of the primary review transcript.

Approved standard, exactly:

> PPU v0.1 targets U.S. urban consumer-price-indexed purchasing power using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted (CUUR0000SA0).

This is neither each holder's individual cost of living nor universal global purchasing power. It does not establish demonstrated user demand; Q021 remains OPEN.

No target-calculation mechanics are approved: base date, base index value, TIPS Reference CPI timing, publication lag, interpolation, rounding, corrections, missing observations, prolonged outages, deflation treatment and successor-index rules all remain proposals for Gate 1B. Oracle architecture, reserves, collateralization, capital structure, minting, redemption, governance and blockchain selection remain unapproved later-package dependencies.

The 2025 CPI data gap is a mandatory WP1B design input. The Treasury contingency-methodology conflict stays OPEN; possible future TIPS holdings cannot automatically determine PPU fallback. CPI-U institutional dependence and public reconstruction limitations persist. C-CPI-U and PCE are live research comparators, not rejected or failed alternatives. Historical draft rejection language does not control their current research status.

The prior Draft Monetary Constitution / Hypothesis Set remains unratified except for decisions explicitly approved through the roadmap. Gate 0's provenance, unresolved-tension and package-boundary conditions remain binding. Only WP1B was authorized by this instruction; stop at Gate 1B, with no WP1C or later authorization.

## Current approval reconciliation — 2026-09-21

D012 current authority is reaffirmed and bounded by SRC016 on 2026-09-21; the earlier date/evidence are historical. D011 now uses the exact SRC016 wording above. No other target or architectural decision is accepted. D013 remains a recommendation pending Gate 1B. D006 persistence is superseded operationally by the GitHub repository, selected through the infrastructure initialization; the initial commit preserves the prior records.

## PPU-D014 — Benchmark Impairment Policy revision
2026-09-21. Status: RECOMMENDATION / PENDING GATE 1B. Authority: SRC017, Brad's primary-review disposition REVISION REQUIRED. D013 is not withdrawn wholesale; D014 supersedes only its assumption that indefinite freeze/no compensation is a sufficiently defended fallback. [Analysis](../../research/wp1b/18-benchmark-impairment-policy.md) compares A freeze, B signed contingent true-up and C precommitted structural substitution.

Recommend temporary carry plus explicit impairment classification, incident-specific restoration and review clearance. Do not endorse permanent freeze as preserving purchasing power; structural economic remedy is unresolved and blocks activation. No automatic B/C adoption. Reasons: B adds unresolved eligibility, signed collection and missing-observation problems; C can fail with the source or depart from Gate 1A's concept; A itself fails ongoing coverage. Reconsider on credible remedy/entitlement/fallback evidence or a different primary priority ranking. Choosing the least-assumption interim calculation does not prove it best for users. No Gate 1A change, liability-ledger selection, reserve decision or WP1C authorization.

