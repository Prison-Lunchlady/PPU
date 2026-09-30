#!/usr/bin/env python3
"""WP2B research acquisition contract. Standard-library only."""
import csv, io, urllib.request

BLS_URL="https://download.bls.gov/pub/time.series/cu/cu.data.1.AllItems"
FRED_URL="https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
CORE=["DTB3","DGS5","DGS10","DFII5","DFII10","DFF","SOFR"]

def fetch(url):
    req=urllib.request.Request(url,headers={"User-Agent":"PPU-WP2B-research/0.1"})
    with urllib.request.urlopen(req,timeout=60) as r:
        return r.read()

def main():
    # This file defines reproducible source endpoints. Generated files must retain
    # source IDs, units, native dates, retrieval timestamps and response hashes.
    # Do not forward-fill or fabricate unavailable observations.
    bls=fetch(BLS_URL).decode("utf-8-sig")
    rows=[r for r in csv.DictReader(io.StringIO(bls),delimiter="\t")
          if (r.get("series_id") or "").strip()=="CUUR0000SA0"
          and (r.get("period") or "").strip().startswith("M")
          and (r.get("period") or "").strip()!="M13"]
    assert rows
    for sid in CORE:
        raw=fetch(FRED_URL.format(sid)).decode("utf-8-sig")
        assert list(csv.DictReader(io.StringIO(raw)))
    print("WP2B core source acquisition checks passed")

if __name__=="__main__":
    main()
