# Formal PPU Target Calculation Specification

> **Revision 0.3 controls impairment policy.** Primary disposition: REVISION REQUIRED. Revised submission awaits primary review; no Gate 1B approval. [Benchmark Impairment Policy](18-benchmark-impairment-policy.md) supersedes earlier indefinite-freeze recommendations and impairment-clearance shorthand. The public interface for this proposal is `replay_with_impairment` in [impairment_policy.py](impairment_policy.py), wrapping the unchanged arithmetic model. Other mechanics remain conditional proposals; WP1C is unauthorized.


WP1B candidate v0.2, 2026-09-19. **RECOMMENDATION — NOT APPROVED.** Gate 1A approved only the underlying benchmark. This specification defines a reference value, not market price, an unconditional redemption guarantee, or a reserve design. [Review clarifications](17-review-clarifications.md) form part of this specification and control any earlier ambiguity.

**Proposed prominent promise qualification requiring explicit primary acceptance:** PPU uses a delayed, first-release-vintage CPI-U reference. Its contractual reference may stop tracking CPI indefinitely when data or delivery are unavailable or contested, or an index review hold remains unresolved, even while BLS publishes normally. Prior values and elapsed coverage gaps receive no retroactive makeup. Narrow human judgments concerning corrections, material changes and successor compatibility can delay resumption. Nominal values can fall below $1. This qualification is not already approved by Gate1A. Recommend reopening Gate1A's promise wording for this explicit qualification if Gate1B accepts these mechanics; no silent amendment to the accepted benchmark concept.

## Recommendation and controlling order

Adapt the normal TIPS daily interpolation convention, but do not import Treasury's forecasting, successor discretion, nominal maturity floor or intermediate rounding. Publish an immutable monthly schedule in advance. Carry the last committed endpoint forward when an eligible observation cannot be admitted; resume prospectively toward the next eligible observation. Never relabel a carried endpoint as measured CPI.

Decision priority: historical finality and no invented observations first; authentic benchmark identity second; continuity and compatibility with ordinary TIPS indexing third; speed of response last. These are proposed project choices, not statistically established optimal weights. Monthly steps are a serious alternative if the lag fails acceptance. [Comparison](03-method-comparison.md) and [lag](05-publication-lag.md).

## Inputs and identities

Underlying series: BLS CUUR0000SA0, CPI-U, U.S. City Average, All Items, Not Seasonally Adjusted; published reference base 1982–1984=100. The approved promise remains the exact promise in [current Gate 1A authority](../../evidence/gate1a-approval-2026-09-21.txt). The PPU contractual index is a delayed, vintage-fixed transformation of this series, not the current statistical series in all circumstances.

M is a Gregorian calendar month in UTC; d is its calendar day (1 through D); D is its actual number of days. M−k means calendar-month subtraction. B = USD 1 exactly. G is a future first-of-month 00:00:00 UTC base date, configured before activation. **No live G is selected in research.** I0 is the authenticated, normalized first-release CPI for G−3, fixed forever. Initialization also requires eligible G−2 CPI. Without both, activation is undefined and prohibited, not silently assigned $1. See [base specification](02-base-and-reference.md).

For every month M, define cutoff C(M) = first instant of M minus exactly 86,400 POSIX seconds. Only evidence finalized strictly before C(M) counts; an event at the cutoff is late. A monthly plan becomes irrevocable at C(M), even if computed lazily later from the immutable event prefix. There is no privileged optional seal transaction. This avoids a discretionary scheduler withholding an otherwise valid plan. No evidence may be backdated. The value API is defined from a finalized, append-only event log with trustworthy UTC timestamps; establishment of that log is a later technical requirement, not solved by this research model.

Each observation packet records month, series, seasonal status, base, positive exact decimal value, original BLS publication/edition identifier, captured content hashes and URLs, delivery identities, publication time, and finalized admission times. Minimum requirement: two distinct preconfigured delivery paths independently capture matching original BLS evidence before cutoff. They are not independent price measurements. Admission authentication and delivery independence must be proved before implementation; neither web scraping nor a hash alone authenticates BLS. Any unresolved authenticated contradiction about the *same first edition* blocks admission, even if two paths agree. A different official correction edition is handled under the correction policy, not majority voting.

