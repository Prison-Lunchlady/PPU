# Source capture: Phase 0 state

Source: conversation 6aaf31ef-3638-83ea-bdde-10a3e6ba7b4e, latest returned assistant response. Full 10,337-character response recovered; historical citation tokens preserved but not independently resolved.

I’m adopting this as the **PPU Development Roadmap v0.1** and as the project-control framework for this chat. Its central rule is important: PPU advances through discrete Work Packages, actively searches for flaws, documents assumptions, and stops at each Review Gate before moving forward. fileciteturn0file0L28-L56

It also changes how I think we should proceed from here. Before doing more monetary design, we should complete **Work Package 0A** so we have a permanent source of truth rather than letting important decisions disappear into a long conversation. The roadmap explicitly calls for a Protocol State, Decision Register, Risk Register, and Research Library. fileciteturn0file0L60-L136

## PPU Protocol State — Initial Entry

**Project:** PPU — Purchasing Power Unit  
**Roadmap:** v0.1  
**Current phase:** Phase 0 — Project Infrastructure  
**Current Work Package:** 0A — Canonical Project Structure  
**Next phase after approval:** Phase 1 — Monetary Architecture

### Current architectural hypothesis

PPU is being investigated as a redeemable digital monetary unit whose nominal value changes with a defined purchasing-power benchmark rather than remaining fixed at $1.

Current working formula:

\[
T_t = B \times \frac{I_t}{I_0}
\]

where:

- \(T_t\) = current PPU target value
- \(B\) = $1.00 genesis/base value
- \(I_t\) = current reference purchasing-power index
- \(I_0\) = base-date reference index

Balances should not rebase merely because inflation changes.

Supply should expand only through collateralized minting and contract through redemption and burning.

### Working monetary architecture

The current **hypothesis**, not yet a finalized constitutional decision, is:

- CPI-U NSA as the initial purchasing-power benchmark.
- Daily target calculation based substantially on the TIPS Reference CPI methodology.
- Core reserve initially centered on cash, Treasury bills, qualifying Treasury repo, and short-duration TIPS.
- Separate first-loss capital protecting PPU liabilities.
- PPU liabilities senior to claims on reserve surplus.
- Minting allowed only when collateral, liquidity, oracle, and settlement requirements are satisfied.
- Redemption provides the economic anchor between secondary-market price and target value.
- Governance should be narrowly constrained.
- Emergency powers should generally be capable of **reducing risk**, not creating new monetary authority.
- Bitcoin, gold, equities, commodities, XRP, and other assets remain research candidates rather than assumed core collateral.

These remain subject to the full Phase 1 research program and Phase 2 attempts to break them.

## Initial Decision Register

**PPU-D001 — Project purpose**

PPU will be treated as a monetary research and engineering project, not as an immediate token-launch project.

**Status:** Accepted.

This follows the roadmap's explicit statement that token issuance is not the initial objective. fileciteturn0file0L6-L22

---

**PPU-D002 — Development sequencing**

Economic architecture will be designed before blockchain selection and production contract development.

**Status:** Accepted.

The roadmap places monetary architecture and economic simulation before legal architecture, technical design, and testnet implementation. fileciteturn0file0L142-L168 fileciteturn0file0L340-L380

---

**PPU-D003 — Custom purchasing-power index**

PPU will **not assume** that a proprietary index is superior to CPI.

CPI-U, TIPS methodology, C-CPI-U, PCE, alternatives, and potential future global indexes must first be researched under Work Package 1A. fileciteturn0file0L148-L168

**Status:** Open hypothesis.

---

**PPU-D004 — Alternative reserve assets**

Gold, Bitcoin, commodities, equities, and tokenized RWAs will not automatically become core reserve assets.

They must demonstrate improved monetary resilience relative to the Treasury/TIPS baseline after volatility, liquidity, correlation, custody, drawdown, legal, and basis-risk effects are included. fileciteturn0file0L472-L496

**Status:** Accepted research methodology.

---

**PPU-D005 — First-loss capital**

Overcollateralization requires a distinct capital structure and cannot simply be assumed to arise from ordinary PPU minting.

**Status:** Critical unresolved architecture question.

This receives its own Work Package because we need to determine who supplies that capital, how it is compensated, how dilution and recapitalization work, and what happens during insolvency. fileciteturn0file0L248-L267

## Initial Risk Register

I would start the register with these as the highest-priority risks:

