# Candidate Parameters, Assumptions and Rejected Shortcuts

All values here are proposed, not empirically calibrated or approved. Changing them changes the candidate specification and requires new review; they are not discretionary live knobs.

| Parameter | Proposed value and reason | Alternative / sensitivity / residual uncertainty |
|---|---|---|
| Plan cutoff lead |24hours; a full UTC day to make the coming schedule knowable |0h maximizes admission time but removes advance window;48h loses one more day of possible valid input. All three behave identically for normal midmonth releases; late arrivals in the lost interval create an extra frozen month. Choice not operationally validated |
| Monitoring age |Strictly<24hours from two paths; bounded daily evidence burden |12h halves undetected-loss window with twice-daily operations;48h doubles it. No value proves truthful attestations or instant incident detection |
| Admission paths |At least2distinct verified paths, plus no credible unresolved contradiction |One path is a single delivery point; more paths can improve fault evidence but add censorable dependencies. Two is a minimum requirement, not a proven quorum design |
| Arithmetic |Exact rational→18places binding;6display |5-place TIPS ratios trade fidelity for established convention; greater fixed precision does not improve CPI measurement. Integer bounds/transaction rounding later |
| Escalation |3consecutive frozen or3non-NORMAL plans in trailing6; disclosure/review only |1or2 responds sooner;6 tolerates longer failure. None bounds economic loss or authorizes substitution. Threshold is an alarm, not a safety guarantee |
| Review deadlines |7days evidence/reasons,30days proposed disposition |Shorter deadlines may be infeasible; longer permits less accountable holds. Missed deadlines never permit forced substitution. Institutional enforcement pending |
| Correction policy |Hold on any relevant official correction, even before first use |Magnitude threshold risks gaming/materiality discretion; automatic latest-before-cutoff would better statistical fidelity but change Treasury vintage matching; blanket ignore conceals known error. Hold can overreact to tiny benign corrections |
| Recovery |One month to next expected level, then a NORMAL consecutive plan for issuance data eligibility |Immediate step catches up faster but concentrates jump; multi-month cap extends tracking failure and invents cap discretion. No method restores purchasing power during the elapsed gap |

Assumptions A-W1B01–06: an enforceable canonical event log can exist; original BLS editions can be authenticated and archived; path identities are genuinely distinct; monitors report incidents honestly; semantic changes can be classified and reviewed without opportunistic index choice; users/later architecture can tolerate disclosed lag and outages. None is established by the arithmetic/replay checks. Q013/Q014/Q011/Q021/Q022 own the corresponding future evidence.

Explicitly rejected shortcuts: choose lowest feed, accept API-null as0, interpolate across missing data by invented CPI, relabel Treasury substitute as BLS measurement, retroactively insert a late timestamp, silently reset base, cap authenticated inflation, ignore all same-ID methodological changes, treat Claude review as approval, or infer WP1C authority from a completed report.
