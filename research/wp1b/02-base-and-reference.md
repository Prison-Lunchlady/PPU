# Base-Date and Reference-Index Specification

Status: proposed configuration requirements, not an activation decision.

Choose G as a future Gregorian month start at 00:00:00 UTC only after all required later reviews. Fix B=1 USD and I0=original first-release CUUR0000SA0 for G−3 on its original 1982–1984 base, or an exactly normalized equivalent. Require both G−3 and G−2 authenticated, positive, unambiguous and admitted before G−24 hours; no active review hold. Otherwise do not activate. The version's signed configuration must identify G, I0, evidence hashes, original editions, normalization map, arithmetic convention and observation-path identities. No reset of I0 after inflation, deflation or rebasing.

Illustration only: G=2026-04-01T00:00:00Z, synthetic January CPI=300 and February=303. I0=300; April 1 T=1; April 16 T=1.005; May 1 T=1.01. These are synthetic, not actual 2026 CPI observations or a historical launch.

The CPI published base (1982–1984=100) and the PPU base date are different concepts. A 300 CPI level does not mean 300 dollars per PPU. Numerator and denominator must use the same normalization. Monthly-average source prices cannot establish the exact purchasing power on G; G defines contractual $1 reference value, not a surveyed spot basket on that day.

Alternative rejected: choosing today's date while writing this report. It would manufacture a launch commitment, incomplete vintage evidence and an intramonth base complication. A future date is an explicit required parameter, not a missing formula variable. Dates before G return NOT_ACTIVE.
