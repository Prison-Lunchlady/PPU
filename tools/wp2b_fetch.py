#!/usr/bin/env python3
import csv, datetime as dt, hashlib, html, json, math, pathlib, re, urllib.request
OUT=pathlib.Path("research/wp2b/data"); REV=pathlib.Path("reviews/wp2b")
SER={
"CPIAUCNS":("cpi_u_nsa","index_1982_1984_equals_100","monthly","BLS"),
"DTB3":("treasury_3m_discount","percent_discount_basis","daily_business","Federal Reserve Board"),
"DGS5":("treasury_5y_nominal","percent","daily_business","Federal Reserve Board"),
"DGS10":("treasury_10y_nominal","percent","daily_business","Federal Reserve Board"),
"DFII5":("tips_5y_real_yield","percent","daily_business","Federal Reserve Board"),
"DFII10":("tips_10y_real_yield","percent","daily_business","Federal Reserve Board"),
"DFF":("effective_federal_funds_rate","percent","daily","New York Fed"),
"SOFR":("sofr","percent","daily_business","New York Fed"),
"STLFSI4":("stl_fed_financial_stress_index","index","weekly","St. Louis Fed"),
"DCOILWTICO":("wti_cushing_spot","dollars_per_barrel","daily_business","EIA")}
PAT=re.compile(r"(?m)^\s*(\d{4}-\d{2}-\d{2})\s+(\.?|[-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?)\s*$")
def get(sid):
 u=f"https://fred.stlouisfed.org/data/{sid}.txt"
 q=urllib.request.Request(u,headers={"User-Agent":"PPU-WP2B-research/0.3","Accept":"text/plain,text/html;q=0.8,*/*;q=0.1"})
 with urllib.request.urlopen(q,timeout=45) as r: return u,r.geturl(),r.headers.get("Content-Type",""),r.read()
def parse(raw):
 t=raw.decode("utf-8",errors="replace")
 if "<html" in t.lower() or "<table" in t.lower():
  t=re.sub(r"(?is)<(script|style).*?>.*?</\1>"," ",t); t=re.sub(r"(?i)</(tr|p|div|li|h\d|br)>","\n",t); t=re.sub(r"(?s)<[^>]+>"," ",t); t=html.unescape(t); t=re.sub(r"[ \t]+"," ",t)
 out=[]; miss=0; seen=set()
 for m in PAT.finditer(t):
  d,v=m.groups()
  if d in seen: raise RuntimeError(f"duplicate source date {d}")
  seen.add(d)
  if v==".": miss+=1; continue
  if not math.isfinite(float(v)): raise RuntimeError("non-finite")
  out.append((d,v))
 if not out: raise RuntimeError("no numeric observations parsed")
 if [d for d,_ in out]!=sorted(d for d,_ in out): raise RuntimeError("unsorted source")
 return out,miss
def main():
 OUT.mkdir(parents=True,exist_ok=True); REV.mkdir(parents=True,exist_ok=True)
 now=dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(); rows=[]; prov={}; val={"retrieved_utc":now,"passed":True,"retrieval_path":"fred_static_table","series":{},"global_checks":{},"limitations":["CPI is current-published, not a complete first-release-vintage archive.","Yields are not bond total returns.","No unavailable historical TIPS or SOFR observations are backfilled.","License-unclear alternative market histories are not vendored."]}
 for sid,(key,unit,freq,agency) in SER.items():
  req,final,ctype,raw=get(sid); sha=hashlib.sha256(raw).hexdigest(); obs,miss=parse(raw)
  prov[sid]={"series_key":key,"requested_url":req,"final_url":final,"originating_agency":agency,"distributor":"Federal Reserve Bank of St. Louis (FRED)","retrieved_utc":now,"content_type":ctype,"source_payload_bytes":len(raw),"source_sha256":sha,"vintage_status":"current_published"}
  val["series"][sid]={"rows":len(obs),"source_missing_markers_excluded":miss,"start":obs[0][0],"end":obs[-1][0],"source_payload_bytes":len(raw),"source_sha256":sha,"unique_dates":len({d for d,_ in obs})==len(obs),"ascending_dates":[d for d,_ in obs]==sorted(d for d,_ in obs),"fabricated_rows":0}
  for d,v in obs: rows.append([key,d,v,unit,freq,sid,agency,"FRED",req,final,"current_published",now,sha])
 keys=[(r[0],r[1]) for r in rows]
 if len(keys)!=len(set(keys)): raise RuntimeError("duplicate series/date output")
 rows.sort(key=lambda r:(r[1],r[0]))
 hdr=["series_key","date","value","unit","frequency","source_series_id","source_agency","distributor","requested_url","final_url","vintage_status","retrieved_utc","source_sha256"]
 panel=OUT/"core-observations.csv"
 with panel.open("w",newline="",encoding="utf-8") as f:
  w=csv.writer(f); w.writerow(hdr); w.writerows(rows)
 psha=hashlib.sha256(panel.read_bytes()).hexdigest()
 (OUT/"source-hashes.json").write_text(json.dumps({"retrieved_utc":now,"normalized_panel_sha256":psha,"series":prov},indent=2,sort_keys=True)+"\n")
 val["global_checks"]={"series_count":len(SER),"row_count":len(rows),"unique_series_date":len(keys)==len(set(keys)),"normalized_panel_sha256":psha,"all_series_nonempty":all(x["rows"]>0 for x in val["series"].values()),"all_fabricated_rows_zero":all(x["fabricated_rows"]==0 for x in val["series"].values()),"vintage_label":"current_published"}
 (REV/"validation.json").write_text(json.dumps(val,indent=2,sort_keys=True)+"\n")
 lines=["# WP2B Acquisition Validation Report","",f"Retrieved UTC: {now}",f"Normalized panel SHA256: `{psha}`",f"Rows: {len(rows)} across {len(SER)} series","", "| Series | Rows | Start | End | Missing markers excluded | Source SHA256 |","|---|---:|---|---|---:|---|"]
 for sid in SER:
  x=val["series"][sid]; lines.append(f"| {sid} | {x['rows']} | {x['start']} | {x['end']} | {x['source_missing_markers_excluded']} | `{x['source_sha256']}` |")
 lines+=["","## No-fabrication checks","",f"- Unique series/date keys: **{val['global_checks']['unique_series_date']}**",f"- All series nonempty: **{val['global_checks']['all_series_nonempty']}**",f"- Fabricated rows recorded: **0**","- Vintage label for this panel: **current_published**","- No forward fill, backfill or interpolation is performed by the acquisition script.","- TIPS and SOFR begin only where the official source publishes observations.","","## Limits","","- This panel does not reconstruct the first-release CPI vintages required for protocol-faithful WP1B replay; Q033 remains open.","- Yield series are not total-return series.","- Alternative market-price series with unresolved redistribution terms are intentionally omitted.",""]
 (REV/"WP2B-acquisition-validation.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
 print(json.dumps(val["global_checks"],sort_keys=True))
if __name__=="__main__": main()
