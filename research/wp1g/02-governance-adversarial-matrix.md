# WP1G — Adversarial Governance Matrix
Revision 0.1 — 2026-09-27

This is a policy-level adversarial matrix, not a smart-contract test suite. Phase 4 must convert these cases into executable authorization/invariant tests.

| Case | Adversarial action | Expected result | Status |
|---|---|---|---|
| G-A01 | Normal governance orders unbacked mint | Denied by G0 | PASS by specification |
| G-A02 | Emergency authority orders unbacked mint | Denied by capability set | PASS |
| G-A03 | Governance changes target formula in place | Denied; new version required | PASS |
| G-A04 | Governance reduces already valid claims retroactively | Denied | PASS |
| G-A05 | Governance forces holders to migrate | Denied | PASS |
| G-A06 | Reserve operator rehypothecates core reserve for unrelated debt | Denied | PASS |
| G-A07 | Emergency authority lowers haircuts to keep minting open | Denied | PASS |
| G-A08 | Emergency authority pauses minting after oracle compromise | Allowed, time-limited | PASS |
| G-A09 | Emergency authority pauses redemption because of ordinary liquidity shortage | Denied; claims remain | PASS |
| G-A10 | Direct contract exploit makes settlement unsafe | Narrow technical redemption hold allowed, time-limited | PASS |
| G-A11 | Oracle implementation replaced but series/vintage semantics change | Reclassified; denied as routine swap | PASS |
| G-A12 | Oracle implementation replaced with same semantics after comparison | Allowed after notice/timelock | PASS |
| G-A13 | CPI is rebased by constant scale only | Mechanical normalization if equivalence proven | PASS |
| G-A14 | Official successor materially changes economic concept | No in-place adoption; new version | PASS |
| G-A15 | Governance chooses lower-liability alternative index | Denied | PASS |
| G-A16 | Guardian cancels compromised pending change | Allowed | PASS |
| G-A17 | Guardian executes its preferred replacement | Denied | PASS |
| G-A18 | New version sweeps old reserves while old claims exist | Denied | PASS |
| G-A19 | Fee is raised within formal cap to make redemption uneconomic in stress | Violates cost-linked/non-opportunistic rule | PASS at constitutional level |
| G-A20 | Timelock admin shortens its own delay instantly | Denied; delay administration must itself be delayed | PASS at design level |
| G-A21 | Emergency flag never expires | Violates automatic-expiry invariant | PASS at specification level |
| G-A22 | Compromised emergency key attempts reserve transfer | Capability absent | PASS |
| G-A23 | Compliance need is used as excuse for arbitrary confiscation | Not authorized; Phase 3 mechanism required | PASS |
| G-A24 | Service-provider replacement indirectly changes liability accounting | Reclassified as G0/new-version change | PASS |

## Counterexamples retained
The architecture does not solve Q023 permanent benchmark-failure remedy, legal enforceability, exact production signer/quorum composition, production timelock durations, smart-contract bypass risk, legacy-version servicing economics, legally compelled account restrictions or governance deadlock after key/institutional failure.

## Execution limitation
The local Python/container execution environment was unavailable during this run, so no executable governance harness was run or falsely reported as passing. These 24 cases are specification-level checks. Phase 4 must implement them as automated authorization/invariant tests.
