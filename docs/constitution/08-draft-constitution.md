# Draft Monetary Constitution / Hypothesis Set v0.1
Record revision 0.2 • 2026-09-19 America/Chicago

**RESEARCH DRAFT / NOT RATIFIED.** Full user-supplied recovered text is preserved in [SRC-003 complete evidence](../../evidence/PPU_full_recovered_source.txt). The original truncated capture remains historical evidence. Recovery closes Q-001; it does not approve the monetary provisions.

All 24 articles are reproduced below, retaining original wording with line endings normalized for this Markdown view. Citation/rendering markers missing from the supplied file remain available in the older capture. Post-constitution analysis is preserved verbatim in the full evidence file and mapped in [source reconciliation](../../reviews/wp0a/source-recovery-reconciliation.md).

The later adopted roadmap and Phase 0 state control sequencing and hypothesis status. In particular, the original recommendation to build a model “next” does not authorize skipping Phase 1. No parameters, blockchain, reserve composition, legal structure or protected rules are newly ratified here.

## Recovered original constitution
# PPU MONETARY CONSTITUTION v0.1

**Status:** Research specification — not production monetary policy  
**Working name:** Purchasing Power Unit (PPU)  
**Version:** 0.1

## PREAMBLE

PPU is intended to function as an open, programmable monetary unit whose nominal redemption target changes in accordance with measured purchasing power rather than remaining permanently fixed to one nominal U.S. dollar.

PPU shall not depend upon discretionary monetary issuance, algorithmic reflexivity, unsecured credit creation, or speculative appreciation for maintenance of its monetary target.

The protocol shall instead rely upon:

- objectively defined purchasing-power measurement;
- verifiable reserve assets;
- senior redemption rights;
- first-loss reserve capital;
- deterministic issuance and redemption rules;
- transparent risk measurement;
- constrained governance;
- limited emergency powers;
- and rules enforced wherever possible by immutable software.

PPU shall be designed primarily as a unit of account, settlement asset, and store of standardized purchasing power. It shall not be designed primarily as an investment or yield-bearing instrument.

---

# ARTICLE I — DEFINITION OF ONE PPU

One PPU represents the nominal U.S.-dollar amount required, according to the protocol's designated purchasing-power index, to represent the same standardized purchasing power as **$1.00 on the PPU Base Date**.

PPU wallet balances shall not rebase merely because the purchasing-power index changes.

Instead, the reference and redemption value of each individual PPU shall change.

If:

Base Target = $1.00

Base Reference Index = I₀

Current Reference Index = Iₜ

then:

**PPU Target Valueₜ = $1.00 × Iₜ / I₀**

Example:

If the relevant index has risen cumulatively by 18% since the Base Date:

PPU Target Value = $1.18.

If the index falls because of genuine measured deflation, the PPU Target Value shall also fall.

There shall be no automatic $1.00 nominal floor.

Adding such a floor would create an asymmetric deflation guarantee and therefore an additional liability that would have to be separately funded.

PPU represents standardized U.S. consumer purchasing power. It does not claim to preserve the individual cost of living of every holder.

---

# ARTICLE II — BASE DATE

The production Base Date shall be the official monetary genesis date of the protocol at 00:00 UTC.

The Base Reference Index shall be the valid Daily Reference CPI applicable to that date.

Regardless of the absolute CPI level on that date:

**1 PPU = $1.000000 reference value at genesis.**

Testnet deployments may use arbitrary historical base dates for simulation.

---

# ARTICLE III — PURCHASING-POWER INDEX

PPU v0.1 shall use:

**U.S. Consumer Price Index for All Urban Consumers (CPI-U)**  
**U.S. City Average**  
**All Items**  
**Not Seasonally Adjusted**

published by the U.S. Bureau of Labor Statistics.

PPU shall not use core CPI.

Food and energy shall remain included because PPU is intended to preserve purchasing power rather than forecast underlying monetary-policy inflation.

PPU v0.1 shall not use an internally created proprietary inflation index.

A proprietary purchasing-power index may be researched independently and compared against CPI-U during Phase 2, but it shall not control PPU v0.1 liabilities.

---

# ARTICLE IV — DAILY TARGET CALCULATION

