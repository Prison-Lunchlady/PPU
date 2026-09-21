# WP1B Benchmark Impairment Policy — Revised Completion Report

> **Current disposition:** Gate 1B revision 0.3 APPROVED WITH CONDITIONS for continued development under [SRC018](../../evidence/gate1b-approval-wp1c-authorization-2026-09-21.md). Earlier pending/revision-required statements below are historical. Q023 remains an OPEN production-activation blocker; no true-up or fallback adopted. Approval is not production certification.

Revision 0.3 • 2026-09-21. **Narrow revision COMPLETE FOR RESUBMISSION. Primary disposition REVISION REQUIRED; Gate 1B AWAITING RENEWED PRIMARY REVIEW / NOT APPROVED. WP1C NOT AUTHORIZED.**

The [policy revision](18-benchmark-impairment-policy.md) compares all three alternatives across all ten dimensions, with signed examples and attempts to falsify each. A deterministic continuous-holder adjustment requires a separate compensation metric, collectible negative claims and observations that may never exist. A precommitted fallback can fail alongside CPI-U or change its monetary concept. Indefinite freezing itself cannot preserve ongoing purchasing power.

Recommendation: temporary carry with explicit impairment status; **do not endorse permanent freeze as a satisfactory structural remedy**. Such a remedy remains an activation-blocking unresolved requirement. The state layer adds confirmed-structural versus persistent-unresolved classification and incident-specific restoration/clearance; no automatic compensation or substitution. It can remain impaired indefinitely: it discloses and constrains the unresolved failure rather than claiming to cure it.

Validation: 159 original + 12 prior independent + 49 new checks = **220 passing checks**. Core arithmetic unchanged; the proposed overlay is [impairment_policy.py](impairment_policy.py). [New results](impairment-validation.json) cover notices, temporary/chronic failure, rolling impairment, prospective holds, recovery, clearance, simultaneous events, stale monitors, history, symmetry and policy counterexamples. Tests assume validated inputs; no live oracle or claims system is implemented.

Records updated: D014 proposed; R025/R026 and Q023/Q024 OPEN; H002 impairment recommendation narrowed. Existing R021/R022/R023 and Q021/Q022 remain OPEN. SRC017 records current authority. No Gate 1A wording change, original-draft ratification or WP1C start. [Reconciliation](../../reviews/gate1b/current-reconciliation.md), [submission](Gate-1B-submission.md), [manifest](../../reviews/gate1b/submission-manifest.json).

Primary must assess whether this explicitly incomplete structural remedy is an acceptable research outcome or needs another bounded revision before Gate 1B approval. Prior text below is historical; policy 18 and this revision control conflicts. No new Claude review or endorsement is claimed.

---

# Earlier WP1B Completion Report — historical revision 0.2

Revision0.2 •2026-09-19 • **COMPLETE FOR REVIEW; Gate1B AWAITING REVIEW / NOT APPROVED.** Phase1 remains IN PROGRESS. WP1C and every later package are NOT AUTHORIZED.

## Result and recommendation

Completed the authorized Target Calculation research and produced a deterministic reference algorithm conditional on authenticated, finalized inputs. Recommend an adapted, precommitted TIPS-style daily path, fixed original vintages, exact rational arithmetic with18-place half-even output, symmetric deflation, endpoint carry for missing observations, prospective recovery and narrowly constrained index review holds. These are proposals, not accepted monetary rules. [Formal specification](01-target-specification.md) and [controlling review clarifications](17-review-clarifications.md).

**Primary decision needed:** indefinite freezing without makeup and human review holds are material qualifications of the promise. Recommend reopening Gate1A's promise wording to make those qualifications explicit if this target design is accepted. The underlying CPI-U selection need not change. Gate1A's existing approval has not been unilaterally revoked, expanded or replaced. Q021 stays OPEN.

The principal challenge remains that daily interpolation restores purchasing power more slowly than monthly/release steps. A common10%shock comparison produces3.909091,5.363636 and6.818182 cumulative shortfall-days over90days for release, monthly and daily shapes respectively. These synthetic calculations establish a tradeoff, not user preference. Daily's smaller per-boundary changes and ordinary reference-index compatibility motivate a conditional recommendation; they do not prove economic superiority.

## Deliverables and evidence

