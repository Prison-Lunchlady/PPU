# PPU — Purchasing Power Unit
## Development Roadmap v0.1

### Purpose

The objective of the PPU project is to determine whether a purchasing-power-preserving digital monetary unit can be designed that is:

- economically sustainable;
- transparently and verifiably reserved;
- elastic in response to legitimate economic demand;
- resistant to discretionary monetary issuance;
- redeemable for real reserve value;
- programmable and globally transferable;
- resilient under financial stress;
- governed under narrowly constrained rules;
- and technically capable of eventual production deployment.

PPU is a research and engineering project first.

Token issuance is not the initial objective.

The protocol shall advance through defined development phases. Each phase must produce specified deliverables and satisfy a review gate before the project proceeds.

The roadmap may be changed when research, simulation, legal analysis, or engineering demonstrates that the current plan is inadequate.

---

# OPERATING MODEL

Development shall occur through discrete Work Packages.

For each Work Package:

1. Work receives a defined objective.
2. Work performs research, analysis, modeling, coding, or documentation necessary to complete the package.
3. Work may use Claude Opus as an independent reviewer or adversarial critic when useful.
4. Work shall actively search for flaws rather than merely confirm existing assumptions.
5. Work shall document assumptions and uncertainties.
6. Work shall produce the required deliverables.
7. Work shall stop at the Review Gate.
8. Brad and the primary PPU architecture conversation review the results.
9. The next Work Package begins only after approval or revision.

Work may make routine implementation decisions necessary to complete an authorized Work Package.

Work may not independently:

- change constitutionally protected monetary principles;
- launch a production token;
- accept real customer or investor funds;
- commit project capital;
- execute legal agreements;
- represent the project to regulators;
- deploy unaudited production contracts;
- materially change PPU's monetary target;
- or advance beyond a Review Gate without approval.

---

# PHASE 0 — PROJECT INFRASTRUCTURE

## Objective

Create the permanent research, documentation, decision, and engineering environment for PPU.

## Work Package 0A — Canonical Project Structure

Create and maintain:

### PPU Protocol State

A concise authoritative record containing:

- current protocol architecture;
- current Monetary Constitution;
- accepted decisions;
- rejected proposals and reasons;
- unresolved questions;
- active hypotheses;
- equations and definitions;
- simulation results;
- known risks;
- regulatory questions;
- current development phase;
- next authorized Work Package.

This document becomes the primary source of truth.

### Decision Register

Each major protocol decision should include:

- decision ID;
- date;
- question;
- alternatives considered;
- evidence;
- final decision;
- rationale;
- known tradeoffs;
- circumstances that would justify reconsideration.

### Risk Register

Track:

- economic risks;
- reserve risks;
- liquidity risks;
- oracle risks;
- governance risks;
- custodial risks;
- legal risks;
- blockchain risks;
- smart-contract risks;
- adoption risks;
- operational risks.

### Research Library

Maintain source material relating to:

- inflation indexes;
- monetary economics;
- TIPS;
- stablecoins;
- flatcoins;
- reserve management;
- tokenized assets;
- banking;
- payment systems;
- blockchain architecture;
- smart-contract security;
- applicable law and regulation.

## Review Gate 0

Project infrastructure is sufficiently organized that another qualified researcher or engineer could understand the current state of PPU without reading the complete chat history.

---

# PHASE 1 — MONETARY ARCHITECTURE

## Objective

Define precisely what PPU is before designing software around it.

## Work Package 1A — Purchasing-Power Standard

Research and validate:

- CPI-U NSA;
- TIPS Reference CPI methodology;
- CPI publication lag;
- CPI revisions;
- CPI methodology risk;
- C-CPI-U;
- PCE;
- alternative purchasing-power indexes;
- possible future global indexes.

Primary question:

**What exactly does one PPU promise to preserve?**

Required output:

Purchasing-Power Standard Specification.

---

## Work Package 1B — Target Calculation

Define mathematically:

- Base Date;
- Base Reference Index;
- Daily Reference CPI;
- Target Value;
- interpolation rules;
- rounding;
- stale-data handling;
- discontinued-index handling;
- deflation behavior.

Required output:

Formal Target Calculation Specification with worked examples.

---

## Work Package 1C — Liability Model

Define:

- outstanding monetary liability;
- accepted but unsettled redemptions;
- seniority of PPU claims;
- effects of inflation;
- effects of deflation;
- effects of supply expansion and contraction.

Required output:

PPU Liability Model.

---

## Work Package 1D — Reserve Architecture

Determine candidate reserve structure.

Initial baseline:

- cash;
- Treasury bills;
- short-term Treasury repo;
- short-duration TIPS;
- first-loss capital.

