# Adversarial Scenario Matrix

All outcomes are proposed behavior under validated event inputs, not observed performance of a deployed system. `issuanceDataOK` is a necessary restriction only. [Executable cases and results](model-validation.json).

| Case | Trigger and exact quantitative behavior | Data/issuance result | Remaining discretion / limitation |
|---|---|---|---|
| A — Normal | Two authenticated timely paths for M−2; E=CPI(M−2), S=prior E; daily fraction (d−1)/D | NORMAL; health flag only if fresh and no adverse event | Authenticity and monitoring infrastructure, not value selection |
| B — High inflation | 300→330→363→399.3→439.23; no slope cap; April midpoint=1.05, next start=1.10 | Normal source health does not prove solvency | Later reserve/capital stress; no power to suppress true inflation |
| C — Deflation | 300→294→288 gives endpoint targets .98 then .96 | Same rules as inflation, no floor | Liability fixation timing later; no holder-specific preservation |
| D — Missing October analogue | December starts September324.800 and freezes endpoint there; January moves toward November324.122 | FROZEN then CATCH_UP; both data flags false | No estimate of missing October; BLS later imputation remains institutional exposure |
| E — Delayed publication | February observation received March31 00:00 UTC misses April cutoff exactly; April E=S; arrival before cutoff by one microsecond qualifies | Late data cannot restore April eligibility | Delivery censorship can force conservative freeze |
| F — Official correction | Used February303 corrected to302 after April commitment; old April16 stays1.005; next uncommitted endpoint carries303 | Immediate health block and INDEX_REVIEW_HOLD | Transparent prospective clearance required, no retroactive substitution |
| G — Multiple-month outage | May–July unavailable: endpoint stays303 for each month; frozen counter=3 | Reassessment disclosure latched; no new issuance data approval | Review cannot invent CPI; coverage can fail indefinitely |
| H — Material same-ID method change | On authenticated classification, preserve committed plan, freeze first uncommitted and later plans | Review hold | Materiality detection/classification human and fallible; no automatic redefinition |
| I — Official successor | Old series discontinued; no successor admission; hold carry at303 in fixture | Review hold, no auto-clear by publishing new series | Scope/mapping/protected-term compatibility requires primary review; reopen Gate1A if needed |
| J — Oracle disagreement | Two authenticated paths say303, third credible first-edition claim304: no eligible observation | FROZEN; health conflict block | Authentication and resolution; no majority chosen for liability advantage; denial-of-service risk |
| K — Chain/oracle downtime | Precommitted April20 remains3019/3000; source publication before cutoff but receipt at/after cutoff freezes new month | Stale attestations block health; no backdating | Mathematical value available does not mean transfer execution available |
| L — Bad one-feed input | Unauthenticated999999 quarantined; two good303 paths govern; two authenticated999999 reports are not clipped by an inflation cap | Spoof need not block valid observation; authenticated contradiction does | Correlated compromise can defeat paths; authenticity assumption remains |

Boundary tests additionally cover 28/29/30/31-day months, leap day, UTC offsets, half-even ties, exact rebase equivalence, failed base equivalence, invalid values, failed genesis, and conservative health restoration. Cases H/I/F explicitly supply a validated review-hold fact: the executable test does not certify human materiality judgments or real authentication.

v0.2 validation update: all A–L also pass through the public replay interface from valid genesis; earlier isolated-helper cases remain labeled unit tests. Correction and official normalization holds are derived from packets; materiality/successor classifications remain validated control-event inputs. A second rolling impairment trigger and scoped publisher-artifact conflict resolution are specified in17.

