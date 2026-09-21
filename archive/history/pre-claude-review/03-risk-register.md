# Risk Register
Version 0.1 • Recorded 2026-09-19 America/Chicago

Source: [Phase 0 response](../../../evidence/phase0-source.md). Original IDs and severity preserved. Every original risk remains OPEN; probability, quantitative loss and residual severity are UNASSESSED. No mitigation has been validated. Brad is the gate authority; technical/research owners are unassigned until authorization.

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
| R-016 | Truncated constitution silently treated as complete | High | OPEN; Q-001, Gate 0 HOLD; preserve exact partial response |
| R-017 | Local files mistaken for synced/backed-up cloud records | Medium | OPEN residual; explicit README location and portable archive, no sync claim |
| R-018 | Draft wording mistaken for constitutional approval | High | Controlled in documentation; status banner, D007 and gate log; no ratification |
| R-019 | Assistant self-review mistaken for independent Claude review | Medium | Controlled in documentation; reviewer identity and availability disclosed |
| R-020 | Registers diverge or future packages begin automatically | High | Controlled procedurally; common state, change log, stable IDs and explicit approval evidence required |

Infrastructure controls are documentation measures, not validated monetary risk controls. Reopen controlled items when a later edit violates the stated control.

