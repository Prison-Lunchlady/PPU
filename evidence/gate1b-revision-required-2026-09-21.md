# Direct primary-review disposition supplied by Brad — SRC017

2026-09-21. The text below is the current user instruction, not an independently retrieved review transcript.

**Gate 1B primary review disposition: REVISION REQUIRED.**

Do not begin WP1C.

The existing WP1B arithmetic, CPI-U benchmark, fixed-vintage approach, no-floor symmetry, UTC timing, exact arithmetic, historical finality, and conditional daily-interpolation recommendation do not require wholesale redesign.

Before Gate 1B can be approved, perform a narrowly scoped Benchmark Impairment Policy revision.

The current proposal permits the PPU target to remain frozen indefinitely during prolonged source failure or unresolved benchmark review, with no retroactive compensation for purchasing-power loss experienced during the frozen interval. This is a material monetary-design decision and has not yet been sufficiently defended against alternatives.

Compare at minimum:

1. permanent freeze with prospective recovery;
2. finalized historical values plus a deterministic contingent true-up for continuously held claims;
3. a fully precommitted contingency-benchmark mechanism activated only under objectively defined structural benchmark impairment.

For each alternative, analyze:

- inflation and deflation treatment;
- treatment of holders who transact during the impairment;
- liability uncertainty;
- reserve consequences;
- manipulation and governance risk;
- compatibility with Gate 1A;
- historical finality;
- oracle/authentication requirements;
- potential arbitrage;
- and failure modes.

Do not assume a contingency benchmark is superior. Actively attempt to show why each alternative fails.

Also distinguish temporary data failure from structural benchmark impairment and define an explicit `BENCHMARK_IMPAIRED` state or equivalent if justified.

Preserve the Treasury contingency conflict as OPEN. Do not automatically adopt Treasury substitution methodology.

Update the relevant Protocol State, Decision Register, Risk Register, Active Hypotheses, Unresolved Questions, WP1B specification, and Gate 1B submission.

Rerun all existing validation and add tests needed for any revised state behavior.

Stop again at Gate 1B for primary review.

**WP1C remains unauthorized.**
