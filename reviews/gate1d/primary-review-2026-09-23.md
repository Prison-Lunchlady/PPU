# Gate 1D Primary Review — Reserve Architecture

Date: 2026-09-23 America/Chicago
Authority: SRC020 standing daily development authorization
Disposition: **APPROVED WITH CONDITIONS**
WP1D: **COMPLETE**
Next package: **WP1E — Capital Structure, AUTHORIZED FOR THE NEXT DAILY RUN**
Phase Gate 1: **NOT REACHED**

## Scope reviewed

Primary review examined the Gate 1D submission, WP1D completion report, reserve architecture report, eligibility specification, candidate structures, adversarial failure analysis, parameter register, Claude reconciliation and the current canonical handoff.

Independent source spot-checks confirmed the key factual premises used by WP1D: Treasury TIPS are issued in 5-, 10- and 30-year terms and their original-principal floor applies at maturity rather than guaranteeing a secondary-market sale price; Treasury market liquidity deteriorated materially in March 2020 under dealer balance-sheet constraints; TIPS prices can embed material liquidity premia; and Treasury actually invoked its CPI index-contingency provisions after the missing October 2025 CPI observation. These facts support treating liquidity, real-rate exposure, market access and benchmark-contingency basis as real reserve-design risks rather than theoretical edge cases.

The final corrected WP1D core did not receive a fresh Claude stage-4 review because the preserved Claude session returned repeated service-unavailable messages. Three earlier Opus 5 High review stages produced 42 material findings plus an integrity caveat, and those findings were reconciled. No claim of Claude endorsement of the final corrected core is made. The lack of a fresh final Claude pass is not treated as certification and does not waive the conditions below.

## Gate decision

PPU-D018's **candidate reserve architecture and analytical-control framework is accepted for continued research**. This approval does **not** select a production allocation, safe collateral ratio, production haircut, production custodian, legal ownership structure or investable reserve portfolio.

The research establishes a defensible baseline to carry into WP1E and Phase 2:

- conditionally eligible usable USD cash;
- direct Treasury bills;
- controlled short Treasury reverse repo with PPU as cash lender, only where title, collateral, closeout and actual access are verified;
- direct short remaining-duration TIPS as a partial inflation-matching sleeve;
- explicit exception inventory for stale, encumbered, unsettled, disputed or inaccessible positions;
- first-loss capital treated as financing/economic loss absorption, not as an additional reserve asset counted on top of assets it already financed;
- time-horizon liquidity tests based on actual accessible cash against due obligations;
- separate gross, market, stressed, available and recovery quantities;
- no borrowing, rehypothecation, hidden leverage or collateral/debt double counting in the baseline.

## Standing conditions

1. **Candidate only, not production selection.** Cash/bill/repo/short-TIPS eligibility is a research baseline subject to later calibration, legal enforceability, custody, market access and implementation evidence.

2. **No numerical parameter is ratified.** All WP1D weights, 120/100 scale examples, maturity brackets, shocks, liquidity horizons, haircuts, run assumptions, concentration limits and recovery assumptions remain hypotheses or diagnostics unless a later authorized package explicitly validates and adopts them.

3. **Liquidity is liability-deadline specific.** No universal reserve-liquidity percentage may be inferred from WP1D. WP1F must define redemption and settlement timing before a binding liquidity requirement can be selected.

4. **TIPS are not a perfect hedge.** The maturity floor does not guarantee a forced-sale price, short remaining-duration holdings require secondary-market selection, and real-yield/liquidity moves can cause losses despite inflation accretion. Treasury's own 2025 contingency methodology also remains distinct from PPU's accepted benchmark-impairment treatment.

5. **Persistent negative net real carry remains a structural funding problem.** A finite starting buffer cannot by itself prove long-run solvency. WP1E must explicitly analyze who supplies first-loss capital, expected compensation, expense drag, replenishment and recapitalization without double counting contributed capital.

6. **Run resilience is not established.** Positive initial overcollateralization does not prove orderly redemption under sequential forced sales. WP1F and Phase 2 retain responsibility for redemption terms, run dynamics and calibrated stress.

7. **Legal title and access are unresolved.** Custody segregation, setoff, repo closeout, bankruptcy priority and enforceable access remain Phase 3 dependencies. WP1D calculations are conditional on those facts, not substitutes for them.

8. **Alternative assets remain comparators.** Gold, Bitcoin, commodities, equities, tokenized Treasury wrappers, stablecoins and other RWAs are not admitted merely because they improve one synthetic scenario. D004 remains controlling.

9. **Q023 remains an activation blocker.** No benchmark fallback, holder true-up or structural impairment remedy was adopted by WP1D. Reserve liquidity cannot cure a failed monetary benchmark.

10. **No user-demand conclusion.** Q021 remains open. A technically defensible reserve architecture does not prove that programmable/transferable PPU provides sufficient utility versus direct Treasury/TIPS ownership.

## Resulting project state

Gate 1D: **APPROVED WITH CONDITIONS**.
WP1D: **COMPLETE**.
PPU-D018: **ACCEPTED FOR CONTINUED DEVELOPMENT WITH THE CONDITIONS ABOVE**.

Open questions including Q021, Q022, Q023, Q024, Q025, Q026, Q027 and Q028 remain open unless separately closed by their own evidence. Q023 remains a production-activation blocker.

Under SRC020's standing daily process authority, **WP1E — Capital Structure is authorized for the next daily run only**. This review does not start WP1E today. WP1F and all later packages remain unauthorized until the roadmap reaches their transition through the same daily gate process.

WP1E must be allowed to reopen D018 if sustainable first-loss funding cannot support the reserve baseline without hidden subsidy, double counting, economically implausible compensation, unacceptable dilution or insolvency dynamics.
