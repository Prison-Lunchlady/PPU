# PPU Monetary Constitution v1.0 Candidate
WP1G candidate — 2026-09-27
Status: research candidate for Phase Gate 1 review; not production law, legal advice or deployed code.

## Article 1 — Purpose
PPU governance exists to maintain a predefined monetary system, not to conduct discretionary monetary policy. Human authority shall be minimized, enumerated, transparent and constrained.

## Article 2 — Versioned monetary terms
Each PPU version shall publish the economic terms that govern its holders. Materially different monetary terms require a new version rather than silent in-place rewriting.

## Article 3 — Protected monetary invariants
No ordinary or emergency governance action may:
1. create unbacked PPU;
2. arbitrarily expand supply;
3. retrospectively reduce valid PPU monetary claims;
4. rewrite historical target values after contractual finality;
5. rebase balances arbitrarily;
6. confiscate balances at governance discretion;
7. divert core reserves to unrelated purposes;
8. permit hidden reserve leverage, double counting or unrelated rehypothecation;
9. subordinate PPU monetary claims to junior-capital or governance claims;
10. force holders into materially different monetary terms;
11. change the purchasing-power formula or benchmark merely to reduce issuer liabilities;
12. use stale or uncertain data to enable additional issuance;
13. grant unlimited emergency authority.

A material change to these invariants requires a separately deployed protocol version and voluntary migration.

## Article 4 — Governance domains
Governance shall separate normal governance, emergency risk authority, guardian/cancellation authority, oracle operations and reserve operations. No single authority should possess unrestricted control over all domains.

## Article 5 — Ordinary governance
Ordinary governance may perform only enumerated maintenance actions inside published bounds, including qualified provider changes, AP/custodian changes, bounded fees/minimums/cutoffs/haircuts, approved adapter changes and same-semantics oracle implementation replacement.

## Article 6 — Governance prohibitions
Ordinary governance may not use a nominally operational change to achieve an economically forbidden result. An adapter, proxy, role, fee, minimum, valuation or provider change that materially changes protected monetary terms is governed by Article 3 regardless of software label.

## Article 7 — Timelock classes
Research baseline:
- ordinary bounded operational changes: minimum 7 days;
- high-impact provider/adapter/peripheral implementation changes: minimum 14 days absent an active incident;
- equivalent-successor index activation: minimum 30-day public evidence window;
- new-version voluntary migration offer: minimum 30 days after final terms are published.

These durations are hypotheses until Phase 3/4 calibration. The hierarchy is protected: core/new-version changes receive the longest notice; routine changes are delayed; emergency risk reduction may be immediate but temporary.

## Article 8 — Emergency principle
Emergency power may reduce risk but shall not create new monetary power.

Emergency authority may stop minting, quarantine compromised oracle/provider/adapter paths, tighten risk limits and impose a narrowly scoped technical redemption safety hold when continued execution would directly risk theft, duplication or incorrect discharge.

Emergency authority may not mint, change the target, lower safety requirements, change balances, cancel valid claims, transfer reserves to administrators, force migration or permanently amend rules.

## Article 9 — Emergency expiry
Emergency actions shall expire automatically unless renewed under a documented process involving an independent authority domain and public incident record.

Research baseline:
- initial mint pause/oracle quarantine/risk tightening: up to 72 hours;
- initial technical redemption safety hold: no more than 24 hours;
- a redemption hold may not become an indefinite substitute for recovery/resolution. After 7 continuous days the system must operate under a disclosed recovery, resolution or migration process.

A liquidity shortage alone does not erase claims.

## Article 10 — Guardian
A guardian may cancel a pending privileged action that is compromised, unconstitutional or incorrectly scheduled. The guardian does not acquire authority to execute a substitute economic action.

## Article 11 — Oracle replacement
Changing the delivery implementation while preserving the exact authoritative series, vintage rules and target semantics may be an ordinary/high-impact governance action after reproducibility testing and timelock.

Changing the economic benchmark is not oracle maintenance.

## Article 12 — Index contingency
Temporary missing data shall follow the approved freeze/carry rules. Ordinary minting remains disabled when required benchmark facts are impaired.

A purely mathematical rebase may be normalized if equivalence is proven.

An official successor may be adopted in place only through a precommitted contingency process if it preserves substantially the same economic concept and the equivalence case is publicly documented.

A materially different successor or methodology change shall place the benchmark in an impaired state and require a new version rather than discretionary substitution.

This Article does not resolve the economic remedy for permanent structural benchmark failure. Q023 remains a launch blocker.

## Article 13 — Upgrades
Core monetary semantics should be immutable or versioned. Peripheral components may be upgradeable only within the constitutional envelope.

No universal administrator shall possess an unrestricted capability to replace the monetary constitution in code.

Any proposed upgrade shall disclose its economic-semantic impact.

## Article 14 — Voluntary migration
Migration to a new version is voluntary. Existing holders may remain, redeem or migrate subject to the old version's continuing ability to operate and any precommitted resolution process.

A new version does not automatically acquire the old version's reserve assets.

Governance may stop new minting in a legacy version when justified, but may not erase legacy liabilities or coerce migration through reserve diversion or retroactive claim changes.

## Article 15 — Service providers and APs
Provider eligibility shall be objective and public. No single AP or provider receives an exclusive monetary franchise. Provider replacement cannot be used to alter target, liability, reserve or seniority semantics.

## Article 16 — Fees and operational parameters
Fees and operational parameters must be published, bounded and formulaic where practicable. They shall not become discretionary monetary-policy tools or devices to conceal insolvency or prevent legitimate redemption.

## Article 17 — Reserve governance
Reserve operators may act only within the approved reserve mandate. They may not change reserve eligibility rules, liability accounting, protected priority or collateral semantics by operational practice.

## Article 18 — Transparency
Privileged actions shall be machine-auditable where technically possible and publicly disclose action class, responsible authority, exact change, evidence, conflicts, timelock, cancellation history, emergency renewal history and resulting protocol state.

## Article 19 — Conflicts of interest
Material conflicts shall be disclosed. A party with a direct conflict should not be the sole discretionary decision-maker over its own appointment, valuation, incident disposition or replacement.

## Article 20 — Resolution boundary
Governance cannot convert an ordinary liquidity problem into claim cancellation. If full performance becomes impossible, the system must use the precommitted resolution architecture rather than ad hoc first-come depletion or retrospective rewriting.

## Article 21 — Legal/compliance boundary
This Constitution does not predetermine legal classification. If applicable law requires address restrictions or other controls, Phase 3 must specify the legally scoped mechanism. Such requirements do not create a general governance right to conduct discretionary confiscation or monetary-policy changes.

## Article 22 — Governance failure
Loss of keys, governance deadlock or authority failure shall fail privileged changes closed. The protocol should continue deterministic monetary functions where safe, while new issuance may be disabled when required governance or verification facts are unavailable.

## Article 23 — No governance-token assumption
This Constitution does not require a governance token, PPU-holder plutocracy or coin-weighted monetary control. Binding governance design shall be selected for competence, accountability, independence and constitutional enforceability.

## Article 24 — Research status
Exact signer composition, quorums, legal entity, timelock durations, emergency-renewal limits, compliance controls and technical enforcement remain subject to Phase 3/4 validation. No provision here authorizes production deployment.