PPU shall use a daily reference-index methodology based substantially on the methodology used for U.S. Treasury Inflation-Protected Securities.

For a day occurring in calendar month M:

Reference CPI for the first day of month M shall equal CPI-U for the third preceding calendar month.

Reference CPI shall then be linearly interpolated across the month toward the CPI-U value applicable to the first day of the following month.

Conceptually:

**RefCPI(d) = RefCPI(M) + ((d − 1) / D) × [RefCPI(M+1) − RefCPI(M)]**

where:

d = calendar day within the month  
D = number of days within the month

The resulting PPU target shall therefore change gradually each day.

This design intentionally accepts an index-publication lag in exchange for:

deterministic calculation,

smooth target changes,

absence of inflation forecasting,

and substantially improved liability matching with TIPS.

The PurchasingPowerOracle shall never forecast future inflation.

---

# ARTICLE V — PPU LIABILITIES

Total PPU monetary liabilities shall be calculated as:

**L = Circulating PPU Supply × Current PPU Target Value**

plus any PPU redemption obligations already accepted but not yet settled.

PPU liabilities shall be senior to claims on reserve surplus.

---

# ARTICLE VI — RESERVE STRUCTURE

The PPU reserve shall consist of two economically distinct layers.

### Senior Reserve

Assets supporting redemption of outstanding PPU.

### First-Loss Capital

Assets subordinate to PPU claims that absorb reserve losses before PPU becomes impaired.

This separation is necessary because overcollateralization cannot be created merely by charging ordinary PPU buyers more than the monetary unit is worth.

If reserve collateralization is C and liabilities increase by ΔL, maintaining collateralization C requires reserve assets to increase by:

**C × ΔL**

Therefore, at 120% collateralization, every $1.00 of new PPU liability ultimately requires:

$1.00 of senior reserve assets

plus

$0.20 of first-loss capital.

PPU issuance shall therefore be constrained not merely by demand but by available reserve capital.

No protocol mechanism shall conceal this capital requirement.

---

# ARTICLE VII — COLLATERALIZATION

PPU v0.1 shall initially model a:

**120% normal gross collateralization target**

together with a separate risk-adjusted collateral test.

Gross Collateral Ratio:

**GCR = Gross Eligible Reserve Value / PPU Liabilities**

Risk-Adjusted Reserve Value:

**RARV = Σ [Market Valueᵢ × (1 − Haircutᵢ)] − Senior Non-PPU Liabilities**

Risk-Adjusted Collateral Ratio:

**RACR = RARV / PPU Liabilities**

Initial simulation thresholds:

Normal operation:

GCR ≥ 120%

and

RACR ≥ 110%

Restricted recovery mode:

GCR between 110% and 120%

or

RACR between 105% and 110%.

In recovery mode, new PPU may only be issued if the associated transaction restores or improves required collateral ratios.

Defensive mode:

GCR < 110%

or

RACR < 105%.

Ordinary minting shall automatically stop.

Redemptions shall continue while the reserve remains economically solvent.

Actual insolvency:

Gross realizable reserve assets < 100% of PPU liabilities.

At this point the protocol shall not pretend that full redemption remains possible.

A predefined resolution mechanism shall convert redemption to pro-rata realizable reserve value unless the reserve is recapitalized.

The 120%, 110%, and 105% levels are provisional v0.1 engineering parameters and must be validated or replaced through Phase 2 stress testing.

They are not ideological constants.

---

# ARTICLE VIII — RESERVE ELIGIBILITY

PPU v0.1 Core Reserve assets shall initially be restricted to assets with low credit risk, high transparency, and measurable liquidity.

Eligible categories shall initially consist of:

cash and qualifying cash equivalents;

short-duration U.S. Treasury bills;

appropriately collateralized short-term Treasury repo;

and short-duration U.S. Treasury Inflation-Protected Securities.

Individual TIPS used as core reserve assets should initially have no more than approximately two years of remaining effective duration exposure unless additional hedging exists.

The weighted interest-rate duration of the entire reserve shall be strictly limited.

Reserve-risk haircuts must include:

interest-rate risk;

real-rate risk;

liquidity risk;

custodian risk;

settlement risk;

oracle risk;

and basis risk.

A simplified duration stress approximation may be expressed as:

**Approximate price loss ≈ Duration × Yield Shock**

