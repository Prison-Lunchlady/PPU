# WP1A — Purchasing-Power Standard Research Report
Revision 1.1 • 2026-09-19 America/Chicago • Research recommendation awaiting Gate 1A

## Finding
Recommend an explicitly **U.S. urban consumer-price-indexed** v0.1 unit, using CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted as its underlying benchmark. This is a conditional choice about the economic promise, not proof that the protocol can deliver it. The recommendation is narrower than universal purchasing-power preservation and does not approve TIPS interpolation, a reserve portfolio or the original constitution.

The conditional choice survives comparison **if Brad and primary review affirm the decision rule below**. It does not survive as a claim that CPI is the best possible measure of individual living costs, fully independently reconstructible, immune to institutional influence, always published, or a perfect hedge. See the [comparison matrix](02-comparative-benchmark-matrix.md), [methodology](03-methodology-and-revisions.md), [institutional risks](04-benchmark-institutional-risk.md) and [hedge analysis](05-hedgeability-and-matching.md). Those documents contain the factual evidence; the judgments below are model interpretation and recommendations.

## Method and decision criteria
The authorized question is benchmark choice, not maximizing compatibility with the old draft. The assessment first distinguishes economic concepts, then compares coverage, statistical construction, publication/revision behavior, independent verification, institutional dependency and hedgeability. No arbitrary weighted score is used: its weights would obscure the value judgment about what PPU promises. No empirical PPU performance claim is made. Source retrieval was live on 2026-09-19 local time; source versions, limitations and affected questions are indexed in [the source register](sources.md).

Economic concepts considered:
 
**Proposed decision rule:** first require a meaningful aggregate consumer-price promise for the chosen population; among candidates meeting that threshold, prioritize manageable contractual vintages and a practical matching path over incremental substitution fidelity. This ordering is a project judgment proposed to Gate 1A, not a fact derived from statistics or established user demand. If Brad/primary review instead prioritize a closer constant-utility approximation, the CPI-U recommendation must be reconsidered rather than accepted on operational convenience alone.

- **Nominal dollars:** observable and familiar, but does not meet the inflation-adjusting objective.
- **Price change for a permanently fixed physical basket:** concrete but increasingly unrepresentative as goods disappear, quality changes and spending changes. This is not what modern CPI-U does.
- **Constant household utility/cost of living:** economically attractive but depends on household preferences and substitution, cannot be one observable universal basket. C-CPI-U is the strongest direct challenger for this concept.
- **Broad U.S. consumption prices:** PCE is a serious candidate when consumption financed on households' behalf is part of the intended promise.
- **Named published consumer-price index:** narrower and auditable at the output level; its definition and exceptions must be disclosed. Recommended for v0.1.
- **Worldwide purchasing power:** requires a population, country weights, exchange-rate convention and consumption concept. Global transfer alone defines none of these.

## Answers to the twelve authorized questions
### 1. What economic concept should one PPU preserve?
**Recommendation:** cumulative change in the price level of a specified aggregate U.S. urban consumption measure, relative to a base reference. Describe this as a benchmark-linked target, not an unconditional ability to buy the same goods today. The proposed standard states the reference economic exposure. Whether a token holder can realize that target depends on later economic and legal work.

### 2. Is standardized U.S. consumer purchasing power the correct v0.1 promise?
**Interpretation:** defensible only as qualified shorthand. Prefer “U.S. urban consumer-price-indexed” with the index named alongside it. “Standardized” must not imply a real representative person's budget, all U.S. residents, or fixed welfare. **Uncertainty:** user demand for this limited promise has not been tested. If the intended users principally want non-U.S. local living-cost preservation, this recommendation should be reopened.

### 3. Which benchmark best represents that promise?
**Recommendation:** CPI-U NSA all-items U.S. City Average. C-CPI-U better addresses a particular substitution issue; PCE covers a broader consumption concept. Neither is inherently inferior. CPI-U wins for this proposed v0.1 objective after explicitly accepting its representativeness and measurement limits. TIPS Reference CPI is a transformation/contract convention, not a competing basket.

### 4. What limitations and basis risks follow?
**Interpretation:** household, income, age, tenure, location and non-U.S. spending can differ; asset affordability differs from consumption-service inflation; updated weights and quality adjustment change the measured object. Publication and target lag create timing basis. Any mismatch in chosen vintages or contingencies introduces contractual basis. Index tracking cannot cure market discounts, access costs, fees or insolvency. Detailed routing is in the hedge analysis; no related risk is closed.

### 5. How significant is publication lag?
**Fact:** publication is normally in the following month, whereas Treasury's daily convention adds a separate lag. **Interpretation:** smooth low inflation can make the timing gap look small; shocks and outages can make it material. The [lag examples](03-methodology-and-revisions.md) show sensitivity, not a calibrated acceptable tolerance. No frequency, lag, nowcast or fallback is selected in WP1A.

