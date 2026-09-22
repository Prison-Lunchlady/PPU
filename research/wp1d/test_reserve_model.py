"""Independent expected values, boundary and invariant diagnostics."""
from reserve_model import *
from pathlib import Path
import json
def known_asset(*args,**kwargs):
    assumed=dict(authenticated=True,ownership_verified=True,stale=False)
    assumed.update(kwargs)
    return Asset(*args,**assumed)

checks=[]; failed=[]
def check(name,condition):
    checks.append(name)
    if not condition: failed.append(name)
def rejects(name,fn):
    try: fn()
    except (ValueError,TypeError,ZeroDivisionError): check(name,True)
    else: check(name,False)

check('liability dimensions',liability(80,'1.20',22)==118)
check('indexed versus fixed inflation',liability(100,'1.20',0)-liability(80,'1.20',20)==4)
check('fixed queue deflation burden',liability(80,'.9',20)==92)
check('missing target not zero',liability(80,None,20) is None)
for t in ['0','-1']:
    rejects('invalid target '+t,lambda:liability(1,t,0))
check('18 digit target exact',liability(3,'1.123456789012345678',0)==F('3.370370367037037034'))
check('one year discount manual',zero_coupon_ratio(1,0,'.1')==F(400,441))
check('zero time ratio',zero_coupon_ratio(0,0,'.5')==1)
check('negative yield permitted',zero_coupon_ratio(1,0,'-.01')>1)
for years in ['.5',1,2,5,10]:
    check('no yield change '+str(years),zero_coupon_ratio(years,'.02','.02')==1)
    check('positive rate shock loss '+str(years),zero_coupon_ratio(years,'.02','.05')<1)
    check('negative rate shock gain '+str(years),zero_coupon_ratio(years,'.02','-.01')>1)
for y in ['.01','.03','.05']:
    check('duration loss monotone '+y,zero_coupon_ratio(1,0,y)>zero_coupon_ratio(2,0,y)>zero_coupon_ratio(5,0,y)>zero_coupon_ratio(10,0,y))
rejects('invalid discount base',lambda:zero_coupon_ratio(1,0,-2))
rejects('off grid maturity',lambda:zero_coupon_ratio('.1',0,1))
for bad in [-1,True,0.1]:
    rejects('invalid monetary input '+str(bad),lambda:liability(bad,1,0))

a=[known_asset('cash',20),known_asset('bill',40,24,0,'.99','.01'),known_asset('tips',60,48,0,'.9','.05')]
v=reserve_view(a,24)
check('gross market 120',v['eligible_market']==120)
check('stress value no double loss',v['stressed_realizable']==F('110.504'))
check('liquidity deadline includes bill excludes TIPS',v['horizon_available']==F('59.204'))
check('before deadline excludes bill',reserve_view(a,'23.999')['horizon_available']==20)
check('after deadline includes TIPS',reserve_view(a,48)['horizon_available']==F('110.504'))
check('buffer not second asset',adequacy(v,100)['free_pool_market_buffer']==20)
check('other liabilities counted',adequacy(v,100,[OtherClaim('ops',5)])['free_pool_market_buffer']==15)
check('zero liability ratio undefined',adequacy(v,0)['ratio'] is None)
check('negative buffer retained',adequacy(v,130)['free_pool_market_buffer']==-10)
check('missing liability fail closed',adequacy(v,None)['status']=='LIABILITY_UNDETERMINED')
check('incomplete inventory not coverage proof',adequacy(reserve_view(a,24,inventory_complete=False),100)['status']=='INVENTORY_UNDETERMINED')
for status in ['NORMAL','TEMPORARY_CARRY','BENCHMARK_IMPAIRED']:
    x=adequacy(v,100,benchmark=status)
    check('same face '+status,x['free_pool_market_buffer']==20)
    check('never activates '+status,x['production_activation'] is False)
rejects('invalid benchmark state',lambda:adequacy(v,100,benchmark='FALLBACK'))
for field in ['authenticated','ownership_verified','stale']:
    kw={field: field=='stale'}
    x=reserve_view([known_asset('x',100,**kw)],0)
    check(field+' exclusion',x['eligible_market']==0 and x['exceptions']==['x'] and not x['complete'])