Use the first official released value for each observation, including if an unconsumed value is later corrected. Never select a vintage opportunistically. If the first release cannot be authenticated, that observation is unavailable. Ordinary revisions of other series do not substitute for CUUR0000SA0. Dash, null, zero, negative, NaN, wrong-series, wrong-month, wrong-base, seasonally adjusted and unauthenticated packets are ineligible. A very large *authenticated* positive CPI is not rejected solely because its inflation rate is surprising.

## Formula and monthly state transition

At G: S(G) = I0. Subsequently S(M) = E(M−1), including during recovery or a hold. Let eligible(M) mean that the required first-release observation for M−2 satisfies the packet rules and that no unresolved index review hold is in force in the event prefix at C(M).

E(M) = normalized CPI(M−2) if eligible(M); otherwise E(M) = S(M).

J(M,d) = S(M) + ((d−1)/D) × (E(M)−S(M)).

T(t) = roundHalfEven18(B × J(M,d) / I0), for every instant t on day d in UTC.

No intraday interpolation. Each daily value binds at 00:00:00 UTC and remains binding until the next UTC midnight. The last day uses (D−1)/D; the following month's first day reaches E(M). Thus the month boundary completes one increment of the outgoing plan. During recovery this increment can be much larger than an ordinary inflation-month increment; it is not an economic jump bound. A missing month still completes the preceding committed slope; its own slope is zero. The endpoint is not compounded from rounded targets.

Normal conditions give S(M)=CPI(M−3), E(M)=CPI(M−2), matching Treasury's unrounded mathematical reference path. After a gap, S can be older than M−3: the next eligible endpoint restores the level prospectively over a month, in either direction. No missing CPI is reconstructed; no makeup payments or retroactive values arise. This creates catch-up slopes and temporary basis risk. The normalized next observed level may itself reflect BLS imputations, which PPU cannot remove.

## Arithmetic, time and totality

Parse decimal inputs to exact rational numbers; retain fractions through index normalization, interpolation and division. Final reference target is a decimal with 18 places, ties to even. Human display uses six places independently rounded from the exact rational, and labels the full 18-place value as binding. Do not round to six and then eighteen, use binary floats, copy Treasury's five-place ratio, or round balances here. Token units and transaction payment rounding belong to WP1C/1F and technical design.

Use UTC Gregorian date from POSIX time; all contractual days have 86,400 seconds. A leap second belongs to the same civil date and causes no extra target step. Leap years use 29 February. Ignore local daylight-saving transitions. U.S. release timestamps must be converted using the applicable Eastern offset, not a hard-coded 13:30 UTC.

For t<G return NOT_ACTIVE. For positive inputs the exact rational remains positive; rounding can theoretically yield zero at extreme deflation. If rounded output is zero, return UNREPRESENTABLE with the exact rational and issuance-blocked status; never invent a floor. A bounded implementation must similarly detect overflow and fail closed rather than wrap or clamp. Supported numeric bounds must be demonstrated in Phase 4. These states prevent falsely promising a numeric decimal at every conceivable input.

## Data health and conservative behavior

Return a tuple: binding target (or explicit nonactive/unrepresentable state), plan mode, source observation month, fixed vintage IDs, cutoff, event-prefix hash, and data-health status. Modes are NORMAL, CATCH_UP or FROZEN. NORMAL means the start and endpoint correspond to consecutive expected observation months; a recovery month is CATCH_UP even when the numerical difference is zero.

The target is not a freshness assertion. A precommitted path continues during an intramonth communications outage. Define a necessary `issuanceDataOK` flag: true only in NORMAL mode, with no unresolved review hold or authenticated conflict, and at least two fresh monitoring attestations finalized strictly before the query instant, each younger than 86,400 seconds. Monitor attestations cover the expected release status, BLS notices/errata, series identity and path availability; their truth remains a trust assumption. At age exactly 86,400 seconds they are stale. An authenticated adverse event makes the flag false immediately upon finalization. FROZEN and CATCH_UP always return false. Restoration requires a NORMAL plan and fresh clean evidence, plus any required review-hold clearance. This is a necessary restriction, never sufficient authority to mint.