A two-year-duration inflation-linked security exposed to a hypothetical instantaneous +500 basis-point real-yield shock could therefore experience approximately a 10% duration-driven price decline before accounting for convexity.

This is why inflation linkage alone does not eliminate TIPS market-value risk.

Bitcoin, XRP, gold, equities, commodity exposures, energy assets, corporate credit, unsecured loans, DeFi lending positions, and speculative tokenized assets shall not count toward required v0.1 Core Reserve collateral.

They may be modeled during Phase 2.

They may not be introduced merely because their historical returns appear attractive.

No reserve asset may be:

rehypothecated;

pledged for unrelated liabilities;

secretly leveraged;

or counted simultaneously toward more than one reserve obligation.

---

# ARTICLE IX — REDEMPTION LIQUIDITY

At all times during normal operation, the protocol shall maintain liquid assets available within one business day equal to at least:

**30% of outstanding PPU liabilities**

unless Phase 2 demonstrates that a different level provides superior resilience.

Additionally:

**30-Day Liquidity Coverage Ratio ≥ 125%**

where the denominator represents modeled stressed redemption requirements over 30 days.

Liquidity shall be measured against liabilities, not merely as a percentage of reserve assets.

The protocol shall maintain sufficient liquidity to prevent routine redemption demand from forcing liquidation of longer-duration inflation hedges.

---

# ARTICLE X — RESERVE OUTPERFORMANCE

PPU holders shall receive the purchasing-power target defined by this Constitution.

PPU holders shall not automatically receive reserve investment gains.

If reserve assets outperform growth in PPU liabilities, the excess shall first strengthen First-Loss Capital.

Reserve income shall follow the following priority:

required custody, audit, oracle, insurance, legal, and protocol operating expenses;

restoration of liquidity requirements;

restoration of collateral requirements;

growth of First-Loss Capital;

and only afterward treatment as true reserve surplus.

PPU v0.1 shall distribute no reserve surplus while the monetary model remains experimental.

Reserve outperformance shall not cause the PPU Target Value to rise faster than its designated purchasing-power index.

PPU therefore remains a purchasing-power unit rather than an investment fund.

---

# ARTICLE XI — RESERVE UNDERPERFORMANCE

Reserve underperformance shall first reduce First-Loss Capital.

It shall not automatically reduce the PPU Target Value.

As collateralization deteriorates:

surplus distributions stop;

new issuance becomes restricted;

ordinary minting stops at predefined thresholds;

reserve risk is reduced;

liquidity is increased where possible;

all reserve income is retained;

and external recapitalization may be accepted under predefined rules.

Governance may not solve undercollateralization by issuing unbacked PPU.

Governance may not retrospectively redefine inflation in order to reduce PPU liabilities.

If reserve assets become insufficient to satisfy all PPU liabilities, losses must be recognized explicitly through the predetermined resolution mechanism.

---

# ARTICLE XII — MINTING

PPU supply shall expand only in response to actual collateralized issuance.

No administrator, governance body, founder, validator, custodian, central bank, oracle operator, or emergency committee shall possess unrestricted authority to create PPU.

A valid mint requires:

a valid PurchasingPowerOracle;

a valid ReserveOracle;

confirmed settlement of eligible reserve assets;

satisfaction of liquidity requirements;

satisfaction of post-mint collateral requirements;

and authorization by the MintBurnController.

PPU shall never be minted against:

anticipated collateral;

unsettled transfers;

accounts receivable;

future revenue;

expected reserve yield;

or unsecured promises.

For N newly issued PPU:

**Senior reserve contribution = N × Current PPU Target Value**

plus whatever additional first-loss capital is necessary to maintain mandatory collateral ratios.

Mint fees may exist to cover operating and liquidity costs but must be transparent, bounded, and formulaic.

Mint fees shall not constitute discretionary monetary policy.

---

# ARTICLE XIII — REDEMPTION

Redemption is a fundamental monetary mechanism of PPU.

A qualified reserve-layer participant surrendering PPU shall be entitled, while the protocol is solvent and functioning normally, to redemption based upon:

**Number of PPU Redeemed × Current PPU Target Value**

minus a transparent predefined redemption cost.

Redeemed PPU shall be burned.

