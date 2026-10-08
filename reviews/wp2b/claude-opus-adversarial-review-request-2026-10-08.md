# Independent WP2B adversarial review — prepared, not executed

Reviewer: Claude Opus through an authenticated Work browser session if available. This is a review **request**, not an actual review or endorsement.

Inputs: canonical Protocol State, Decision Register, Risk Register, Active Hypotheses, Unresolved Questions, Research Library, Draft Monetary Constitution/Hypothesis Set, Work Package Register, Review Gate Register, latest handoff; the branch's WP2B data dictionary, source registry, vintage policy, acquisition script, validation.json, full source-hashes.json and 91-chunk provenance file; coverage-defect-2026-10-01.md; archived ZIP research/wp2b/data/wp2b-verified-artifact-37128007402.zip.

Challenge the implementation adversarially. Seek falsifiers for:
- Partial/truncated official FRED response, date-chunk gaps or overlap, stale last chunk, wrong or revised series, look-ahead and cross-vintage mixing.
- False confidence from start-date/minimum-row/recent-end checks; mis-keying, invalid dates, hidden missing observations, precision/units errors, stale responses that still pass.
- Payload identity: hashes must bind actual raw official response, precise query range, retrieval time, missing markers and transformations. Independently re-hash exact CSV and ZIP.
- CPIAUCNS current published versus required first-release CUUR0000SA0 vintages (Q033); zero forward/backfill; TIPS/SOFR inception; yield versus total-return distinction; source licensing and alternative series (Q034).
- Whether an archived exact ZIP is an acceptable evidence checkpoint while the required standalone CSV tree path is still absent (it does not satisfy this project's stated acceptance condition).
- Material consequences for PPU economic assumptions without silently upgrading H003/H004 or resolving Q023.

Return severity-ranked findings with stable identifiers, reproducible counterexamples/tests, better alternatives, explicit supported/unsupported claims, rejected alternatives and gate recommendation. Independently reproduce important calculations. Require a written disposition and remediation artifact for every substantive finding. WP2B cannot be approved and WP2C cannot start before reconciliation.
