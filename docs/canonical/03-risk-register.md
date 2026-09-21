# Risk Register
Version 0.1 • Recorded 2026-09-19 America/Chicago

Source: [Phase 0 response](../../evidence/phase0-source.md). Original IDs and severity preserved. Every original risk remains OPEN; probability, quantitative loss and residual severity are UNASSESSED. No mitigation has been validated. Brad is the gate authority; technical/research owners are unassigned until authorization.

## Preserved risks

I would start the register with these as the highest-priority risks:

| ID | Risk | Current severity |
|---|---|---|
| R-001 | Reserve assets fail to grow with inflation-linked PPU liabilities | Critical |
| R-002 | Capital requirements make PPU economically unscalable | Critical |
| R-003 | Redemption run forces reserve losses at unfavorable market prices | Critical |
| R-004 | TIPS duration/real-rate risk causes collateral impairment | High |
| R-005 | Inflation-index methodology fails to represent intended purchasing power | High |
| R-006 | CPI publication lag creates meaningful target mismatch | Medium/High |
| R-007 | Reserve custody or legal structure prevents holders from having enforceable claims | Critical |
| R-008 | Oracle failure or manipulation corrupts mint/redemption calculations | Critical |
| R-009 | Governance gradually acquires central-bank-like discretionary powers | Critical |
| R-010 | Authorized Participants become concentrated or fail during stress | High |
| R-011 | Off-chain reserves cannot be continuously verified with adequate confidence | High |
| R-012 | Regulatory treatment makes proposed reserve/redemption architecture impractical | Critical |
| R-013 | Smart-contract failure compromises liabilities or collateral | Critical |
| R-014 | Cross-chain architecture introduces unacceptable bridge risk | High |
| R-015 | Secondary-market liquidity is insufficient for arbitrage to maintain target proximity | High |

That matches the roadmap's requirement to track economic, reserve, liquidity, oracle, governance, custodial, legal, blockchain, smart-contract, adoption, and operational risks.



## Investigation routing and candidate controls
| ID | Category | Future evidence / candidate control, not implemented | Planned work |
|---|---|---|---|
| R-001 | Economic/reserve | Asset-liability model and adverse inflation paths | 1C–1E, Phase 2 |
| R-002 | Economic/adoption | Junior capital incentive and scalability model | 1E, 2D |
| R-003 | Liquidity | Run, forced-sale and settlement stress model | 1F, 2C, 2F |
| R-004 | Reserve | Duration/real-rate valuation and haircut tests | 1D, Phase 2 |
| R-005 | Economic/index | Benchmark scope and methodology analysis | 1A |
| R-006 | Index/operational | Publication/interpolation timing analysis | 1A–1B |
| R-007 | Custodial/legal | Qualified review of ownership and claim priority | Phase 3 |
| R-008 | Oracle | Staleness/manipulation/fallback threat model | 1B, 1G, Phases 4–5 |
| R-009 | Governance | Enumerated powers, indirect-change and emergency review | 1G, Phases 4–5 |
| R-010 | Adoption/operational | Multi-participant concentration and failure scenarios | 1F, Phase 3 |
| R-011 | Custodial/operational | Assets, liabilities, liens and reconciliation design | 1D, Phases 3–4 |
| R-012 | Legal | Jurisdiction/classification and counsel questions | Phase 3 |
| R-013 | Smart-contract | Threat model and independent security testing | Phases 4–6 |
| R-014 | Blockchain | Chain/bridge selection and failure analysis | Phase 4 |
| R-015 | Adoption/liquidity | Arbitrage cost, access and depth model | 1F, Phase 2 |

## Added infrastructure risks
| ID | Risk | Severity | Status and response |
|---|---|---|---|
| R-016 | Truncated constitution silently treated as complete | High | CLOSED as source-recovery issue; Q001 full file preserved and reconciled; reopen upon source discrepancy |
| R-017 | Local files mistaken for synced/backed-up cloud records | Medium | OPEN residual; explicit README location and portable archive, no sync claim |
| R-018 | Draft wording mistaken for constitutional approval | High | Controlled in documentation; status banner, D007 and gate log; no ratification |
| R-019 | Assistant self-review mistaken for independent Claude review | Medium | Controlled in documentation; reviewer identity and availability disclosed |
| R-020 | Registers diverge or future packages begin automatically | High | Controlled procedurally; common state, change log, stable IDs and explicit approval evidence required |