Redemption must create real economic arbitrage.

If secondary-market PPU trades materially below target, participants must be capable of acquiring PPU and redeeming it for reserve value.

If PPU trades materially above target, qualified participants must be capable of creating additional fully backed PPU and selling it into the market.

This mint/redemption mechanism, rather than an unsupported algorithmic price target, shall provide the primary economic force anchoring PPU to its target.

Redemption fees may compensate the reserve for genuine transaction and liquidation costs.

They shall not be increased arbitrarily to conceal insolvency or prevent economically legitimate redemptions.

Large redemptions may eventually permit settlement through qualifying in-kind Treasury assets when legally and operationally practical, reducing forced asset sales.

---

# ARTICLE XIV — RESERVE-LAYER ACCESS

At initial production deployment, direct reserve-layer minting and redemption shall occur through multiple qualified Authorized Participants.

Authorized Participants may include appropriately regulated financial institutions, market makers, custodians, or other entities meeting published eligibility requirements.

Authorized Participant criteria shall be objective and public.

No single Authorized Participant shall have an exclusive franchise.

Holding and transferring PPU should remain as open as legally possible.

The monetary constitution shall separate access-control requirements imposed by law from monetary-policy rules.

Compliance requirements may determine who can interact directly with the off-chain reserve.

They shall not authorize discretionary changes to the PPU monetary target.

---

# ARTICLE XV — RESERVE LEGAL OWNERSHIP

Assets counted as PPU reserves must be legally owned or held for the benefit of the appropriate reserve structure.

Proof of Reserve alone shall not be sufficient.

The protocol must also establish:

proof of liabilities;

legal ownership;

absence of undisclosed liens;

custodial segregation;

bankruptcy treatment;

and the senior economic position of PPU redemption claims.

Assets that cannot be legally verified as available to satisfy PPU obligations shall receive zero reserve value.

---

# ARTICLE XVI — ORACLE ARCHITECTURE

The protocol shall distinguish between:

PurchasingPowerOracle;

ReserveAssetPriceOracle;

Custodian/Proof-of-Reserve Oracle;

and Liability Accounting.

Purchasing-power data shall be deterministic from authoritative source data.

Reserve-market pricing shall use independent market sources.

Custodial assets shall require verifiable reporting from custodians and independent attestations.

The protocol shall not rely upon one organization's unaudited statement that reserves exist.

Oracle disagreement shall cause the protocol to become more conservative.

It shall never automatically allow increased issuance.

When critical oracle data become stale:

minting shall fail closed;

additional reserve haircuts may apply;

and the last cryptographically verified purchasing-power value may temporarily govern redemptions according to predefined fallback rules.

---

# ARTICLE XVII — TRANSPARENCY

The protocol shall publicly expose in machine-readable form:

circulating PPU supply;

current PPU Target Value;

total PPU liabilities;

reserve composition;

gross collateral ratio;

risk-adjusted collateral ratio;

available liquidity;

pending redemptions;

reserve haircuts;

oracle freshness;

and emergency-system status.

On-chain PPU liabilities shall be observable continuously.

Off-chain reserve assets shall be reconciled as frequently as operationally possible and subject to independent external examination.

The reserve must be auditable as a balance sheet, not merely advertised through wallet addresses.

---

# ARTICLE XVIII — GOVERNANCE

PPU shall practice minimized governance rather than attempting to eliminate all human governance.

Governance shall be able to perform only explicitly enumerated functions.

Adjustable peripheral parameters may include matters such as:

approved custodians;

approved Authorized Participants;

oracle implementations;

reserve-asset adapters;

operational fees within constitutional bounds;

and collateral haircuts within predetermined risk limits.

Core monetary rules shall not be casually upgradeable.

The production PPUToken, TargetCalculator, and fundamental issuance constraints should ultimately be immutable or protected from in-place constitutional rewriting.

Fundamental monetary changes should generally require deployment of a new protocol version.

Existing holders must then be permitted to remain in the prior system, redeem, or voluntarily migrate.

Governance shall not be permitted to force holders into materially different monetary terms.

---

# ARTICLE XIX — CONSTITUTIONALLY PROTECTED RULES

No ordinary governance vote shall be permitted to:

create unbacked PPU;

arbitrarily increase PPU supply;