Delayed release alone before cutoff does not change the current precommitted target. A missed advertised publication, path failure or unresolved discrepancy must be recorded and block the health flag until resolved; calendar announcements must be archived, and a later calendar amendment cannot erase the missed-deadline history. The quantitative function does not depend on interpreting that calendar. This monitoring interface requires implementation and adversarial assurance later.

## Corrections, changes, holds and finality

Official correction of an admitted/committed observation triggers INDEX_REVIEW_HOLD on authenticated receipt. All committed plans and historical targets stay fixed. Every not-yet-committed plan freezes until an explicit, documented prospective disposition clears the hold. First-edition observations remain locked even after clearance. An official correction before first use is also disclosed and held for review; no known correction is silently ignored. Authenticity disputes hold admission rather than pick a favorable number.

Ordinary methodological maintenance explicitly within the existing CPI-U framework (routine expenditure weights, sample rotation, quality adjustments) is inherited and disclosed. A change in the target population or expenditure concept, index formula framework, publication identity, or an official fundamental redefinition triggers review hold; sampled coverage changes alone are not concept changes (17). Distinguishing a technical improvement from a substantive scope change is not fully algorithmic: authenticated notice plus reasoned classification is required and can be wrong or late. An unrecognized change may enter the target; disclose this residual institutional risk.

A pure base rescaling can be normalized mechanically only when official evidence establishes an exact conversion on the same economic series. Prefer continued old-base publication. Otherwise require documented official conversion K into the original base, fixed prospectively; normalized value = new-base value × K. Do not infer K from a single pair of rounded observations. If exact equivalence cannot be established, hold. Existing plans and I0 never change.

Discontinuation or substantive successor: freeze not-yet-committed plans. No automatic move to CPI-W, C-CPI-U, PCE, private indexes, Treasury estimates or an official successor merely because it is official. A successor requires primary/Brad review of concept equivalence, mapping, public overlap, impact and prospective notice, with Gate 1A reopening if scope changes. Existing protected terms and voluntary-migration tension remain Q011; WP1B grants no administrator power to rewrite them.

Temporary absence alone permits automatic prospective resumption to the next expected observation. Three consecutive frozen plans trigger mandatory BENCHMARK_REASSESSMENT_REQUIRED disclosure and primary review request; no permission to select another index or unlimited emergency amendment arises. The disclosure persists until review records a disposition, even if normal observations resume. The target may stay frozen indefinitely; inflation preservation does not continue during that condition.

Index review must publish reasons and evidence within seven calendar days of the hold, and a proposed disposition within thirty; missed deadlines keep the hold and escalate disclosure. These deadlines do not force approval or empower anyone to replace the index. Hold clearance is a narrow prospective decision requiring demonstrated return to the same benchmark/first-vintage policy; any altered terms require a separately authorized version and review. Authority implementation, abuse resistance and coexistence remain WP1G dependencies.

## Limits of the recommendation

Deterministic conditional on a canonical log, configuration and validated event facts; not deterministic discovery of truth or governance judgments. This model does not establish oracle security, chain finality, legal enforceability, solvency or actual execution during downtime. Reference value can be reconstructed while transfers cannot execute. A future transaction must use its actual finalized contractual time, never a user's chosen pre-downtime timestamp; liability timing belongs to WP1C/1F.

Gate 1A remains defensible only with the disclosed delayed/vintage-fixed transformation and explicit failure states. An uninterrupted contemporaneous purchasing-power guarantee is not supported. Reject this recommendation and reopen Gate 1A if that stronger promise is required, if lag is unacceptable, or if constrained contingency authority cannot be reconciled with protected terms. No target mechanics are accepted until Gate 1B approval.

## Current repository submission — 2026-09-21

Reconciled under [SRC016](../../evidence/gate1a-approval-2026-09-21.txt); the exact approved standard is in [Protocol State](../../docs/canonical/01-protocol-state.md). The prior dated research is reused with its limitations and review history; no new Claude review or primary endorsement is claimed. See [current reconciliation and validation](../../reviews/gate1b/current-reconciliation.md). All target mechanics remain proposed; Treasury contingency conflict remains OPEN. No oracle, minting, reserve or governance architecture is approved by the research interface examples.
