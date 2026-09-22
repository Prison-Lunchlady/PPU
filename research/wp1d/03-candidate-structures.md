# Candidate Reserve Structures
Revision 0.1 • all weights illustrative percent of reserve market value, not liability and not approved allocations.

| Case | Cash | Bills | Short TIPS | Expected strength | Attempt to falsify |
|---|---:|---:|---:|---|---|
| A | 20 | 80 | 0 | Lower duration; many dated nominal receipts | Unanticipated inflation, low rollover yields, repeated expenses erode buffer |
| B | 20 | 40 | 40 | Mixed liability/settlement sensitivity | Simultaneous real-rate increase and run can overwhelm the buffer |
| C | 40 | 40 | 20 | More immediate capacity if bank cash accessible | Cash drag, bank failure; initial liquidity does not imply full-run coverage |
| D | 10 | 20 | 70 | Greater index sensitivity before rate/liquidity effects | Long liquidation queue, TIPS fire sale, index/contract basis |

Test reverse repo as a substitution within the bill sleeve (0/10/20% total asset share), never an extra asset. Conditional 100 receivable secured by collateral marked102: a5% collateral fall and1% incremental liquidation cost yields95.931 collateral recovery, not197.931. Matured but unpaid repo remains receivable; default does not magically convert it into usable cash. No unsecured deficiency recovery assumed in the example.

Comparison uses A0=120 and L0=100 USD million only to keep scale common. This does not select 120% collateralization or reproduce Phase 2's full 105–130% grid. Ratios must reference gross WP1C liability, and other claims remain separately visible. Candidate rankings can reverse with target path, net carry, queue mix, sale deadline and price basis; no optimizer is run.

In the synthetic deflation case target -.10, cash1/bills1.01/TIPS.90, B has115.68 assets. All-indexed liability90 gives25.68 buffer; 20 fixed USD plus80 indexed gives92 liability and23.68 buffer. Fixed accepted claims reduce deflation relief. Neither acceptance branch is selected, and face price does not determine legal priority.

Every candidate must also be tested with inaccessible cash and common custodial failure; reallocating between securities at the same inaccessible custodian may add no operational diversification. See [scenario results](scenario-results.json) and [adversarial analysis](08-adversarial-failure-analysis.md).