Evaluate:

- duration;
- liquidity;
- inflation matching;
- credit exposure;
- real-rate exposure;
- custody;
- concentration;
- basis risk.

Alternative assets such as:

- gold;
- Bitcoin;
- commodities;
- equities;
- tokenized RWAs;

shall initially be treated as research alternatives rather than assumed reserve assets.

Required output:

Reserve Architecture Specification.

---

## Work Package 1E — Capital Structure

Resolve the first-loss-capital problem.

Determine:

- who provides junior capital;
- how junior capital is compensated;
- required capitalization;
- whether capital is permanent or redeemable;
- dilution mechanics;
- recapitalization mechanics;
- insolvency waterfall;
- reserve surplus treatment.

This Work Package is critical.

Required output:

PPU Capital Structure Specification.

---

## Work Package 1F — Mint and Redemption Architecture

Define:

- authorized minting;
- reserve settlement;
- creation price;
- redemption price;
- mint fees;
- redemption fees;
- creation units;
- Authorized Participants;
- secondary-market arbitrage;
- in-kind redemption;
- liquidity management;
- settlement timing.

Required output:

Mint/Redemption Specification.

---

## Work Package 1G — Governance Constitution

Define:

- immutable monetary rules;
- adjustable operational parameters;
- governance powers;
- governance prohibitions;
- emergency powers;
- timelocks;
- upgrade procedures;
- protocol migration;
- oracle replacement;
- index contingency.

Required output:

PPU Monetary Constitution v1.0 candidate.

---

## Review Gate 1

The economic architecture must be internally coherent.

The project must be able to answer clearly:

- What is one PPU?
- What creates its value?
- What legally and economically backs it?
- Who absorbs reserve losses first?
- How does supply expand?
- How does supply contract?
- Why should market price remain near target?
- What happens during inflation?
- What happens during deflation?
- What happens during a bank run?
- What happens during reserve losses?
- What happens during insolvency?
- Who can change the rules?
- Which rules can never be changed?

No simulation assumptions should remain hidden.

---

# PHASE 2 — ECONOMIC MODEL AND SIMULATION

## Objective

Attempt to mathematically break PPU before building production smart contracts.

## Work Package 2A — Balance-Sheet Simulator

Build a reproducible model containing:

### Assets

- cash;
- T-bills;
- repo;
- TIPS;
- first-loss capital;
- optional experimental reserve assets.

### Liabilities

- circulating PPU;
- redemption queue;
- operating liabilities.

### Variables

- inflation;
- real interest rates;
- nominal rates;
- TIPS duration;
- reserve yield;
- redemption demand;
- liquidity;
- supply growth;
- market price deviations;
- collateral ratios.

Required output:

Reproducible PPU balance-sheet simulator.

---

## Work Package 2B — Historical Data Environment

Build clean datasets for relevant historical periods.

Include where possible:

- CPI-U;
- Treasury yields;
- real yields;
- TIPS;
- short-term interest rates;
- Treasury bills;
- market liquidity indicators;
- gold;
- equities;
- Bitcoin;
- commodities;
- energy.

Data provenance must be documented.

Required output:

Version-controlled research dataset and data dictionary.

---

## Work Package 2C — Historical Stress Tests

Test PPU against environments including:

- 1970s inflation;
- Volcker tightening;
- 1987 crash;
- dot-com collapse;
- Global Financial Crisis;
- COVID liquidity crisis;
- 2021–2022 inflation;
- rapid rate increases;
- commodity shocks;
- deflation;
- severe redemption runs.

Required metrics:

- minimum GCR;
- minimum RACR;
- reserve drawdown;
- first-loss-capital drawdown;
- redemption liquidity;
- forced-sale volume;
- mint shutdown frequency;
- recapitalization requirements;
- insolvency events;
- time to recovery.

Required output:

Historical Stress-Test Report.

---

## Work Package 2D — Capital-Ratio Optimization

Test candidate starting collateral ratios such as:

- 105%;
- 110%;
- 115%;
- 120%;
- 125%;
- 130%.

Determine the relationship between:

- safety;
- scalability;
- capital efficiency;
- reserve composition;
- liquidity;
- issuance capacity.

Required output:

Capital Efficiency Study.

---

## Work Package 2E — Reserve Optimization

Begin with Treasury/TIPS baseline.

Only afterward test additions such as:

- gold;
- Bitcoin;
- commodity exposure;
- equities;
- other RWAs.

An asset should be added only if it improves PPU's monetary resilience after accounting for:

- volatility;
- liquidity;
- correlation;
- drawdowns;
- custody;
- legal treatment;
- basis risk.

Required output:

