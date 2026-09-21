# PPU — Purchasing Power Unit

PPU is a gated research project investigating a programmable monetary unit tied to a defined purchasing-power standard. The name and monetary architecture remain provisional. This repository is the version-controlled source for ongoing PPU documentation and authorized development.

## Current project status

| Control | Status |
|---|---|
| Gate 0 | APPROVED WITH CONDITIONS |
| Phase 0 / WP0A | COMPLETE |
| WP1A — Purchasing-Power Standard | COMPLETE |
| Gate 1A | APPROVED WITH CONDITIONS |
| WP1B — Target Calculation | COMPLETE FOR REVIEW |
| Gate 1B | AWAITING REVIEW / NOT APPROVED |
| WP1C and later packages | NOT AUTHORIZED |

The initial commit preserved the Gate 1A review baseline. Brad subsequently approved Gate 1A with conditions and authorized WP1B only; see [current approval](evidence/gate1a-approval-2026-09-21.txt). Completion of research or repository setup does not approve a gate. No production token, contracts, capital commitments, or technical architecture are authorized here.

## Start here

1. [Protocol State](docs/canonical/01-protocol-state.md)
2. [Decision Register](docs/canonical/02-decision-register.md)
3. [Risk Register](docs/canonical/03-risk-register.md)
4. [Active Hypotheses](docs/canonical/04-active-hypotheses.md)
5. [Unresolved Questions](docs/canonical/05-unresolved-questions.md)
6. [Research Library Index](docs/canonical/06-research-library-index.md)
7. [Development Roadmap v0.1](docs/roadmap/07-development-roadmap.md)
8. [Draft Monetary Constitution / Hypothesis Set](docs/constitution/08-draft-constitution.md)
9. [Work Package Register](docs/canonical/09-work-package-register.md)
10. [Review Gate Register](docs/canonical/10-review-gate-register.md)

## WP1A review

Read the [research report](research/wp1a/01-purchasing-power-standard-research-report.md), [benchmark comparison](research/wp1a/02-comparative-benchmark-matrix.md), and [recommended standard](research/wp1a/06-recommended-standard.md), then the [completion report](reviews/gate1a/WP1A-completion-report.md) and [Gate 1A submission](reviews/gate1a/Gate-1A-submission.md). Those research documents preserve the original submission; the underlying standard is now approved only within the current conditions. Target mechanics remain unapproved.

The [public review package](archive/PPU-WP1A-Gate1A-package-public-copy.zip) preserves the original layout and historical snapshots, with documented privacy redactions. See the [import record](archive/README.md) and [file-level provenance](archive/import-provenance.json). Historical validation reports describe their original submissions; the [repository validation](reviews/repository-validation.json) covers this reorganized import.

## Organization and maintenance

- `docs/`: the ten project-control records and maintenance guide.
- `research/wp1a/`: completed benchmark research and sources.
- `reviews/`: WP0A evidence of review and Gate 1A submission records.
- `evidence/`: source material; preserve provenance and original wording.
- `archive/`: earlier revision snapshots and import history.

Future simulation, protocol, contract and legal directories will be added when useful to an explicitly authorized work package. Their omission creates no design decision.

Before work, check the Gate and Work Package registers. Preserve stable IDs and distinguish facts, hypotheses, recommendations and accepted decisions. Update affected records, evidence and [change log](CHANGELOG.md) together in a reviewed commit. Record Brad's explicit disposition and exact next authorized package before progression. Follow the [maintenance guide](docs/workspace-guide.md), subject to this repository's migration record and current scope.

Gate 0's permanent conditions remain: SRC003 is authoritative user-confirmed recovery, **not a formal platform export**; architectural tensions remain unresolved; authorization is limited to a single work package. The constitution remains draft/hypothesis except for explicitly accepted records. No open-source license has been selected or added.

## Approved standard and current Gate 1B handoff

> PPU v0.1 targets U.S. urban consumer-price-indexed purchasing power using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted (CUUR0000SA0).

No individual cost-of-living or universal global guarantee is implied. C-CPI-U and PCE remain live comparators, user demand is unproven, and the original constitution remains unratified outside explicitly approved decisions.

[Gate 1B submission](research/wp1b/Gate-1B-submission.md) · [Completion report](research/wp1b/WP1B-completion-report.md) · [Current reconciliation](reviews/gate1b/current-reconciliation.md). The daily-path candidate, outage rules and all other target mechanics are proposals only. Treasury contingency conflict stays open. Stop at Gate 1B; WP1C is not authorized.
