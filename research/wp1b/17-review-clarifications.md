# Controlling WP1B v0.2 Clarifications

These amendments are part of the **unapproved** specification. They reconcile independent critique and supersede any inconsistent shorthand in earlier candidate paragraphs. The frozen review input remains unchanged.

## Complete target interface and evidence boundary

`replay(genesis_month, t, packets, control_events, monitor_times, ...)` is the public mathematical reference interface. It initializes only from valid G−3 and G−2 evidence, generates every intervening month, applies event-prefix cutoffs and returns target, mode, source month, vintage keys, cutoff, serialized-input-prefix hash and health. Low-level `plan`, `select` and `value` are helpers; calling a helper with a fabricated state is not activation. The A–L public-interface fixtures all begin with valid initialization. Other unit tests deliberately exercise invalid or isolated helper states.

Times must be timezone-aware and normalized to UTC before date selection. Naive times are rejected. NOT_ACTIVE and UNREPRESENTABLE return no spendable reference; the latter suppresses a misleading zero display. The Python implementation uses unbounded integers, not production arithmetic bounds.

The model accepts validated source/control facts; it does not verify BLS signatures, TLS provenance, monitor truth or institutional independence. URLs/hashes/seasonal/base/path metadata now accompany packets, but first-release status and normalization evidence remain authentication prerequisites. The prefix hash hashes the *research input serialization*, not an actual chain commitment. This is a formal algorithm and test model, not deployed software.

## Canonical identity, parsing and conflict resolution

Canonical edition key = series + observation month + original publication instant in UTC + SHA256 of the designated BLS original release artifact. Friendly labels are ignored. The future configuration must designate the authoritative release artifact format/location and canonicalization convention before activation. Different HTML/PDF representations are delivery attachments to that designated artifact, not competing edition keys. If it cannot be authenticated, no first edition is admitted. That deployment configuration is required rather than arbitrarily chosen here.

CPI grammar is `(0|[1-9][0-9]*)(\.[0-9]+)?`, strictly positive, no whitespace/sign/exponent/fraction/underscore. Do not impose a six-digit inflation cap or permanently assume three decimals. Exact normalization factors may be positive rationals backed by official conversion evidence; they are a different field with different grammar. Configured path identities are closed: new strings never add votes. Tests use synthetic A/B/C identities, not chosen vendors or a live governance membership.

Two agreeing paths admit; one unresolved **authenticated contradictory original-artifact claim** vetoes that observation. This asymmetric fail-closed tradeoff is intentional and can prevent admission indefinitely for that observation. It is not a rule allowing any unsolicited packet to halt the protocol. Authenticity/relevance must be established. Conflict also blocks the data-health flag until resolved. A documented `REJECT_PACKET` event may exclude only a specified packet proved inconsistent with the designated *original publisher artifact* (e.g. parsing/identity error). It may not exclude a valid original merely because BLS later corrected it or because its liability is higher. Exact packet hash, authoritative artifact and reason must be public. Resolution applies only to event prefixes after its receipt; old plans remain final. If original evidence remains contradictory, no value-selection authority is granted.

## Typed causes and hold transitions

| Cause | Numeric effect if no other admissible observation | Prospective resumption / extra action |
|---|---|---|
| SOURCE_ABSENT |Carry endpoint |Automatic next expected usable observation; no invented missing data |
| DELIVERY_INSUFFICIENT |Carry endpoint |Automatic next expected observation after enough configured paths |
| AUTHENTICATION_FAILED / UNCONFIGURED_PATH / INVALID_VALUE / INVALID_PUBLICATION_TIME / ARTIFACT_INCOMPLETE / WRONG_IDENTITY |Reject packet; carry if insufficient valid evidence remains |Valid independent evidence can still admit; record diagnostic; spoof alone has no veto |
| CONFLICT |Carry endpoint; health blocked |Publisher-artifact resolution event, no majority favoring lower liability; future unchanged-source observations can set future numeric plans but unresolved conflict still blocks health |
| NORMALIZATION_UNVERIFIED (authentic official rebase) |Review hold before next commitment |Explicit documented equivalence/old-terms restoration required |
| CORRECTION_EDITION (authentic relevant publisher correction) |Review hold; old vintage retained |Explicit prospective review disposition required |
| INDEX_REVIEW_HOLD (material concept change/discontinuation) |Carry every uncommitted endpoint |Primary disposition under original terms or separately authorized version; no automatic successor |