check('partial encumbrance then shock',reserve_view([known_asset('x',100,0,30,'.8',secured_claim_id='s',secured_obligation_usd=30)],0)['stressed_realizable']==56)
check('all encumbered',reserve_view([known_asset('x',100,0,100,secured_claim_id='s',secured_obligation_usd=100)],0)['eligible_market']==0)
check('separate prior claim negative not floored',adequacy(reserve_view([known_asset('x',10)],0),0,[OtherClaim('o',20)])['free_pool_stress_buffer']==-10)
rejects('duplicate identifier',lambda:reserve_view([known_asset('x',1),known_asset('x',1)],0))
rejects('missing identifier',lambda:reserve_view([known_asset('',1)],0))
for kw in [dict(encumbered_usd=101),dict(sale_discount='1.1'),dict(shock_factor=-1),dict(accessible_after_hours=-1)]:
    rejects('bad asset '+str(kw),lambda:reserve_view([known_asset('x',100,**kw)],0))
check('snapshot replay idempotent',reserve_view(a,24)==reserve_view(a,24))
check('order invariant',reserve_view(a,24)==reserve_view(list(reversed(a)),24))
check('new stale state excludes',reserve_view([known_asset('x',100,stale=True)],0)['eligible_market']==0)
check('restored authenticated state includes',reserve_view([known_asset('x',100)],0)['eligible_market']==100)
check('liquidity gap explicit',liquidity_gap(20,30,2)==-12)
check('repo collateral not double asset',repo_default_value(100,102,0,0)==100)
check('repo loss despite margin',repo_default_value(100,102,'.05','.01')==F('95.931'))
check('repo total loss',repo_default_value(100,102,1,0)==0)
for d in [0,'.02','.2',1]:
    x=run_sale(20,100,80,d)
    check('run assets conservation '+str(d),x['residual_assets']+x['paid']+x['sale_loss']==120)
    check('run obligation split '+str(d),x['paid']+x['unpaid']==80)
    check('no negative residual '+str(d),x['residual_assets']>=0)
check('run numeric sold',run_sale(20,100,80,'.2')['sold_mark']==75)
check('run numeric loss',run_sale(20,100,80,'.2')['sale_loss']==15)
check('unpayable demand retained',run_sale(20,100,130,'.2')['unpaid']==30)
check('cash only no forced sale',run_sale(20,100,10,'.5')['sale_loss']==0)
for inflation in ['-.9','-.1','0','.1','2']:
    check('symmetric indexed extreme '+inflation,liability(100,1+F(inflation),0)==100*(1+F(inflation)))
check('fixed claims cannot shrink with target',liability(0,'.1',100)==100)

# Stage2 reviewer counterexamples, independently calculated expected outputs.
check('stress buffer explicitly returned',adequacy(v,100)['free_pool_stress_buffer']==F('10.504'))
check('horizon is due cash not gross debt',adequacy(v,100,due_outflows=100)['horizon_gap']==F('-40.796'))
check('unknown due deadline not fabricated',adequacy(v,100)['horizon_gap'] is None)
check('impaired disclosure distinct',adequacy(v,100,benchmark='BENCHMARK_IMPAIRED')['status']=='BENCHMARK_IMPAIRED_REFERENCE_ONLY')
check('temporary disclosure distinct',adequacy(v,100,benchmark='TEMPORARY_CARRY')['status']=='CARRIED_TARGET_REFERENCE_ONLY')
paired=reserve_view([known_asset('y',100,encumbered_usd=30,secured_claim_id='secured',secured_obligation_usd=30)],0)
check('paired correct buffer ten',adequacy(paired,60)['free_pool_market_buffer']==10)
check('full inventory reconciliation ten',adequacy(paired,60)['full_inventory_reference_buffer']==10)
rejects('paired debt cannot reappear in other',lambda:adequacy(paired,60,[OtherClaim('secured',30)]))
rejects('duplicate other debt',lambda:adequacy(v,100,[OtherClaim('a',1),OtherClaim('a',1)]))
rejects('unpaired encumbrance',lambda:reserve_view([known_asset('x',100,encumbered_usd=30)],0))
excepted=reserve_view([known_asset('x',100,encumbered_usd=90,stale=True,secured_claim_id='s',secured_obligation_usd=90)],0)
check('excepted encumbrance visible',excepted['encumbered_market']==90 and excepted['paired_secured_debt']==90)
check('excepted residual disclosed but not certified',adequacy(excepted,10)['full_inventory_reference_buffer'] is None and adequacy(excepted,10)['status']=='INVENTORY_UNDETERMINED')
loss=reserve_view([known_asset('z',100,encumbered_usd=30,shock_factor='.5',secured_claim_id='s',secured_obligation_usd=40)],0)
check('deficiency in market branch',adequacy(loss,50)['free_pool_market_buffer']==10)
check('deficiency worsens with collateral stress',adequacy(loss,50)['free_pool_stress_buffer']==-40)
for kw in [dict(authenticated=None),dict(ownership_verified=1),dict(stale=None)]:
    rejects('unknown evidence flag '+str(kw),lambda:reserve_view([known_asset('x',1,**kw)],0))
