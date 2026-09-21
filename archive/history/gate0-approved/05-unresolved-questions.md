# Unresolved Questions
Version 0.1 • Recorded 2026-09-19 America/Chicago

Entries OPEN except Q001 CLOSED and Q020 NO LONGER APPLICABLE, as documented below. Q IDs are new indexing identifiers; they do not imply these questions were previously resolved. Brad controls authorization; future package owners are unassigned.

| ID | Question / uncertainty | Provenance | Resolution evidence and route |
|---|---|---|---|
| Q-001 | Full remainder of SRC003 recovered? | User-supplied full response, normalized prefix match and 24-article/post-analysis coverage | CLOSED. See reviews/source-recovery-reconciliation.md. Does not approve Gate 0 or ratify draft. |
| Q-002 | Who owns, funds and is compensated for the first-loss layer; can it scale? | D005; Phase 0 central unresolved question | Capital Structure Specification, WP1E; stress validation Phase 2 |
| Q-003 | What standardized purchasing power does PPU promise and which benchmark is defensible? | D003, H001 | Purchasing-Power Standard Specification, WP1A |
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
**Q-019 — Primary architecture-conversation review.** OPEN. Roadmap names Brad and the primary architecture conversation as reviewers. No separate primary-conversation review evidence has been recorded. Gate record now has a field for it; whether concurrence is required or advisory remains for Brad to clarify at review. No extra veto or approval is inferred.

**Q-020 — Irrecoverable-source disposition.** NO LONGER APPLICABLE after supplied-source recovery; reopen only if provenance fails. Historical contingency: Continue recovery under existing authorization. If SRC003 cannot be recovered, only Brad can explicitly revise preservation scope, accept a permanently documented gap, or defer affected material. None selected; conditional acceptance would not mean complete preservation, and no WP1G work is authorized.

## Detailed unresolved matters recovered from XVIII–XXIV and analysis
- Q004/Q011: objective unusability criteria, successor hierarchy, prolonged unavailability and hedge preservation versus protected target terms.
- Q005/Q009/Q011: Article XIX prohibits ordinary governance retroactively reducing claims, while Article VII contemplates pro-rata insolvency resolution. Distinguish ex ante resolution from discretionary impairment; do not resolve here.
- Q010/Q011/Q015: precise emergency expiry/renewal process, maximum mint/redemption pauses, shorter security-only redemption restriction, and preservation of orderly claims during contract quarantine.
- Q011/Q012/Q014: how voluntary migration, staying in a prior version or redeeming works with continuing reserve/custody obligations; no forced new terms. Governance limits versus legal requirements remain open.
- Q002/Q007/Q009: can retained income/funded junior capital support growth, and is 120% excessive or insufficient? Stress-test alternatives later; 108–112% is not an approved range.
- Q012: narrow-bank analogy is not classification advice; legal status remains unknown.

Q019 remains OPEN: user-reported primary source confirmation does not constitute primary review of this revised Gate 0 package.