Infrastructure controls are documentation measures, not validated monetary risk controls. Reopen controlled items when a later edit violates the stated control.

## Severity and reverse navigation
Inherited R001–R015 severity labels are preserved uncalibrated source assessments, not quantitative estimates. R006 Medium/High is an inherited non-atomic value and is not silently normalized.
For new infrastructure risks only: Critical = could permit prohibited irreversible action; High = could invalidate preservation or approval authority; Medium = materially impairs traceability or handoff; Low = localized clarity issue. No severity was retrospectively re-rated.
Operator owns documentation controls; recheck R018 after draft/status edits, R019 after review claims, R020 before every handoff or authorization change.

| Risk | Related existing questions | Related hypotheses |
|---|---|---|
| R-001 | Q005, Q007, Q008 | H003, H006 |
| R-002 | Q002, Q009 | H004 |
| R-003 | Q007, Q010, Q015 | H003, H005 |
| R-004 | Q007 | H001, H003 |
| R-005 | Q003 | H001 |
| R-006 | Q004 | H002 |
| R-007 | Q005, Q012 | H008 |
| R-008 | Q004, Q013 | H002, H006 |
| R-009 | Q011 | H007 |
| R-010 | Q010, Q015 | H005 |
| R-011 | Q005, Q013 | H006, H008 |
| R-012 | Q012 | H008 |
| R-013 | Q014 | H006, H007 |
| R-014 | Q014 | None assigned |
| R-015 | Q010 | H005 |
| R-016 | Q001 | None; source integrity |
| R-017 | Q017 | None; persistence |
| R-018 | Q011 | H007 |
| R-019 | Q019 | None; review provenance |
| R-020 | Q016, Q019 | None; workflow |

Navigate to [questions](05-unresolved-questions.md) and [hypotheses](04-active-hypotheses.md). These links do not establish resolution.


## Recovered-source risk implications
No new risk IDs needed: R002 now explicitly includes dilution of capital ratios by 1:1 issuance; R009 includes in-place rewriting, forced migration, confiscation, emergency renewal and opportunistic index substitution; R007/R012 include protected-claim language versus insolvency resolution (Q005/Q009/Q011); R008 includes stale/discontinued index fallback and quarantined adapters; R003/R010 include security-only redemption pauses and continuity across versions; R004 includes duration/liquidity tradeoffs. All remain OPEN, unvalidated, and retain original severities. R016 closure concerns evidence completeness only.

## WP1A risk amendment — 2026-09-19
Existing R005 now explicitly includes non-U.S. currency/geographic basis, household heterogeneity and confusing index tracking with constant welfare or asset affordability. Existing R006 includes publication, input-age and contractual-reference clocks separately; inherited Medium/High severity unchanged. R004 remains open despite CPI/TIPS linkage. R009 retains index-methodology and external replacement authority exposure. No economic risk is closed by benchmark research.

| ID | Newly distinguished risk | Severity / status | Evidence, response and routing |
|---|---|---|---|
| R-021 | Contractual index-vintage/contingency basis between target and hedge, including actual missing observations | High, qualitative provisional assessment / OPEN | W1A-S09/S11/S12, 2025 missing October CPI. Unlike delivery failure R008, two authentic contractual values can differ. Q004/Q011; WP1B/1D/1G and Phase 2. Specify and test later; no fallback selected. H001/H002/H003. |
| R-022 | Public arithmetic mistaken for independently reproducible underlying measurement | High, qualitative provisional assessment / OPEN | W1A-S03/S15; confidential inputs and estimation. Q013; disclose distinction now, requirements in WP1B/1G and Phase 4. Multiple mirrors do not remove source-institution trust. H001/H007. |

New economic-research severities above are prioritization judgments based on potential promise/matching failure, not calibrated probabilities or an extension of the infrastructure-only scale. Owner: operator for disclosure; later-package research owners unassigned. Reconsider after specified target and matching tests. R018/R020 controls remain active through Gate 1A; R019 is not closed merely because Q019's Gate 0 evidence issue is resolved.