rejects('unknown inventory completeness',lambda:reserve_view([],0,inventory_complete=None))
check('twenty-five percent run knife edge',run_sale(20,100,80,'.25')['residual_assets']==20)
check('thirty percent run shortfall exact',run_sale(20,100,80,'.30')['residual_assets']==F(100,7))
check('thirty percent run still owes twenty',100-run_sale(20,100,80,'.30')['paid']==20)
check('unpayable full run exact',run_sale(20,100,100,'.30')['unpaid']==10)
check('near total illiquidity expected paid',run_sale(20,100,80,'.9')['paid']==30)
check('near total illiquidity expected unpaid',run_sale(20,100,80,'.9')['unpaid']==50)
check('fractional units keep residual precision',liability('1.000000000000000001','1.000000000000000001',0)==F('1.000000000000000002000000000000000001'))
rejects('target off binding grid',lambda:liability(1,'1.0000000000000000001',0))
check('joint loss execution and expenses',run_sale(20,90,80,'.10')['residual_assets']-20-2==F(4,3))

# Reconciliation invariant is a useful necessary property, not an independent
# expected-value proof; direct counterexamples above test payout correctness.
for e,debt in [(0,0),(30,20),(30,40),(100,100)]:
    a=known_asset('a',100,encumbered_usd=e,secured_claim_id='s' if debt else '',secured_obligation_usd=debt)
    view=reserve_view([a],0); result=adequacy(view,50)
    check('pool reconciliation '+str((e,debt)),result['full_inventory_reference_buffer']-result['free_pool_market_buffer']==e-min(e,debt))

# Final-review input defaults and unsupported collateral coverage.
check('omitted evidence fails eligible credit',reserve_view([Asset('unknown',100)],0)['eligible_market']==0)
check('omitted evidence remains exception',not reserve_view([Asset('unknown',100)],0)['complete'])
check('excepted asset never offsets market debt',excepted['conditionally_allocated_secured_debt']==0)
check('excepted asset never offsets stressed debt',excepted['stress_allocated_secured_debt']==0)
check('excepted known debt retained free pool',adequacy(excepted,10)['free_pool_market_buffer']==-100)
check('excepted full buffer withheld',adequacy(excepted,10)['full_inventory_reference_buffer'] is None)
check('remaining liquidation haircut explicit',run_sale(20,100,80,'.30')['residual_liquidation_value']==10)
check('zero execution value not mark recovery',run_sale(20,100,80,1)['residual_liquidation_value']==0)

bill=known_asset('m',99,accessible_after_hours=0,sale_discount='.1',maturity_after_hours=24,maturity_receipt_usd=100)
check('bill sale before maturity discounted',reserve_view([bill],23)['horizon_available']==F('89.1'))
check('bill maturity not sale discounted',reserve_view([bill],24)['horizon_available']==100)
check('bill never counts sale plus maturity',reserve_view([bill],25)['horizon_available']==100)
check('defaulted maturity receipt explicit zero',reserve_view([known_asset('d',99,maturity_after_hours=24,maturity_receipt_usd=0)],24)['horizon_available']==0)
rejects('unpaired maturity',lambda:reserve_view([known_asset('x',1,maturity_after_hours=24)],24))
rejects('unpaired receipt',lambda:reserve_view([known_asset('x',1,maturity_receipt_usd=1)],24))
check('expense exceeding cash forces sale',run_sale(9,100,15+80,'.2')['sold_mark']==100 and run_sale(9,100,95,'.2')['unpaid']==6)

report={'passed':len(checks)-len(failed),'failed':failed,'checks':checks,
        'scope':'Exact synthetic balance-sheet, pricing sensitivity and liquidity checks; no production, economic, legal, solvency, oracle or independent audit certification'}
Path(__file__).with_name('validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':report['passed'],'failed':failed}))
raise SystemExit(bool(failed))
