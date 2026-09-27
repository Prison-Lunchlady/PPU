# WP1G — Governance Constitution Specification
Revision 0.1 — 2026-09-27

## Objective
Define minimized governance for PPU so that human authority can maintain operations and respond to failures without acquiring open-ended monetary-policy power.

## Design conclusion
PPU should use role-based, capability-limited governance with five action classes:
1. G0 protected monetary invariants: not changeable in place; material changes require a new version and voluntary migration.
2. G1 bounded operational parameters: adjustable only inside precommitted ranges through normal governance and a public timelock.
3. G2 service-provider and implementation maintenance: replacements must preserve economic semantics and objective eligibility requirements.
4. G3 emergency risk reduction: immediate authority may only reduce risk, pause expansion, quarantine compromised components or tighten constraints.
5. G4 index contingency: equivalent rebases/successors may follow a special constrained process; materially different benchmark terms require a new version.

No governance-token or PPU-balance voting model is selected. Exact legal body, signer count, voting threshold and institutional composition remain Phase 3/4 questions.

## G0 protected invariants
- no unbacked minting;
- supply expansion only after final eligible reserve settlement and required funded junior capital;
- no retrospective reduction of valid PPU monetary claims;
- no arbitrary wallet rebasing or discretionary confiscation;
- historical target finality after contractual binding;
- no reserve double counting, hidden leverage or unrelated rehypothecation;
- PPU claims economically senior to junior capital and reserve surplus, subject to later legal enforceability;
- no forced migration;
- no opportunistic target/index rewrite;
- no emergency loosening of safety requirements to enable issuance;
- no reserve transfer to administrators or unrelated beneficiaries;
- required reserve/liability/governance transparency may not be disabled.

## Authority domains
Normal Governance; Emergency Risk Authority; Guardian/Canceller; Oracle Operations; Reserve Operations; and a neutral executor where technically possible. No single domain should possess unrestricted proposal, cancellation, emergency and execution powers.

## Normal powers
Within published bounds and timelocks, governance may add/remove qualified APs or custodians, replace service providers, activate/deactivate already approved adapters, adjust bounded fees/minimums/cutoffs/haircuts, update operational calendars, replace same-semantics oracle delivery implementations, approve non-semantic bug fixes and deploy a new protocol version for voluntary adoption.

## Prohibitions
No governance path may mint unbacked PPU, rewrite historical target values, retroactively haircut claims outside a precommitted resolution process, force migration, select a replacement benchmark because it reduces liabilities, treat stale data as fresh to enable issuance, lower risk requirements through emergency authority, raise redemption friction opportunistically to conceal insolvency, erase delayed claims, bypass a timelock via adapter/role/proxy equivalence, subordinate PPU claims, or conceal material conflicts.

## Timelock research baseline
- G1 ordinary bounded changes: 7 days.
- G2 high-impact provider/adapter/peripheral implementation changes: 14 days absent an active incident.
- G4 equivalent-successor index activation: 30-day evidence/review window after objective trigger.
- New-version migration offer: at least 30 days after final terms are published.
- G3 emergency mint pause/oracle quarantine/risk tightening: immediate, initial expiry 72 hours; renewal requires an independent authority domain and public incident record.
- Emergency redemption technical hold: direct technical/security danger only, not illiquidity; initial maximum 24 hours. After 7 continuous days, the system must be in a disclosed recovery/resolution/migration process rather than silent indefinite pause.

These values are hypotheses until Phase 3/4 calibration; the protected ordering is more important than the exact numbers.

## Emergency powers
Emergency authority may stop minting, quarantine a compromised path, tighten haircuts/risk limits, disable a compromised AP/custodian access path and impose a narrowly scoped technical redemption hold when execution would directly create theft, duplication or incorrect discharge. It may not mint, change the target, change benchmark semantics, lower safety requirements, change balances, cancel claims, transfer reserves to administrators, force migration or create permanent rules.

## Oracle replacement
Same-semantics oracle replacement requires identical authoritative source/series identity, vintage and target rules, reproducible output comparison, independent delivery-path testing and notice/timelock. A new benchmark is not oracle maintenance.

## Index contingency
Temporary publication failure follows WP1B freeze/carry. Equivalent rebasing may be mechanically normalized if equivalence is proven. An official successor preserving substantially the same concept may enter G4 after objective trigger and public equivalence analysis. A materially different successor/methodology creates BENCHMARK_IMPAIRED and requires a new version. Q023 remains unresolved.

## Upgrades and migration
Core monetary semantics should be immutable or versioned. Peripheral components may be upgradeable under G2 only. Any upgrade with G0 economic effect is a G0/new-version change regardless of software label. Migration is opt-in; launching a new version does not erase old claims or automatically transfer old reserves.

## Accountability
Privileged actions should publish action class, proposer/authority, affected parameters/code, rationale/evidence, conflicts, execution time, cancellation/renewal history and resulting state. Material conflicts should be disclosed and recused where practical.

## Legal boundary
This is economic/constitutional design, not a legal-classification conclusion. If law later requires account restrictions, Phase 3 must define the scoped mechanism; ordinary governance does not gain a general confiscation power.

## External checks
FSB recommendations support clear governance responsibility/accountability, risk management, recovery/resolution and disclosure as safety principles; they do not classify PPU.
CPMI-IOSCO PFMI governance guidance supports clear lines of responsibility and crisis decision procedures as design context; PPU is not classified here as an FMI.
OpenZeppelin governance/timelock documentation confirms that delayed execution, separated roles and cancellation are established implementation patterns; no Phase 4 library/chain is selected.

## Falsification
H007 should be rejected or materially qualified if later design shows a single ordinary key can change G0 semantics, emergency power can increase monetary risk, adapters/proxies bypass protected rules, migration cannot remain voluntary, index contingency requires broad opportunistic discretion, or legal controls necessarily create incompatible discretionary monetary power.
