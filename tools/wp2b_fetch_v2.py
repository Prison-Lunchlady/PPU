#!/usr/bin/env python3
import csv, datetime as dt, hashlib, io, json, math, pathlib, time, urllib.parse, urllib.request

OUT = pathlib.Path("research/wp2b/data")
REV = pathlib.Path("reviews/wp2b")

# Stable research metadata plus deliberately conservative coverage guards.
# expected_start_on_or_before is a guard against left-truncation, not a claim
# that every series must begin on that exact calendar date.
SER = {
    "CPIAUCNS": dict(key="cpi_u_nsa", unit="index_1982_1984_equals_100", freq="monthly", agency="BLS",
                     start="1913-01-01", expected_start_on_or_before="1913-02-01", min_rows=1300, max_stale_days=75),
    "DTB3": dict(key="treasury_3m_discount", unit="percent_discount_basis", freq="daily_business", agency="Federal Reserve Board",
                 start="1954-01-01", expected_start_on_or_before="1954-02-01", min_rows=12000, max_stale_days=14),
    "DGS5": dict(key="treasury_5y_nominal", unit="percent", freq="daily_business", agency="Federal Reserve Board",
                 start="1962-01-01", expected_start_on_or_before="1962-02-01", min_rows=12000, max_stale_days=14),
    "DGS10": dict(key="treasury_10y_nominal", unit="percent", freq="daily_business", agency="Federal Reserve Board",
                  start="1962-01-01", expected_start_on_or_before="1962-02-01", min_rows=12000, max_stale_days=14),
    "DFII5": dict(key="tips_5y_real_yield", unit="percent", freq="daily_business", agency="Federal Reserve Board",
                  start="2003-01-01", expected_start_on_or_before="2003-02-01", min_rows=4000, max_stale_days=14),
    "DFII10": dict(key="tips_10y_real_yield", unit="percent", freq="daily_business", agency="Federal Reserve Board",
                   start="2003-01-01", expected_start_on_or_before="2003-02-01", min_rows=4000, max_stale_days=14),
    "DFF": dict(key="effective_federal_funds_rate", unit="percent", freq="daily", agency="Federal Reserve Board / New York Fed",
                start="1954-07-01", expected_start_on_or_before="1954-08-01", min_rows=15000, max_stale_days=14),
    "SOFR": dict(key="sofr", unit="percent", freq="daily_business", agency="New York Fed",
                 start="2018-04-01", expected_start_on_or_before="2018-05-01", min_rows=1500, max_stale_days=14),
    "STLFSI4": dict(key="stl_fed_financial_stress_index", unit="index", freq="weekly", agency="St. Louis Fed",
                    start="1993-12-01", expected_start_on_or_before="1994-02-01", min_rows=1200, max_stale_days=21),
    "DCOILWTICO": dict(key="wti_cushing_spot", unit="dollars_per_barrel", freq="daily_business", agency="EIA",
                       start="1986-01-01", expected_start_on_or_before="1986-02-01", min_rows=7000, max_stale_days=21),
}

def parse_date(s):
    return dt.date.fromisoformat(s)

def chunk_ranges(start, end, years=5):
    cur = start
    while cur <= end:
        try:
            nxt = cur.replace(year=cur.year + years)
        except ValueError:
            nxt = cur.replace(month=2, day=28, year=cur.year + years)
        stop = min(end, nxt - dt.timedelta(days=1))
        yield cur, stop
        cur = stop + dt.timedelta(days=1)

def fetch_chunk(sid, start, end):
    params = urllib.parse.urlencode({"id": sid, "cosd": start.isoformat(), "coed": end.isoformat()})
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?" + params
    last = None
    for attempt in range(4):
        req = urllib.request.Request(url, headers={
            "User-Agent": "PPU-WP2B-research/0.4",
            "Accept": "text/csv,text/plain;q=0.9,*/*;q=0.1",
        })
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read()
                if not raw:
                    raise RuntimeError("empty payload")
                return url, r.geturl(), r.headers.get("Content-Type", ""), raw
        except Exception as exc:
            last = exc
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    raise last