Reserve Optimization Study.

---

## Work Package 2F — Monte Carlo and Adversarial Simulation

Generate extreme but plausible combinations of:

- inflation;
- deflation;
- rate shocks;
- liquidity crises;
- redemption runs;
- reserve losses;
- supply growth;
- oracle interruptions;
- custodian failures.

Search specifically for combinations that cause protocol failure.

Required output:

PPU Failure-Mode Simulation Report.

---

## Review Gate 2

PPU proceeds only if the model indicates a viable range of:

- reserve compositions;
- collateral ratios;
- liquidity requirements;
- capital structures;
- issuance rules;

capable of surviving defined stress conditions.

If PPU cannot satisfy these requirements economically, redesign the protocol before continuing.

---

# PHASE 3 — LEGAL AND INSTITUTIONAL ARCHITECTURE

## Objective

Determine whether the economic model can exist legally and operationally.

Work Packages should investigate:

- U.S. stablecoin law;
- securities law;
- commodities law;
- money-transmission law;
- banking law;
- investment-company issues;
- custody;
- bankruptcy remoteness;
- reserve ownership;
- redemption rights;
- Authorized Participants;
- AML/KYC requirements;
- tax treatment;
- accounting;
- attestations;
- audits.

Required outputs:

- Legal Issues Matrix;
- Institutional Architecture Proposal;
- Required Counsel Questions;
- Regulatory Classification Analysis.

## Review Gate 3

No production architecture proceeds until credible legal paths have been identified.

---

# PHASE 4 — TECHNICAL PROTOCOL DESIGN

## Objective

Translate the economic constitution into software architecture.

Candidate components:

- PPUToken;
- TargetCalculator;
- PurchasingPowerOracle;
- ReservePriceOracle;
- ProofOfReserveAdapter;
- LiabilityAccounting;
- CollateralManager;
- MintBurnController;
- RedemptionManager;
- RiskEngine;
- LiquidityManager;
- EmergencyController;
- GovernanceTimelock.

Research blockchain candidates independently.

Possible candidates include:

- Ethereum;
- Ethereum L2s;
- XRPL EVM;
- XRPL interoperability;
- other suitable networks.

Blockchain selection must follow monetary-system requirements rather than dictate them.

Required outputs:

- Technical Architecture Specification;
- Contract Interface Specification;
- Threat Model;
- Blockchain Selection Report.

## Review Gate 4

The proposed software architecture must faithfully enforce the Monetary Constitution.

---

# PHASE 5 — TESTNET IMPLEMENTATION

## Objective

Build PPU without real reserve assets.

Develop:

- smart contracts;
- simulated reserve tokens;
- CPI oracle;
- reserve oracle;
- minting;
- redemption;
- collateral controls;
- emergency controls;
- dashboards;
- automated tests.

Required testing:

- unit tests;
- integration tests;
- fuzz testing;
- invariant testing;
- oracle failures;
- reserve losses;
- governance attacks;
- liquidity runs;
- reentrancy;
- access-control failure;
- contract-upgrade attacks;
- malformed inputs.

Required output:

Functional PPU testnet prototype.

## Review Gate 5

No real assets may enter the protocol until the implementation survives independent technical review.

---

# PHASE 6 — INDEPENDENT REVIEW

Required external review should include:

- monetary economist;
- reserve/risk specialist;
- digital-asset counsel;
- smart-contract auditors;
- tax/accounting professionals;
- custody professionals.

Claude Opus and other AI systems may supplement adversarial review but do not substitute for qualified independent human review.

Required output:

Independent Review Dossier.

## Review Gate 6

All material findings must be resolved, accepted, or explicitly documented before production planning.

---

# PHASE 7 — CONTROLLED PILOT

Only after previous phases succeed.

Possible pilot characteristics:

- limited issuance;
- limited reserve assets;
- limited Authorized Participants;
- strict issuance caps;
- public reserve reporting;
- independent attestations;
- enhanced monitoring;
- conservative liquidity requirements.

The pilot should test monetary mechanics rather than pursue rapid adoption.

---

# PHASE 8 — PRODUCTION PROTOCOL

Production deployment shall occur only if:

- the monetary architecture survives economic testing;
- the legal structure is viable;
- reserve custody is established;
- redemption rights are enforceable;
- smart contracts are independently audited;
- governance controls are operational;
- reserve transparency is credible;
- appropriate capital exists;
- and the system has survived a controlled pilot.

Production does not end research.

PPU shall remain continuously monitored for:

- monetary failure modes;
- reserve behavior;
- liquidity;
- regulatory changes;
- oracle reliability;
- governance risks;
- technological risks;
- and changes in the economic environment.