Relevant means selected national NSA series, and observations from G−3 onward; unrelated regional/SA data and earlier unused history do not open this index hold. Authenticated correction and unverified official normalization packets automatically derive hold events in the replay model. Materiality/discontinuation still enter as separately validated control events because semantic judgment is not mathematical inference. Duplicate evidence of the same correction does not repeatedly reopen a resolved incident. Hold identities are individually resolved; clearing one cannot clear another. At an identical timestamp, OPEN takes precedence over RESOLVE. Events exactly at cutoff cannot alter the committed plan; they can block health immediately.

A review hold skips affected monthly endpoints; the next eligible observed level may incorporate those changes, but the skipped monthly path is never reconstructed. This is intentional finality, not destruction of archived evidence. The tests show a February→April endpoint recovery after a March endpoint was held.

## Chronic impairment and latching

Add a second alarm: three non-NORMAL plans in any trailing six committed plans, alongside three consecutive frozen plans. Both set BENCHMARK_REASSESSMENT_REQUIRED. This catches alternating FROZEN/CATCH_UP operation. The alarm persists after normal data returns; only a subsequent recorded primary disposition clears it. The same continuously active alarm episode does not demand daily reapproval. After its trigger condition clears and later reappears, a new episode relatches. This disclosure does not itself freeze an otherwise eligible endpoint or restore issuance. Three/six is a proposed monitoring policy, not an economic loss bound; see16.

## Method changes and phases

Replace ambiguous “change to population, expenditure coverage” with **change in the target population/expenditure concept**, not a numerical change in sampled coverage or weights within the same urban-consumer concept. Ordinary census-driven sampling refreshes, geographic rotation and reweighting within that concept are inherited. Adding a different population concept, deleting substantive categories, or changing the formula framework triggers review.

The July27,2026 notice's described census-based geographic sample refresh is **provisionally classified as ordinary maintenance on that description**, not preapproval of unknown details. The BLS2016 article on2018's redesign reports approximately87%→94% coverage, illustrating why a coverage percentage alone is insufficient (Claude quoted89%; that number is not adopted here). [BLS primary article](https://www.bls.gov/opub/mlr/2016/article/the-2018-revision-of-the-cpi-geographic-sample.htm).

For a materially changed phased rollout: the notice is logged and assessed when received; once an authenticated material classification is finalized, health blocks immediately and the first not-yet-committed month freezes, even if the announced effective phase is later. A review can clear a precautionary hold prospectively on proof that the original concept continues. This early-hold convention is conservative and can lose coverage before the effective date; it prevents administrators choosing a convenient phase boundary. Routine maintenance needs disclosure, not a multiyear hold. Undisclosed or misclassified changes remain R009/R022.

## Timing and promise implications

Precommitment and update shape are separate choices. A committed daily plan is known from cutoff through its endpoint, about24hours+Ddays; a monthly step is also known in advance. Both create predictable carry. Daily shape lowers the maximum single scheduled step by roughly D for a given change; it does not remove timing incentives or establish economic superiority. If normal TIPS matching is given zero weight, reduced step concentration still favors daily and prompt response/simplicity favor monthly: evidence does not establish a dominant choice. Retain daily only as a conditional recommendation for primary evaluation, with the fully quantified monthly/release alternatives, not as a final selection.

The proposal's data-health flag never changes T(t). Treat its two-path/24hour/recovery restrictions as proposed *necessary interface constraints* for later mint design, not a sufficient mint permission or decision of liability/redemption mechanics. A true flag authorizes nothing by itself. The adverse-event/freshness risk window remains up to24hours of truthful monitoring, not instantaneous detection.

Reopen Gate1A's promise wording for the prominent indefinite-freeze/no-makeup/human-hold qualification in01 if this target candidate is accepted. The same CPI-U benchmark may remain selected. If primary review rejects that qualification, revise/reject this candidate; do not claim Gate1A already authorized it.
