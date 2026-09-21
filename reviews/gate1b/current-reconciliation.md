# Gate 1B current submission reconciliation

2026-09-21. **WP1B COMPLETE FOR REVIEW; Gate 1B AWAITING REVIEW / NOT APPROVED. WP1C and later packages NOT AUTHORIZED.**

## Authority and exact approved standard

Brad's [current direct instruction, SRC016](../../evidence/gate1a-approval-2026-09-21.txt) approves Gate 1A with conditions and authorizes only WP1B. Its canonical wording is:

> PPU v0.1 targets U.S. urban consumer-price-indexed purchasing power using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted (CUUR0000SA0).

This does not promise individual cost-of-living preservation or universal global purchasing power, and it provides no demand evidence. C-CPI-U and PCE remain live research comparators. The original draft is unratified outside separately approved decisions.

## Reused work and new verification

The local September 19 WP1B research packet existed before repository initialization. The initial Git commit deliberately retained the Gate 1A review baseline under the then-current infrastructure instruction. SRC016 now provides current authority to reconcile that earlier WP1B work into the repository. The [reuse provenance](../../archive/wp1b-prior/reuse-provenance.json) identifies original file hashes; private review URLs have been withheld in public copies. Earlier local authority, dates, manifests and reviewer notes remain historical evidence, not substitutes for current authorization or current-byte checks.

The reference algorithm and 159 original checks were rerun on the imported files. Twelve additional checks cover leap/non-leap and 30/31-day paths, intraday constancy, order invariance, future-event noninterference, the 2025 basis calculation and inactive genesis. Both reports are available: [original suite rerun](../../research/wp1b/model-validation.json), [new invariants](../../research/wp1b/revalidation.json). These validate conditional arithmetic; they do not establish truthful source input, user acceptance, production security or solvency.

The earlier Claude review has 20 reconciled findings. Its recorded critique is retained; no new Claude review or endorsement of the revised/current package is claimed. Reusing that critique is appropriate because the proposed mechanics are unchanged. Current reconciliation independently checks authorization, source facts, formulas and scope.

## Mandatory design inputs and open objections

The [BLS shutdown FAQ](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm) was inspected again September 21. It confirms absent October 2025 survey collection, no October CPI release and missing-value indicators. BLS statistical carry-forward imputation in subsequent measurement is distinct from a PPU contractual freeze.

[Treasury's November 26 announcement](https://home.treasury.gov/news/press-releases/sb0324), also rechecked, specifies a 325.604 substitute for its October 2025 obligations and retains it even if BLS later reports the missing index. This is not a measured October headline observation or authority for PPU. The candidate carry rule produces different interim values. **The Treasury contingency-methodology conflict remains OPEN**, linked to R021 and Q004/Q011; possible TIPS holdings do not settle it.

The [BLS FAQ](https://www.bls.gov/cpi/questions-and-answers.htm) confirms rare corrections and limits on disclosed sample information. Deterministic reconstruction of the PPU transform from public, authenticated inputs is different from independently reconstructing BLS's confidential measurement process. Institutional dependence remains R022/Q013. The [calculation methodology](https://www.bls.gov/opub/hom/cpi/calculation.htm) is a statistical-method reference, not an independent measurement feed.

The official [May 2026 Treasury table](https://www.treasurydirect.gov/instit/annceresult/tipscpi/2026/CPI_20260410.pdf) was reopened; the preserved PDF and 31-row fixture support the normal-path comparison. The [Treasury offering rules](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-II/subchapter-A/part-356) remain a source for Treasury conventions, not PPU authority.

The chief adverse conclusion remains: a daily delayed path need not preserve purchasing power as promptly as release or monthly steps. In a prolonged outage or unresolved human review hold, the candidate can stop tracking indefinitely and supplies no retroactive compensation. The proposal therefore asks primary review to explicitly assess a further promise qualification. **No such qualification is approved by Gate 1A or by this report.** Rejection or revision at Gate 1B remains a valid outcome.

## Scope and disposition requested

The formal specification and worked examples satisfy the roadmap's WP1B research output. Base date and base index are defined as future configuration requirements; no live date/value is selected. Timing, lag, interpolation, rounding, correction, absence, outage, deflation and successor behavior are proposals only. Packet, monitoring and health examples express research input constraints, not an approved oracle architecture or authority to mint. The interface cannot determine reserves, collateral, capital, redemption, governance, blockchain or legal structure.

Review the [completion report](../../research/wp1b/WP1B-completion-report.md), [formal specification](../../research/wp1b/01-target-specification.md), [clarifications](../../research/wp1b/17-review-clarifications.md), [parameter register](../../research/wp1b/16-parameter-and-assumption-register.md) and [Gate 1B submission](../../research/wp1b/Gate-1B-submission.md). The current [submission manifest](submission-manifest.json) binds repository bytes; older manifests describe their original packages. The [repository validation](../repository-validation.json) checks current status, navigation, source preservation and privacy patterns.

No Gate 1B approval is inferred. Stop here pending Brad's disposition; no successor work package has begun.
