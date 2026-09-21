# WP1B Required Question Coverage

Answers are the recommendation in 01 unless labeled fact or unresolved. None is Gate1B approval.

1. **Formula:** T=halfEven18([S+(d−1)(E−S)/D]/I0) USD; S=prior committed E; E=eligible expected M−2 first CPI or S. Explicit NOT_ACTIVE/UNREPRESENTABLE exceptions. 01.
2. **Base Date:** future configured month-start G at00UTC, not selected as a live date here. 02.
3. **Base Reference Index:** authenticated original normalized CPI(G−3), fixed permanently. 02.
4. **Controlling observation:** normally M−3 to M−2; after gap start=prior committed endpoint, endpoint still expected M−2 if eligible. 01/07.
5. **Step or daily:** recommend daily under finality/matching priority; monthly and release steps evaluated as credible alternatives. 03.
6. **Interpolation:** exact day fraction(d−1)/D, constant intraday. 01.
7. **TIPS:** adapt normal formula, reject wholesale copying of forecast, replacement power, rounding and instrument floor. 04.
8. **Lag:** three-month reference label, roughly2.5-month weighted midpoint age under approximation, plus input ages; outages unbounded. Fact/interpretation separated in05.
9. **Acceptability:** conditional design judgment, not established user demand; Q021 OPEN. Reopen benchmark if unacceptable. 05.
10. **Deflation:** negative slopes and sub-$1 references permitted. 08.
11. **Floor:** none. 08.
12. **Consequences:** nominal loss possible; no individual price guarantee; later liability-fixation time matters. 08.
13. **Missing:** endpoint carry, FROZEN, issuanceDataOK=false; no imputation. 07.
14. **Delay:** if admission strictly before cutoff qualifies; otherwise month frozen, no late rewrite. 07/10.
15. **Correction/restatement:** preserve first vintage/history; relevant authenticated correction opens prospective review hold and immediate health block. 06.
16. **Retroactivity:** prohibited; technical finality assurance remains prerequisite. 06.
17. **Binding time:** plan commits at month-start−24h; first new endpoint contribution at second day00UTC; each day's value at00UTC. 10.
18. **Timezone:** UTC Gregorian/POSIX, no DST; release clocks converted separately. 01/10.
19. **Precision:** exact rational intermediate;18-place binding target;6-place display rounded independently. 01.
20. **Rounding:** nearest ties-to-even, once from exact target; no Treasury double-round. 01/12.
21. **Stale:** committed value survives, missing next input freezes; daily monitor age≥24h blocks necessary issuance flag. 07/10.
22. **Conflict:** unresolved authenticated original-edition contradiction blocks admission; no favorable-value/majority selection. 10.
23. **Material redefinition:** hold first uncommitted plan; detection/classification requires fallible institutional evidence. 09.
24. **Rebase:** prefer old base, else exact official equivalence factor; never reset I0; uncertain mapping holds. 09.
25. **Discontinued:** freeze, disclose failure of ongoing purchasing-power coverage, seek primary review. 09.
26. **Successor:** official successor first review candidate, no automatic substitution; alternatives require benchmark reconsideration. 09.
27. **Mechanical:** calendar/arithmetic/cutoffs/equality/freshness/carry/exact rescaling/counters. 09.
28. **Human:** source authenticity and path independence, materiality/equivalence classification, future terms/approval. 09/10.
29. **Constrained powers:** evidence7days, proposal30days, hold on missed deadlines, prospective original-terms-only clearance, no forced successor. Sufficient institutional/legal enforcement NOT demonstrated; WP1G/Phase3. 09.
30. **Promise consistency:** supports an explicitly delayed, vintage-fixed reference, not uninterrupted/current/global protection. Conditional consistency; reopen Gate1A if that qualification or necessary authority is unacceptable. 01/05/09.

Every research-scope item maps to these answers and 01–12. Required deliverable13 is reference_model.py plus EVENT_RULES and tests;14 is the separate amendment proposal;15 comprises updated canonical registers;16/17 are completion and Gate submission. The roadmap and original draft remain unchanged.

v0.2 controlling refinement for answers21–30:17adds typed rejection/derived holds, rolling impairment alarm, canonical artifact keys/scoped resolution and concept-based materiality. Answer30 now explicitly recommends primary reopening of Gate1A promise wording for indefinite/no-makeup/human-hold qualifications if target accepted. This is a recommendation only.

