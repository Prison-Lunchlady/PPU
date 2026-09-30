# WP2B Completion / Package Review

Date: 2026-09-30
Package: WP2B — Historical Data Environment
Disposition: REVISION REQUIRED — persistence/execution remediation only

## Completed substantive work

WP2B now has:
- a stable long-form data contract;
- a source hierarchy and source registry;
- explicit vintage/revision labels;
- missing-data and no-fabrication rules;
- historical availability boundaries;
- an acquisition-check script for the core public/official source set;
- explicit treatment of licensing-limited alternative data;
- Q033 and Q034 for unresolved data-vintage/licensing issues.

The core source set is CPI-U NSA, Treasury bill and nominal Treasury yields, TIPS real yields, effective federal funds and SOFR. NFCI and alternative-asset histories are recorded as candidate inputs with revision/license constraints rather than silently copied.

## Adversarial findings

1. A single seamless 1970s-to-present reserve backtest would contain hidden counterfactual assumptions because TIPS real-yield observations and SOFR do not exist in early stress eras.
2. Current published CPI history is not sufficient evidence of the exact first-release vintages required by WP1B. Q033 remains open.
3. NFCI is revision-sensitive, so today's historical series can introduce hindsight into a supposedly contemporaneous stress test.
4. Yield observations are not total-return observations. WP2C needs explicit duration/pricing/roll mechanics before reserve P&L can be claimed.
5. Gold/equity/Bitcoin/commodity/energy histories may have third-party redistribution constraints. Q034 is open.
6. Data convenience must not determine reserve suitability.

## Persistence limitation

The GitHub connector permits low-level Git-object creation but the normal contents write path remains blocked. The current environment also cannot directly download the full public data files into the local runtime. A short source-acquisition checker was created as a Git blob, but the complete normalized historical panel has not yet been generated and committed. WP2B therefore cannot honestly be marked COMPLETE.

## Review result

WP2B is conceptually ready but fails its required-output condition until a version-controlled observation panel plus retrieval hashes and validation report are actually present and inspectable.

Do not begin WP2C yet.

Next bounded work: WP2B persistence remediation only — attach the current package files to the work branch, execute the data acquisition in an environment with outbound access, commit the generated dataset/provenance/validation, then re-review WP2B. No monetary or reserve redesign is authorized by this remediation.

Claude Opus was not available as a callable connector in this run. No Claude review or endorsement is claimed.
