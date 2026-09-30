#!/usr/bin/env python3
import csv,io,urllib.request,hashlib,json,datetime,pathlib
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
def get(s):
 u=f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}"
 req=urllib.request.Request(u,headers={"User-Agent":"PPU-WP2B-research/0.2"})
 with urllib.request.urlopen(req,timeout=90) as r: return u,r.read()
def main():
 OUT.mkdir(parents=True,exist_ok=True); REV.mkdir(parents=True,exist_ok=True)
 now=datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
 rows=[]; prov={}; val={"retrieved_utc":now,"passed":True,"series":{}}
 for sid,(key,unit,freq,agency) in SER.items():
  url,raw=get(sid); sha=hashlib.sha256(raw).hexdigest()
  rd=csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))); fields=rd.fieldnames or []
  dc="observation_date" if "observation_date" in fields else "DATE"; vc=sid if sid in fields else [x for x in fields if x!=dc][0]
  obs=[]; missing=0
  for r in rd:
   d=(r.get(dc) or "").strip(); v=(r.get(vc) or "").strip()
   if not d: continue
   if v in ("",".","NA","NaN"): missing+=1; continue
   float(v); obs.append((d,v))
  if not obs: raise RuntimeError(f"{sid}: no observations")
  dates=[d for d,_ in obs]
  if dates!=sorted(dates) or len(dates)!=len(set(dates)): raise RuntimeError(f"{sid}: bad dates")
  val["series"][sid]={"rows":len(obs),"missing_excluded":missing,"start":obs[0][0],"end":obs[-1][0],"source_sha256":sha}
  prov[sid]={"series_key":key,"source_url":url,"originating_agency":agency,"distributor":"FRED","retrieved_utc":now,"source_sha256":sha,"vintage_status":"current_published"}
  for d,v in obs: rows.append([key,d,v,unit,freq,sid,agency,"FRED",url,"current_published",now,sha])
 keys=[(r[0],r[1]) for r in rows]
 if len(keys)!=len(set(keys)): raise RuntimeError("duplicate series/date")
 rows.sort(key=lambda r:(r[1],r[0]))
 hdr=["series_key","date","value","unit","frequency","source_series_id","source_agency","distributor","source_url","vintage_status","retrieved_utc","source_sha256"]
 with (OUT/"core-observations.csv").open("w",newline="",encoding="utf-8") as f:
  w=csv.writer(f); w.writerow(hdr); w.writerows(rows)
 (OUT/"source-hashes.json").write_text(json.dumps(prov,indent=2,sort_keys=True)+"\n")
 (REV/"validation.json").write_text(json.dumps(val,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"rows":len(rows),"series":len(SER),"status":"ok"}))
if __name__=="__main__": main()
