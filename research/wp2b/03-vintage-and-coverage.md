# WP2B Vintage, Missing-Data and Coverage Policy

Date: 2026-09-30.

1. Preserve native observations. No automatic forward fill, backfill, interpolation, or weekend fabrication.
2. BLS CPI annual-average M13 rows are excluded from the monthly PPU benchmark path.
3. Current BLS CUUR0000SA0 history is tagged current-published history, not a complete archive of first-release vintages.
4. Current H.15/FRED histories may reflect source corrections or revisions. Every machine pull must record retrieval time and source-payload hash.
5. Chicago Fed states NFCI history can change because of incoming data, source revisions, and changing estimated weights. Current-vintage NFCI cannot be represented as contemporaneously known stress information without vintage evidence.
6. Observed TIPS real-yield histories do not exist for the 1970s, 1987, or the early dot-com era. No pre-TIPS real-yield backfill may be described as observed data.
7. SOFR is modern-era only. Earlier funding conditions require another sourced proxy and must not be labeled SOFR.
8. Alternative assets unavailable in a historical period remain unavailable in the observed-asset branch. Projecting a modern asset backward is permitted only as an explicitly counterfactual WP2C branch.
9. Source correction in the research environment does not imply retroactive rewriting of historical PPU obligations; WP1B target-finality rules remain separate.

## Stress-test branch rule

WP2C must separate:
- observed-available-asset history;
- explicitly counterfactual modern-reserve history; and
- protocol-faithful first-release CPI-vintage history when that evidence is available.

A seamless all-era portfolio that silently assumes modern TIPS, SOFR, Bitcoin, or revised data existed in earlier crises is prohibited.

## Newly opened data questions

**Q033 — First-release CPI history.** What auditable source reconstructs monthly first-release CUUR0000SA0 values across all stress eras so WP2C can mirror WP1B's fixed-first-release rule?

**Q034 — Redistributable alternative-asset history.** Which gold, equity, Bitcoin, commodity, energy and liquidity datasets may be versioned publicly with sufficient provenance and license clarity?

Q023 remains the monetary production-activation blocker and is not altered by these data questions.