arbitrarily redefine the PPU Target Value;

rebase user wallet balances;

confiscate PPU from arbitrary accounts;

redirect reserve assets to unrelated purposes;

subordinate PPU holders to governance-token holders;

eliminate reserve transparency;

permit hidden reserve leverage;

permit rehypothecation of core reserves;

retroactively reduce existing PPU redemption claims;

or grant administrators unlimited emergency authority.

The designated purchasing-power index may be replaced only through a predefined Index Contingency process if the original index is discontinued, becomes unavailable, or is fundamentally changed.

The preferred fallback should preserve the closest achievable economic relationship with the reserve's inflation hedges.

---

# ARTICLE XX — EMERGENCY POWERS

Emergency authority shall be designed around the principle:

**reduce risk, do not create new monetary power.**

An Emergency Controller may be permitted to:

temporarily stop minting;

quarantine a compromised oracle;

quarantine a compromised collateral adapter;

temporarily increase risk haircuts;

and temporarily restrict a technically compromised contract.

Emergency authority may not:

mint PPU;

change PPU balances;

change the purchasing-power formula;

lower required collateralization;

transfer reserve assets to administrators;

cancel valid PPU liabilities;

or permanently change protocol rules.

Minting may be paused immediately when necessary.

Emergency powers shall automatically expire unless renewed through the constitutionally defined process.

A redemption pause shall be permitted only when continuation would create direct technical or security risk and shall have a significantly shorter maximum duration than a minting pause.

A liquidity shortage alone shall not justify pretending valid PPU claims no longer exist.

When possible, the protocol shall:

**fail closed for new issuance while preserving orderly redemption.**

---

# ARTICLE XXI — INDEX CONTINGENCY

The protocol shall predefine its response if CPI-U:

ceases publication;

is materially redefined;

becomes unavailable for an extended period;

or is determined by predetermined objective criteria to be unusable.

The protocol shall not allow administrators to choose a replacement index opportunistically.

A fallback hierarchy shall be encoded before production deployment.

Until the precise hierarchy is finalized, the preferred principle is to follow the official successor or replacement methodology applicable to the U.S. Treasury inflation-linked market whenever doing so preserves the closest asset-liability hedge.

---

# ARTICLE XXII — SUPPLY ELASTICITY

PPU shall have an elastic supply but not discretionary money creation.

Supply increases when demand results in properly collateralized minting.

Supply decreases when PPU is redeemed and burned.

There shall be no arbitrary target supply.

There shall be no issuance schedule.

There shall be no mining emission.

There shall be no founder allocation created merely because a fixed token supply exists.

There shall be no algorithmic expansion intended solely to push the secondary-market price downward.

Monetary elasticity shall emerge from reserve-backed creation and redemption.

---

# ARTICLE XXIII — BLOCKCHAIN NEUTRALITY

The Monetary Constitution shall remain independent of the eventual settlement blockchain.

Ethereum, Ethereum L2 systems, XRPL EVM infrastructure, XRPL interoperability, or other networks may be evaluated during protocol engineering.

Blockchain selection shall not change:

what one PPU represents;

the PPU target formula;

reserve requirements;

redemption seniority;

or constitutional monetary restrictions.

The monetary system shall be designed before choosing infrastructure merely because a particular blockchain is commercially attractive.

---

# ARTICLE XXIV — PPU v0.1 RESEARCH STATUS

Every numerical risk parameter in this Constitution shall be treated as a hypothesis until tested.

In particular, Phase 2 must determine whether:

120% gross collateralization is sufficient, excessive, or inefficient;

110% risk-adjusted collateralization provides adequate protection;

30% immediate liquidity is appropriate;

the proposed TIPS duration limitation is sufficient;

the reserve can survive rapid increases in real interest rates;

reserve income is sufficient to maintain required first-loss capital;

and PPU can expand economically without making capital requirements prohibitively expensive.

If simulation demonstrates that any assumption fails, the protocol shall change.

The purpose of PPU is not to prove the original concept correct.

The purpose is to determine whether a purchasing-power-preserving monetary architecture can actually survive.

## Editorial end of constitution
The preceding Article XXIV is the final constitutional article in the supplied source. The two following analysis sections remain in the evidence file; see the reconciliation for their destinations.