### 6. Are published values revised?
**Fact:** NSA CPI-U avoids routine revision but can be corrected for errors; C-CPI-U and PCE have meaningful revision/vintage considerations. There is also a missing October 2025 headline observation, not merely a delayed release; see the methodology analysis. Treasury obligations can retain a previously reported number despite later revisions. **Recommendation:** prohibit the blanket phrase “never revised.” Benchmark selection does not itself define which vintage is binding.

### 7. Can it be independently and deterministically reproduced?
**Finding:** two different tests have different answers. Available published observations can be independently retrieved and a fully specified transformation recomputed; a continuous historical monthly path cannot be assumed in light of the 2025 gap. Full CPI construction from public raw observations cannot be assumed, because confidential microdata and statistical judgments are involved. Even downstream determinism is incomplete until WP1B specifies vintage, dates, arithmetic and exceptional states. Multiple mirrors improve delivery resilience, not independent measurement.

### 8. How vulnerable is it to methodology or institutional influence?
**Interpretation:** nonzero and unavoidable for an externally administered statistical index. Legitimate updates, resource constraints, collection interruptions and discretionary replacement differ from malicious manipulation. Reviewed evidence establishes institutional dependencies and an actual outage; it does not establish deliberate falsification. Freezing the name of a series does not freeze its underlying methodology. See the risk analysis; no governance mechanism is selected.

### 9. Is there a practical hedge?
**Fact:** TIPS provide CPI-related contractual cash flows. **Interpretation:** this gives CPI-U a useful asset-liability research advantage. It does not establish a replicating portfolio for continuously redeemable PPU, particularly when target and security conventions differ. No allocation, duration, capital or collateral ratio is chosen.

### 10. Would another benchmark materially improve the architecture?
**Finding:** it could, under a different prioritized promise. C-CPI-U improves substitution representation; PCE broadens consumption coverage; a regional index improves fit for its own population; daily private data may improve timeliness. These gains bring finality, basis, access or institutional tradeoffs. The reviewed evidence does not demonstrate that their net benefit exceeds the cost for this v0.1 objective. No absolute “no hedge exists” claim is made.

### 11. What is lost by choosing a theoretically better but operationally weaker index?
**Interpretation:** greater conceptual fidelity can require stale final observations, provisional obligations later corrected, or intentionally frozen preliminary observations that diverge from the final statistic. It can also increase custom hedge and data-access dependencies. These costs are real, but operational convenience cannot rescue a benchmark that fails the intended promise. If constant-utility approximation is non-negotiable, CPI-U should lose and the project should accept or investigate those costs explicitly.

### 12. Should v0.1 remain U.S.-based despite global transferability?
**Recommendation:** yes, as a deliberately bounded first standard, subject to primary/user review of that scope. Global transfer is a delivery capability. If x is local currency per dollar, local real exposure is proportional to PPU's dollar reference × x / local price index. A hypothetical 4% increase in the U.S. reference and 10% fall in x yields 1.04 × 0.90 = 0.936 local nominal value before local inflation. Thus international use can lose local purchasing power even while the U.S. reference is followed.

## Attempts to defeat the CPI-U hypothesis
| Challenge | Result and consequence |
|---|---|
| A cost-of-living index should account for substitution more completely | Substantive objection accepted. CPI-U is not a constant-utility guarantee. C-CPI-U remains the counterfactual choice if that promise takes priority. |
| A stablecoin-like liability cannot wait for stale consumer-price measurements | Objection qualifies the promise. No instantaneous preservation claim; quantify tolerances later. Faster input is not necessarily representative input. |
| A public index must be reproducible without institutional trust | Strong version falsified. Public transformations are reproducible; raw measurement is not fully permissionlessly reconstructible. |
| CPI and TIPS share an index, so the hedge must be exact | Falsified as a blanket claim. Vintage, missing-index rules, duration and liquidity can differ. Actual 2025 contingency makes this operational rather than hypothetical. |
| U.S. CPI can preserve worldwide purchasing power | Rejected by the algebraic counterexample above, not an empirical backtest. Geographic and currency basis remain. |
| A proprietary index eliminates political risk and fixes lag | Unsupported. It substitutes provider, data access and methodology control risks; full counterfactual replication and independent audit were not established. |
| Existing constitutional wording should dictate the winner | Rejected research method. Recommend amendments rather than retain inaccurate claims. |

## Uncertainty and research limits
No return backtest, hedge-cost estimate, demand study, full input-data audit or institutional-independence probability model was performed. Those absences limit investment/solvency or universal-optimality claims, not the ability to make a bounded benchmark recommendation. Source schedules and methodology can change. WP1B must treat exceptional states as requirements and later work must test the economic consequences. The [recommended standard](06-recommended-standard.md) identifies exactly what Gate 1A can accept and what remains unselected.