| Requested deliverable group | Completed artifact |
|---|---|
|1 Formal target |[01](01-target-specification.md), [17 clarifications](17-review-clarifications.md) |
|2 Base/reference |[02](02-base-and-reference.md) |
|3 Method comparison |[03](03-method-comparison.md), precommit/react×update-shape and common shock |
|4 TIPS compatibility |[04](04-tips-compatibility.md), actual2025gap and31published daily values |
|5 Publication lag |[05](05-publication-lag.md) |
|6 Revision/finality |[06](06-revisions-and-finality.md) |
|7 Missing/outage |[07](07-missing-and-outage.md),17's chronic impairment latch |
|8 Deflation |[08](08-deflation.md) |
|9 Contingency/successor |[09](09-contingency-hierarchy.md),17's cause/authority rules |
|10 Oracle timing/stale |[10](10-oracle-timing.md),17's interface constraints |
|11 CasesA–L |[11](11-adversarial-scenarios.md), public-interface outputs in model-validation |
|12 Worked examples |[12](12-worked-examples.md), expanded gap grid |
|13 Formal algorithm |[reference model](reference_model.py), [tests](test_reference_model.py), [results](model-validation.json) |
|14 Draft updates |[Separate unratified amendment proposal](14-proposed-constitution-updates.md) |
|15 Canonical records |Updated state,D/R/H/Q/library/package/gates/change log; original roadmap and draft preserved |
|16 Completion |This report |
|17 Gate submission |[Gate1B](Gate-1B-submission.md), manifest and portable ZIP |

Additional: [30question coverage](15-required-question-answers.md), [parameters/assumptions](16-parameter-and-assumption-register.md), [primary sources](sources.md), [review reconciliation](reviewer-reconciliation.md).

## Validation and independent challenge

159 offline checks pass in model-validation.json: all12cases through valid genesis; UTC and cutoff equality; derived correction/rebase holds; named hold clearance; chronic-impairment latch; original-artifact conflict resolution; configured paths and strict decimals; rounding/deflation/rebase;2/3/6missing-observation recovery at0/3/20%annual; all31May2026Treasury reference rows; and normal shape invariants. Official PDF and extracted fixture are preserved. See [package validation](../../archive/wp1b-prior/validation.json) for source/hash/ID/link/coverage checks and [manifest](../../archive/wp1b-prior/submission-manifest.json) for file identities.

Claude Opus5High reviewed the frozen initial packet and objected to genuine implementation/coverage gaps. Twenty recorded findings have accepted, partly accepted or rejected dispositions; code and documents were corrected, and the strongest economic/promise objections are prominent here. Claude did not re-review or endorse the final revision. The operator's tests are independent of the opinion; Brad/primary review retains gate authority.

Scope of evidence: deterministic *research* arithmetic and event scenarios, not a price-measurement reconstruction, live oracle, authenticated production ledger, legal opinion, reserve hedge backtest, solvency model or smart contract. Hashes prove file integrity, not truth of CPI measurement. The offline reference model is expressly within the requested formal algorithm deliverable and is not production implementation or WP2A balance-sheet simulation.

## Records, uncertainties and boundaries

Gate1A recorded APPROVED WITH CONDITIONS; WP1A COMPLETE. All seven standing conditions and Gate0's provenance/tension/boundary conditions persist. D011 accepted only for underlying benchmark; D012 records approval/authority; D013 remains pending target recommendation. Q003 closed only for the bounded benchmark selection; Q004 research complete/pending review; Q021OPEN; Q022 adds lag/freeze acceptability. R023/R024 isolate impaired coverage and evidence-clock finality. Existing stable IDs and unrelated questions preserved.

Unresolved: source authentication, path independence, monitor truth, timestamp/finality assurance, exact live genesis configuration, semantic-change classification, future successor/protected-term compatibility, user tolerance and reserve/claim consequences. No source, roadmap or original24-article draft bytes changed. SRC003 remains authoritative **user-confirmed recovery, never a formal platform export**. The prior approved-package archive and canonical snapshot remain intact.

No reserve mix, capital structure, collateral threshold, AP structure, transaction/liability design, chain, general governance, legal entity or production action was selected. No funds, real capital, contracts or deployments. **STOP AT GATE1B.**

## Current repository submission — 2026-09-21

Reconciled under [SRC016](../../evidence/gate1a-approval-2026-09-21.txt); the exact approved standard is in [Protocol State](../../docs/canonical/01-protocol-state.md). The prior dated research is reused with its limitations and review history; no new Claude review or primary endorsement is claimed. See [current reconciliation and validation](../../reviews/gate1b/current-reconciliation.md). All target mechanics remain proposed; Treasury contingency conflict remains OPEN. No oracle, minting, reserve or governance architecture is approved by the research interface examples.
