# Hedgeability and Asset-Liability Matching Analysis
WP1A • 2026-09-19 • Conceptual feasibility screen, not reserve architecture

## Established facts
TIPS adjust principal with inflation/deflation, pay interest against adjusted principal, and provide a principal floor at maturity. Those contractual features differ from a transferable unit potentially redeemed before the bond matures. [Treasury TIPS description](https://www.treasurydirect.gov/marketable-securities/tips/).

Treasury uses a defined lagged CPI reference and its own vintage and contingency rules. In 2025 it applied a substitute observation for missing October CPI. “Both use CPI” therefore does not establish identical obligations in every state. [Treasury actual contingency announcement](https://home.treasury.gov/news/press-releases/sb0324). Full convention analysis is in the [methodology report](03-methodology-and-revisions.md).

**Observed values, limited inference:** September 2025 CPI-U NSA was 324.800; Treasury's October substitute was 325.604; November's published value was 324.122. The substitute is 325.604 / 324.122 − 1 ≈ **0.457%** above November. This compares different reference months; it is **not** measured same-month basis, hedge error or PPU loss, since the actual October headline is missing and PPU target rules are unselected. [BLS observations](https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm), [Treasury reference sheet](https://www.treasurydirect.gov/instit/annceresult/tipscpi/2026/CPI_20260113.pdf).

**Additional matching path:** ISDA's November 25, 2025 market-practice announcement concerns initial reference levels for certain new CPI-U inflation derivative trades under its 2008 definitions. Its accompanying explanation recommends voluntary use of the TIPS fallback methodology for the missing October level. This establishes a standardized-contract research path beyond TIPS, not a tradable quote, universal contract convention or proof of PPU access. [ISDA announcement](https://www.isda.org/2025/11/25/determining-initial-reference-index-for-new-trades-referencing-cpi-u/), [ISDA explanation](https://www.isda.org/?p=1157058). Publisher-indexed excerpts were available; full-page/PDF retrieval failed, so detailed legal operation is not asserted.

## Model interpretation
Let a hypothetical liability reference move with I_L(t)/I_L(0), while an indexed asset's principal reference moves with I_A(t)/I_A(0). Even before coupons, market prices and credit effects, relative index coverage depends on [I_A(t)/I_A(0)] / [I_L(t)/I_L(0)]. If those paths differ because of vintages, lag, corrections or fallback, index matching is imperfect. This identity is diagnostic, not a reserve or liability design.

| Mismatch | Why an index connection is insufficient | Authorized later destination |
|---|---|---|
| Different geography or consumption scope | CPI-linked cash flow does not promise PCE, CPIH or global consumption | Reconsider standard if desired; WP1D/Phase 2 quantify basis |
| Different lag, vintage or outage handling | Asset and target can use different observations | WP1B specifies candidate target; WP1D tests match; WP1G handles authority |
| Real-yield duration and sale timing | Indexed maturity cash flows need not equal interim market sale value | WP1D and Phase 2 |
| Coupons, maturity, reinvestment | Income timing differs from liability timing | WP1C/1D/1E; no retained-income sufficiency assumed |
| Deflation floor | Asset floor depends on security terms and maturity; it is not a free floor for PPU | WP1B, WP1D, Phase 2 |
| Liquidity, access, settlement and transaction costs | Transferable token time differs from reserve realization time | WP1F and Phase 3 |
| Capital and reserve losses | Hedge relevance does not prove solvency or scalable junior funding | WP1E and Phase 2 |

**Conclusion:** CPI-U has a practical hedge research advantage because an established security references the same broad index family. Exact replication, cost, availability to the eventual entity and required capital remain unproved. Shortening bond duration can change risk but is not chosen or endorsed as sufficient here.

For C-CPI-U and PCE, the reviewed sources did not establish an off-the-shelf government security directly matching those series. That is a limit of this evidence, not proof that no hedge or derivative can exist. A custom swap or cross-index hedge might help, but pricing, counterparties, basis and legal access need separate investigation. Regional inflation-linked instruments would require checking each contract's index, currency and lag; no portfolio is selected by the matrix.

## Most consequential contrary evidence
The draft favors observed values and TIPS matching simultaneously. Treasury's missing-data rule can use extrapolation and its index substitution can involve external judgment. A PPU rule that forbids both may intentionally depart from the asset reference. A rule that follows Treasury may instead relax the draft's intended constraints. **No resolution selected.** WP1B must expose alternatives and WP1G must address constitutional authority; preserving this tension is a standing Gate 0 condition.

**Recommendation:** use hedgeability as one criterion in benchmark selection, not as a backdoor selection of Treasury/TIPS reserve composition, collateral ratios, junior capital, redemption terms or APs. The six collateral ratios and alternative assets preserved from WP0A remain later simulation work, untouched here.
