# TIPS Reference CPI Compatibility Analysis

Source-backed facts: Treasury's rule uses M−3 CPI at month start and linear daily interpolation toward M−2; its example for April 15, 1996 uses 154.40 and 154.90 to obtain 154.63333 after Treasury rounding. Treasury retains unrevised CPI, prefers original-base publication, estimates missing values using prior twelve-month change, and reserves successor discretion. [31 CFR 356, Appendix B I.B.3–4](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-II/subchapter-A/part-356).

| Feature | PPU proposal | Matching consequence |
|---|---|---|
| M−3 start and M−2 daily interpolation | Adopt in normal operation | Same unrounded index path if vintages/base agree |
| Truncate six then round five, and rounded ratio | Reject; exact arithmetic then 18 places | Small systematic convention differences; not literally identical ratios |
| Previously reported vintage | Retain first edition, explicit evidence and correction hold | Normal alignment; review holds can add basis |
| Missing-month estimate | Reject; carry committed endpoint | Potentially material contingency basis |
| Successor discretion | Reject automatic inheritance | Future index divergence possible |
| Original-base preference | Adapt with exact evidence rules | Approximate rounded conversions can fail admission |
| TIPS original-principal maturity protection | Do not adopt for PPU target | PPU may decline below $1; instrument floor is not target symmetry |

Treasury announced 325.604 for missing October 2025. PPU's analogous January 2026 starting endpoint would be September 324.800 if December's missing endpoint froze. Difference at January 1: (325.604−324.800)/324.800 = about 0.24754% of that carried level. This is a comparison of *contractual conventions*, not proof of October's true inflation. January PPU would interpolate toward November 324.122 if eligible; Treasury would interpolate from 325.604 toward 324.122. [Treasury announcement](https://home.treasury.gov/news/press-releases/sb0324), [BLS historical table](https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm).

Same underlying CPI does not hedge the price at which bonds can be liquidated or instant redemption claims. Duration, maturity, coupons, floor value, timing and liquidity remain WP1D/Phase 2. This paper selects no reserve asset, allocation, duration, derivative or funding commitment. The recommendation sacrifices exact contingency matching for no PPU-created forecast; R021 remains open.

The October-gap *reference-level* difference is transient if November is admitted normally: both paths reach November324.122 on February1,2026. It is not a permanent multiplicative drift because PPU moves to an absolute index level rather than compounds an invented growth rate. Prior cash-flow differences and tracking shortfalls are not reversed by later reconvergence. Other correction holds, successors and differing I0 vintages can still produce persistent basis.

Independent expanded vector: all31 May2026 published Treasury Reference CPI rows reproduced to five places through the replay model using January325.252, February326.785 and March330.213. [Official PDF](https://www.treasurydirect.gov/instit/annceresult/tipscpi/2026/CPI_20260410.pdf); archived evidence and extracted fixture included. This checks the reference path, not full security-specific ratios, principal floors, asset prices or proof of each original BLS publication.