def parse_csv(raw, sid):
    text = raw.decode("utf-8", errors="strict")
    rdr = csv.DictReader(io.StringIO(text))
    if not rdr.fieldnames or sid not in rdr.fieldnames:
        raise RuntimeError(f"{sid}: unexpected CSV header {rdr.fieldnames}")
    date_col = "observation_date" if "observation_date" in rdr.fieldnames else ("DATE" if "DATE" in rdr.fieldnames else rdr.fieldnames[0])
    out = []
    missing = 0
    for row in rdr:
        d = (row.get(date_col) or "").strip()
        v = (row.get(sid) or "").strip()
        if not d:
            continue
        # Validate date whether value exists or is missing.
        parse_date(d)
        if v in ("", "."):
            missing += 1
            continue
        x = float(v)
        if not math.isfinite(x):
            raise RuntimeError(f"{sid}: non-finite value on {d}")
        out.append((d, v))
    return out, missing

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    REV.mkdir(parents=True, exist_ok=True)
    now_dt = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    now = now_dt.isoformat()
    today = now_dt.date()
    rows = []
    prov = {}
    validation = {
        "retrieved_utc": now,
        "passed": True,
        "retrieval_path": "fred_graph_csv_date_bounded_chunks",
        "series": {},
        "global_checks": {},
        "limitations": [
            "CPI is current-published, not a complete first-release-vintage archive.",
            "Yields are not bond total returns.",
            "No unavailable historical TIPS or SOFR observations are backfilled.",
            "License-unclear alternative market histories are not vendored.",
        ],
    }

    for sid, meta in SER.items():
        start = parse_date(meta["start"])
        seen = {}
        chunks = []
        missing_total = 0
        for cstart, cend in chunk_ranges(start, today, years=5):
            req, final, ctype, raw = fetch_chunk(sid, cstart, cend)
            sha = hashlib.sha256(raw).hexdigest()
            obs, missing = parse_csv(raw, sid)
            missing_total += missing
            for d, v in obs:
                old = seen.get(d)
                if old is not None and old != v:
                    raise RuntimeError(f"{sid}: conflicting duplicate for {d}: {old} vs {v}")
                seen[d] = v
            chunks.append({
                "requested_url": req,
                "final_url": final,
                "chunk_start": cstart.isoformat(),
                "chunk_end": cend.isoformat(),
                "content_type": ctype,
                "payload_bytes": len(raw),
                "payload_sha256": sha,
                "numeric_rows": len(obs),
                "missing_markers_excluded": missing,
            })

        if not seen:
            raise RuntimeError(f"{sid}: no numeric observations")
        obs = sorted(seen.items())
        dates = [parse_date(d) for d, _ in obs]
        actual_start, actual_end = dates[0], dates[-1]
        expected_start = parse_date(meta["expected_start_on_or_before"])
        staleness_days = (today - actual_end).days
        guards = {
            "start_date_guard": actual_start <= expected_start,
            "minimum_rows_guard": len(obs) >= meta["min_rows"],
            "end_date_staleness_guard": staleness_days <= meta["max_stale_days"],
        }
        coverage_passed = all(guards.values())
        validation["series"][sid] = {
            "rows": len(obs),
            "source_missing_markers_excluded": missing_total,
            "start": actual_start.isoformat(),
            "end": actual_end.isoformat(),
            "staleness_days": staleness_days,
            "expected_start_on_or_before": meta["expected_start_on_or_before"],
            "minimum_rows": meta["min_rows"],
            "max_stale_days": meta["max_stale_days"],
            "guards": guards,
            "coverage_passed": coverage_passed,
            "unique_dates": len(obs) == len(seen),
            "ascending_dates": dates == sorted(dates),
            "fabricated_rows": 0,
            "chunk_count": len(chunks),
        }
        prov[sid] = {
            "series_key": meta["key"],
            "originating_agency": meta["agency"],
            "distributor": "Federal Reserve Bank of St. Louis (FRED)",
            "retrieved_utc": now,
            "vintage_status": "current_published",
            "retrieval_method": "date_bounded_fred_graph_csv",
            "chunks": chunks,
        }
        for d, v in obs:
            rows.append([
                meta["key"], d, v, meta["unit"], meta["freq"], sid, meta["agency"],
                "FRED", "date_bounded_fred_graph_csv", "current_published", now
            ])

    keys = [(r[0], r[1]) for r in rows]
    if len(keys) != len(set(keys)):
        raise RuntimeError("duplicate series/date output")
    rows.sort(key=lambda r: (r[1], r[0]))
    hdr = [
        "series_key", "date", "value", "unit", "frequency", "source_series_id",
        "source_agency", "distributor", "retrieval_method", "vintage_status", "retrieved_utc"
    ]
    panel = OUT / "core-observations.csv"
    with panel.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        w.writerows(rows)
    panel_sha = hashlib.sha256(panel.read_bytes()).hexdigest()

    coverage_all = all(x["coverage_passed"] for x in validation["series"].values())
    validation["global_checks"] = {
        "series_count": len(SER),
        "row_count": len(rows),
        "unique_series_date": len(keys) == len(set(keys)),
        "normalized_panel_sha256": panel_sha,
        "all_series_nonempty": all(x["rows"] > 0 for x in validation["series"].values()),
        "all_fabricated_rows_zero": all(x["fabricated_rows"] == 0 for x in validation["series"].values()),
        "all_coverage_guards_pass": coverage_all,
        "vintage_label": "current_published",
    }
    validation["passed"] = all([
        validation["global_checks"]["unique_series_date"],
        validation["global_checks"]["all_series_nonempty"],
        validation["global_checks"]["all_fabricated_rows_zero"],
        validation["global_checks"]["all_coverage_guards_pass"],
    ])

    (OUT / "source-hashes.json").write_text(
        json.dumps({
            "retrieved_utc": now,
            "normalized_panel_sha256": panel_sha,
            "series": prov,
        }, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (REV / "validation.json").write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# WP2B Acquisition Validation Report",
        "",
        f"Retrieved UTC: {now}",
        f"Normalized panel SHA256: `{panel_sha}`",
        f"Rows: {len(rows)} across {len(SER)} series",
        f"Overall validation passed: **{validation['passed']}**",
        "",
        "| Series | Rows | Start | End | Staleness days | Coverage guards | Missing markers excluded |",
        "|---|---:|---|---|---:|---|---:|",
    ]
    for sid in SER:
        x = validation["series"][sid]
        lines.append(f"| {sid} | {x['rows']} | {x['start']} | {x['end']} | {x['staleness_days']} | {x['coverage_passed']} | {x['source_missing_markers_excluded']} |")
    lines += [
        "",
        "## Acceptance checks",
        "",
        f"- Unique series/date keys: **{validation['global_checks']['unique_series_date']}**",
        f"- All series nonempty: **{validation['global_checks']['all_series_nonempty']}**",
        f"- All per-series coverage guards passed: **{validation['global_checks']['all_coverage_guards_pass']}**",
        "- Fabricated rows recorded: **0**",
        "- Vintage label for this panel: **current_published**",
        "- No forward fill, backfill or interpolation is performed.",
        "- TIPS and SOFR begin only where the official source publishes observations.",
        "- Every date-bounded payload is individually SHA-256 hashed in source-hashes.json.",
        "",
        "## Limits",
        "",
        "- This panel does not reconstruct the first-release CPI vintages required for protocol-faithful WP1B replay; Q033 remains open.",
        "- Yield series are not total-return series.",
        "- Alternative market-price series with unresolved redistribution terms remain omitted.",
        "",
    ]
    (REV / "WP2B-acquisition-validation.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(validation["global_checks"], sort_keys=True))
    if not validation["passed"]:
        failed = {sid: x["guards"] for sid, x in validation["series"].items() if not x["coverage_passed"]}
        raise SystemExit("coverage validation failed: " + json.dumps(failed, sort_keys=True))

if __name__ == "__main__":
    main()
