# Scope coverage and validation limits
WP1D revision0.1,2026-09-21. Required deliverables are indexed in the completion report. This file distinguishes claims the package tests from claims it cannot establish.

| Required scope | Evidence | Practical limit |
|---|---|---|
| Eligibility, segmentation, liquidity/inflation sleeves | Research02–03 | Conditional candidates, no asset/production custodian selected |
| Duration, nominal/real rates, rollover, cash drag | Research04–05;24rate sensitivities; closed-form carry exhaustion | Zero-coupon proxy not full coupon TIPS pricing or historical return estimate |
| Liquidity, run, forced sale, fixed/indexed claims | Research04/08;216run and640joint cases | No behavioral equilibrium, order book, AP or redemption terms selected |
| Repo counterparty, maturity, settlement | Research02/03/04/07;35horizon cases; collateral-loss test | No enforceable closeout or membership/access assumed |
| TIPS/Treasury historical stress | Primary S03/S04/S08; Research08 | Historical mechanisms, synthetic magnitudes; pre1997 TIPS analogues counterfactual |
| Valuation, haircut, encumbrance, ownership/segregation | Research06–07; typed paired-claim and exception tests | Flags/IDs assume actual evidence and cannot prove legal rights or completeness |
| Gross liability versus reserves/capital/recovery | Accepted WP1C; Research01/06; named residuals | No statutory classification, priority or first-loss instrument chosen |
| All requested alternatives | Research09;7isolated/560joint counterexamples | No empirical diversification benefit established; research-only status |
| Benchmark versus reserve impairment | Research05/07/08; disclosure-status tests | Q023 OPEN; no true-up/fallback/compensation or restored promise |
| Parameter uncertainty and later dependencies | Research10; D018; Q026–Q028 | WP1E/1F/Phase2/3 not executed or authorized |
| Claude critique at multiple stages | Exact prompts/bundles and stage findings/dispositions | AI opinion, not human/professional audit or Gate authority |
| Current control and provenance | SRC019/provenance, canonical registers, manifest | Direct user approval record, not independently recovered full Gate1C transcript |

Model tests exercise positive/negative amounts, binding-target grid, fractional residuals, extreme inflation/deflation, duplicate asset/claim IDs, stale/missing evidence, exact access cutoffs, explicit impairment labels and algebraic conservation. Snapshot replay tests are not a new event-ingestion protocol. WP1C event/replacement/discharge tests are rerun unchanged; their assumptions remain unproved in real-world custody/transactions.

The result counts include necessary invariants, expected-value counterexamples and structural assertions with different evidentiary strengths. A high count does not establish independent experiments, empirical distributions, solvency, legal enforceability, oracle authenticity or production security. Scenario generation and source verification are separate tasks; source history does not calibrate arbitrary scenario parameters.

The current repository validator checks local document links, import/source preservation, current manifest hashes, Gate boundary strings and privacy/credential patterns. Pattern matching is not an exhaustive secret audit. Final remote verification separately compares committed blob hashes to GitHub; a passing local report alone is not proof of delivery.
