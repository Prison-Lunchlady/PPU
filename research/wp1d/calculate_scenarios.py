"""Bounded WP1D comparative diagnostics, not Phase 2 backtesting."""
from reserve_model import *
from pathlib import Path
import json
def dec(x):return round(float(x),6)
structures={'A_cash_bills':(20,80,0),'B_mixed':(20,40,40),'C_liquidity':(40,40,20),'D_TIPS_heavy':(10,20,70)}
# All units USD millions; A0=120, L0=100 solely common comparison scale.
# Gross total return factors supplied, inclusive of all assumed carry/index accrual.
scenarios={
 '1970s_inflation_analogue':('.15','1.03','1.05','1.15'),
 'rapid_disinflation':('.02','1.02','1.03','1.02'),
 'Volcker_tightening_analogue':('.10','1.02','.97','.98'),
 'deflation':('-.10','1.00','1.01','.90'),
 'COVID_liquidity_analogue':('0','1','.99','.92'),
 '2008_liquidity_analogue':('-.02','1','1.01','.85'),
 'inflation_and_liquidity':('.15','1','.97','.90'),
 'Treasury_dysfunction':('.03','1','.95','.85'),
 'index_impaired_assets_inflate':('0','1','1.02','1.10'),
 'reserve_impairment_index_normal':('.03','.75','.99','.90')}
rows=[]
for name,weights in structures.items():
 for scenario,(i,c,b,t) in scenarios.items():
    A=sum(F(w)*F(f) for w,f in zip(weights,(c,b,t)))*F('1.2')
    indexed=100*(1+F(i)); fixed_mix=80*(1+F(i))+20
    rows.append(dict(structure=name,scenario=scenario,assets=dec(A),indexed_liability=dec(indexed),fixed_mix_liability=dec(fixed_mix),indexed_buffer=dec(A-indexed),fixed_mix_buffer=dec(A-fixed_mix)))
duration=[]
for years in ['.5','2','5','10']:
 for shock in ['-.05','-.03','-.01','.01','.03','.05']:
    ratio=zero_coupon_ratio(years,'.02',F('.02')+F(shock))
    duration.append(dict(years=years,shock=shock,exact_zero_coupon_change_pct=dec((ratio-1)*100)))
alternatives=[]
for asset,shock in [('gold','-.25'),('Bitcoin','-.70'),('commodities','-.40'),('energy','-.60'),('equities','-.50'),('corporate_credit','-.20'),('tokenized_RWA_wrapper','-.30')]:
    # Replace 6 of 120 in a zero-return bill position. No positive hedge assumed.
    alternatives.append(dict(asset=asset,addition_pct=5,adverse_return=shock,incremental_loss=dec(-6*F(shock)),liquidation_delay='UNKNOWN; no immediate credit'))
run_curve=[]
for assets in [102,120]:
 for cash in [10,20,40]:
  for d in ['0','.02','.10','.20','.25','.30']:
   for demand in [0,20,40,60,80,100]:
    x=run_sale(cash,assets-cash,demand,d); remaining=100-x['paid']
    run_curve.append(dict(initial_assets=assets,cash=cash,demand=demand,discount=d,**{k:dec(v) for k,v in x.items()},remaining_face=dec(remaining),remaining_coverage=dec(x['residual_assets']/remaining) if remaining else None,remaining_liquidation_coverage=dec(x['residual_liquidation_value']/remaining) if remaining else None))
joint=[]; alternative_joint=[]; repo_liquidity=[]
for name,weights in structures.items():
 for scenario,(i,c,b,t) in scenarios.items():
  cash=F(weights[0])*F('1.2')*F(c)
  bills=F(weights[1])*F('1.2')*F(b); tips=F(weights[2])*F('1.2')*F(t)
  L=100*(1+F(i))
  for cost in [0,2,5,15]:
   for demand_share in ['.8','1']:
    for discount in ['.02','.20']:
     # Expense is an additional recognized obligation; funding may require
     # sales even before redemption. No priority assigned between USD debts.
     x=run_sale(cash,bills+tips,L*F(demand_share)+cost,discount)
     rem=L+cost-x['paid']
     joint.append(dict(structure=name,scenario=scenario,operating_expense=cost,demand_share=demand_share,incremental_discount=discount,assets_after_shock=dec(cash+bills+tips),liability=dec(L),remaining_liability=dec(rem),remaining_assets=dec(x['residual_assets']),remaining_buffer=dec(x['residual_assets']-rem),remaining_liquidation_buffer=dec(x['residual_liquidation_value']-rem),unpaid_demand=dec(x['unpaid'])))
  for alt,shock in [('gold','-.25'),('Bitcoin','-.70'),('commodities','-.40'),('energy','-.60'),('equities','-.50'),('corporate_credit','-.20'),('tokenized_RWA_wrapper','-.30')]:
   for branch,alt_return in [('adverse',shock),('favorable','.25')]:
    # Replace6 initial bill dollars with6 alternative, same joint background.
    replacement=6*(1+F(alt_return)); changed=bills-6*F(b)+tips+replacement
    baseline=run_sale(cash,bills+tips,L*F('.8')+2,'.10')
    alternative=run_sale(cash,changed,L*F('.8')+2,'.10')
    base_buffer=baseline['residual_assets']-(L+2-baseline['paid'])
    alt_buffer=alternative['residual_assets']-(L+2-alternative['paid'])
    alternative_joint.append(dict(structure=name,scenario=scenario,asset=alt,branch=branch,alternative_return=alt_return,baseline_remaining_buffer=dec(base_buffer),alternative_remaining_buffer=dec(alt_buffer),incremental_buffer=dec(alt_buffer-base_buffer),assumption='Same10% incremental sale friction for comparability; wrapper/custody access may be worse. Favorable and adverse returns are sensitivities, not empirical correlation evidence.'))
for share in [0,10,20]:
 for term in ([0] if share==0 else [24,168,720]):
  for horizon in [0,24,72,168,720]:
    # Fixed120 assets: cash20, remaining bills100-repo, repo replaces bills.
    # Bills can be sold with1% discount and24h settlement. Repo maturity pays
    # assumed receipt only at stated term. No renewal or predefault sale.
    amount=share*F('1.2')
    baseline=20+(100*F('.99') if horizon>=24 else 0)
    available=20+((100-amount)*F('.99') if horizon>=24 else 0)+(amount if term<=horizon else 0)
    repo_liquidity.append(dict(repo_share_pct=share,term_hours=term,horizon_hours=horizon,available_cash=dec(available),bill_baseline_available=dec(baseline),incremental_available=dec(available-baseline)))
out={'assumptions':'Synthetic analogues, not observed historical returns, fitted distributions or portfolio recommendations. Display rounded only; core uses exact fractions. Common 120/100 scale is not a recommended ratio. Gross comparisons exclude operating expense/incremental sale cost; joint cases add both.','structures':structures,'scenarios':scenarios,'comparisons':rows,'duration':duration,'alternative_tail_counterexamples':alternatives,'cumulative_run_curve':run_curve,'joint_shock_run_costs':joint,'alternative_joint_comparison':alternative_joint,'repo_horizon_comparison':repo_liquidity,'negative_real_carry_assets_after_10y':dec(120*F('.98')**10)}
Path(__file__).with_name('scenario-results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Generated',len(rows),'gross cases,',len(duration),'rate sensitivities,',len(run_curve),'run cases,',len(joint),'joint shock/run/cost cases,',len(alternative_joint),'joint alternative cases,',len(repo_liquidity),'repo horizon cases')