| ID | Risk | Current severity |
|---|---|---|
| R-001 | Reserve assets fail to grow with inflation-linked PPU liabilities | Critical |
| R-002 | Capital requirements make PPU economically unscalable | Critical |
| R-003 | Redemption run forces reserve losses at unfavorable market prices | Critical |
| R-004 | TIPS duration/real-rate risk causes collateral impairment | High |
| R-005 | Inflation-index methodology fails to represent intended purchasing power | High |
| R-006 | CPI publication lag creates meaningful target mismatch | Medium/High |
| R-007 | Reserve custody or legal structure prevents holders from having enforceable claims | Critical |
| R-008 | Oracle failure or manipulation corrupts mint/redemption calculations | Critical |
| R-009 | Governance gradually acquires central-bank-like discretionary powers | Critical |
| R-010 | Authorized Participants become concentrated or fail during stress | High |
| R-011 | Off-chain reserves cannot be continuously verified with adequate confidence | High |
| R-012 | Regulatory treatment makes proposed reserve/redemption architecture impractical | Critical |
| R-013 | Smart-contract failure compromises liabilities or collateral | Critical |
| R-014 | Cross-chain architecture introduces unacceptable bridge risk | High |
| R-015 | Secondary-market liquidity is insufficient for arbitrage to maintain target proximity | High |

That matches the roadmap's requirement to track economic, reserve, liquidity, oracle, governance, custodial, legal, blockchain, smart-contract, adoption, and operational risks. fileciteturn0file0L103-L117

## Active hypotheses

These should be explicitly recorded rather than silently treated as facts:

**H-001:** CPI-U NSA is currently the strongest starting benchmark because it is externally administered and has a natural hedge through TIPS.

**H-002:** Daily interpolation is preferable to monthly step changes.

**H-003:** A Treasury/TIPS-dominant reserve can sufficiently hedge PPU's inflation-linked liability without relying heavily on risky assets.

**H-004:** First-loss capital can be structured in a way that simultaneously provides meaningful solvency protection and permits practical supply growth.

**H-005:** A functioning redemption mechanism can keep market price sufficiently close to target without algorithmic market intervention.

**H-006:** PPU can permit monetary supply elasticity without granting any party discretionary issuance authority.

**H-007:** Governance can be minimized sufficiently that the protocol does not simply recreate a small private central bank.

**H-008:** A legally enforceable relationship between token liability and off-chain reserves can be constructed.

None should be promoted to constitutional fact until the relevant Work Package resolves it.

## Known unresolved questions

The most important one is probably **not CPI or blockchain selection**.

It is:

> **Who economically owns the first-loss layer beneath PPU, and why would they supply capital?**

Until that is solved, we don't yet have a complete monetary system.

Suppose:

\[
L=\$1\text{ billion}
\]

and required collateralization is 120%.

Then:

\[
R=\$1.2\text{ billion}
\]

There is a **$200 million junior-capital requirement**.

If PPU doubles to $2 billion while retaining 120% backing, reserve assets must become:

\[
\$2.4\text{ billion}
\]

So another **$200 million of first-loss capital** has to appear in addition to the $1 billion backing the newly issued monetary claims.

That means we eventually need to compare structures such as:

- permanent protocol equity;
- retained reserve earnings;
- separately subscribed junior capital;
- regulated reserve-company equity;
- a subordinated capital token;
- combinations of these;
- or a substantially lower required capital ratio if simulations justify it.

And we cannot choose based merely on what sounds decentralized.

We need to determine mathematically what the liability actually requires.

## Canonical research organization

The roadmap also gives us a clean research sequence for Phase 1:

**1A:** What does one PPU actually preserve?  
**1B:** Exactly how is its target calculated?  
**1C:** Exactly what liability exists?  
**1D:** What assets should support it?  
**1E:** Who absorbs losses?  
**1F:** How does money enter and leave the system?  
**1G:** Who can change anything?

Only then do we pass **Review Gate 1**, at which point we must be capable of answering the fundamental questions about value, backing, minting, contraction, bank runs, reserve losses, insolvency, and governance without hidden assumptions. fileciteturn0file0L315-L336

That sequencing is strong enough that I would **replace the earlier Monetary Constitution v0.1 with “Draft Constitution / Hypothesis Set v0.1” rather than treating it as settled policy.** Phase 1 exists specifically to earn those constitutional decisions.

### Work Package 0A status

With the structure above, we have the beginnings of:

- Protocol State
- Decision Register
- Risk Register
- active hypotheses
- unresolved questions
- current development phase
- next authorized Work Package

The roadmap's Review Gate 0 says the infrastructure should eventually let another qualified researcher or engineer understand PPU without reading the whole chat history. fileciteturn0file0L136-L138

I would **not declare Review Gate 0 complete yet**. The remaining infrastructure work is to formalize these records into persistent project files and establish the Research Library.

After that, the first actual monetary research task is exactly the right one:

**Work Package 1A — Purchasing-Power Standard: determine precisely what one PPU promises to preserve.**
