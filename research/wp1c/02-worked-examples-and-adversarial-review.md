# WP1C worked examples and adversarial review

Synthetic calculations using exact arithmetic, not observed user behavior or asset performance. Proposed definitions pending Gate 1C; no queue contract selected. All values USD unless specified.

| Case | Calculation / failure | Required model treatment |
|---|---|---|
| 100 live, target 1.10 | L=110 | Recognition of 100 claims; no backing assumption |
| 20 requested, not accepted | 80 live + 20 requested = 100 indexed | L stays 110; request alone creates no extra claim |
| 20 accepted fixed at 1.10 | 80×1.10 + 22 = 110 | Move predecessor once; not 100×1.10+22=132 |
| Same accepted indexed | (80+20)×1.10=110 | Queue units belong to Qidx, not both N and Qidx |
| Target rises to 1.20 | Fixed: 118; indexed: 120 | Queue contract changes exposure; neither is universally superior |
| Target falls to 0.90 | Fixed: 94; indexed: 90 | Fixed face retains dollars; no floor added to the indexed unit |
| Partial fixed discharge 11 | Fixed remainder=11, attributed remaining original units=10 | No rounding away residual; no second full payment allowed |
| Partial indexed discharge 10 units | 10 units remain; value follows current T | No dollar lock inferred from unit quantity |
| Transfer-only event | Aggregate L unchanged | Individual holdings are outside aggregate model; cannot infer user demand |
| Cancel fixed 22 face at T=1.20 | Restore 20 units: new face 24; restore 22/1.20 units: altered unit quantity | Neither accepted-claim cancellation policy silently chosen |
| Payment initiated but reversible | Obligation may remain | No discharge without effective-discharge fact; evidence truth external |
| Burn with unpaid accepted claim | Supply may fall while monetary debt remains | Burning is not modeled as discharge |
| Frozen target / impairment | Reference L may stay calculable while real coverage fails | Carry impairment label; Q023 stays an activation blocker; no automatic compensation |
| No binding target | Indexed portion cannot be valued by this rule | Report undetermined; separately retain fixed faces |
| Assets 90, claims 100 | Shortfall=10 | Liability is not automatically 90; no haircut/waterfall selected |
| Pending refundable funds | Possible non-token obligation before mint | Inventory separately; unknown is not zero |

## Attempts to falsify the framework

**F1 — Effective acceptance fiction (material unresolved implementation dependency).** An arithmetic move cannot prevent a bearer token being spent twice or prove that a legal promise has replaced it. If the source token is still independently valid, the ledger must not assert a single replacement. Gate 1C can accept the invariant as a requirement, not its implementation. Later transaction/chain/legal evidence required.

**F2 — Fixed queue timing option.** If users can freely lock current dollar face before an expected decline and cancel after an expected rise, the queue embeds an option. Daily predictable changes do not remove this problem. A fixed queue without cancellation may reduce optionality but impose liquidity/access costs; an indexed queue removes this particular lock but retains changing settlement amounts. No access/fee/cancellation scheme is selected.

**F3 — False finality.** “Payment sent,” chain inclusion or token burn is not necessarily economic/legal discharge. The test harness trusts an explicit effective-discharge fact and must not be presented as proof that this fact is obtainable securely. A failed/reversible payment cannot silently shrink liabilities.

**F4 — Hidden legal or deposit claims.** A complete unit ledger can still omit refunds, damages, secured claims, costs or another entity's promises. This model cannot classify actual PPU liabilities under law or accounting rules. TOTAL_UNDETERMINED remains until input completeness is justified; no declaration is certification.

**F5 — Denominator camouflage.** Removing queued tokens from supply without carrying the replacement debt understates liability; retaining both overstates it. Removing lost-key or custodied units because they are not actively trading also understates it. “Circulating market supply” is not the liability denominator.

**F6 — Priority versus recovery.** Draft seniority over surplus does not establish priority over secured or statutory claims, nor give a queue temporal priority. Face, priority, due date and recoverability must remain distinct fields. No actual waterfall is inferred.

**F7 — Impairment mistaken for debt relief.** A calculable frozen reference is not preservation of purchasing power. No Q023 remedy, true-up debt or fallback index is smuggled into the model; the production-activation blocker persists. Actual externally arising claims cannot be dismissed merely because no protocol remedy is approved.

**F8 — Replay identity and rounding.** Reusing a claim identifier after cancellation can confuse history; duplicate settlement messages can double discharge; rounding small residuals can erase debt. The model reserves historical claim IDs, rejects conflicting event reuse and retains exact fractions. Production token/payment precision and authenticated ordering remain unproven dependencies.

**F9 — Multiple-version aggregation.** Summing all units and multiplying by one target understates or overstates mixed-version claims. Separate version/perimeter valuations are mandatory. Legal consolidation, cross-guarantees and bridge elimination need explicit evidence; this package selects none.

No new Claude review is claimed. These are operator adversarial checks, not independent economic validation. [Executable checks](test_liability_model.py) and [results](liability-validation.json) test the stated accounting invariants; unresolved evidence/architecture issues remain open even when tests pass.
