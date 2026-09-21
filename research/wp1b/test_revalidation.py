"""Additional independent invariants for the September 21 reconciliation."""
from datetime import timedelta
from fractions import Fraction as F
from pathlib import Path
import json
from reference_model import Plan, value, first, rounded, replay, Packet, shift, cutoff

checks={}
for month in ['2024-02','2025-02','2026-04','2026-05']:
    start=F('324.800');end=F('324.122')
    p=Plan(month,start,end,shift(month,-2),'NORMAL',0,'ELIGIBLE')
    days=(first(shift(month,1))-first(month)).days
    got=[F(value(p,first(month)+timedelta(days=d),start)['exact']) for d in range(days)]
    checks[month+'_daily_slope_and_endpoint']=all(got[d]-got[d-1]==(end-start)/start/days for d in range(1,days)) and got[-1]+(end-start)/start/days==end/start
    checks[month+'_no_intraday_change']=value(p,first(month)+timedelta(hours=23,minutes=59),start)==value(p,first(month),start)

def packets(month,val):
    t=first(shift(month,1))+timedelta(days=15)
    return [Packet(month,str(val),'original',path,t,t-timedelta(hours=1),release_hash='a'*64,source_url='https://example.invalid/synthetic') for path in ['A','B']]
ps=packets('2026-01',300)+packets('2026-02',303)+packets('2026-03',306)
at=first('2026-05')+timedelta(days=14)
checks['input_order_invariance']=replay('2026-04',at,ps)==replay('2026-04',at,list(reversed(ps)))
checks['future_packets_do_not_rewrite_prior_target']=replay('2026-04',at,ps)==replay('2026-04',at,ps+packets('2026-06',330))
checks['actual_2025_substitute_basis']=rounded((F('325.604')-F('324.800'))/F('324.800')*100,5)=='0.24754'
checks['absence_never_activates']=replay('2026-04',at,[])['status']=='NOT_ACTIVE'
report={'date':'2026-09-21','scope':'additional independent arithmetic and causal invariants; not production certification','checks':checks,'passed':sum(checks.values()),'failed':[k for k,v in checks.items() if not v]}
Path(__file__).with_name('revalidation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
assert all(checks.values())
