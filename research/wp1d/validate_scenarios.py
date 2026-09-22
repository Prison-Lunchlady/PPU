"""Reproduction plus independently calculated scenario-level spot checks.

Counts are assertions, not independent economic experiments.
"""
from pathlib import Path
from fractions import Fraction as F
import subprocess,sys,json
r=Path(__file__).parent;p=r/'scenario-results.json';before=p.read_bytes()
subprocess.run([sys.executable,str(r/'calculate_scenarios.py')],check=True)
j=json.loads(p.read_text(encoding='utf-8'));checks={}
checks['exact_reproduction']=before==p.read_bytes()
for key,n in [('comparisons',40),('duration',24),('alternative_tail_counterexamples',7),('cumulative_run_curve',216),('joint_shock_run_costs',640),('alternative_joint_comparison',560),('repo_horizon_comparison',35)]:
 checks['count_'+key]=len(j[key])==n
def one(key,**match):return next(x for x in j[key] if all(x[k]==v for k,v in match.items()))
b=one('comparisons',structure='B_mixed',scenario='inflation_and_liquidity')
checks['gross_B_assets']=b['assets']==113.76
checks['gross_B_indexed_face']=b['indexed_liability']==115
checks['gross_B_negative_buffer']=b['indexed_buffer']==-1.24
checks['gross_B_fixed_face']=b['fixed_mix_liability']==112
b=one('comparisons',structure='B_mixed',scenario='deflation')
checks['deflation_fixed_exposure']=b['fixed_mix_liability']==92 and b['indexed_liability']==90
x=one('cumulative_run_curve',initial_assets=120,cash=20,demand=80,discount='.30')
checks['run_remaining_harm']=x['remaining_face']==20 and x['residual_assets']==14.285714 and x['remaining_coverage']==.714286
checks['net_real_carry_exhaustion']=j['negative_real_carry_assets_after_10y']==round(float(120*F('.98')**10),6)<100
x=one('joint_shock_run_costs',structure='B_mixed',scenario='inflation_and_liquidity',operating_expense=2,incremental_discount='.20')
# cash24 - expense2; bill46.56+TIPS43.2; demand92. Sell87.5
# marked ->70 cash; residual securities2.26; remaining face23.
checks['joint_B_remaining_assets']=x['remaining_assets']==2.26
checks['joint_B_remaining_buffer']=x['remaining_buffer']==-20.74
x=one('repo_horizon_comparison',repo_share_pct=20,term_hours=168,horizon_hours=72)
checks['repo_before_maturity']=x['available_cash']==95.24 and x['incremental_available']==-23.76
x=one('repo_horizon_comparison',repo_share_pct=20,term_hours=168,horizon_hours=168)
checks['repo_at_maturity']=x['available_cash']==119.24
checks['signed_alternative_sensitivities']=any(x['incremental_buffer']>0 for x in j['alternative_joint_comparison']) and any(x['incremental_buffer']<0 for x in j['alternative_joint_comparison'])
report={'passed':sum(checks.values()),'failed':[k for k,v in checks.items() if not v],'checks':checks,'scope':'Deterministic artifact reproduction and scenario accounting; magnitudes are synthetic, no historical/economic validation'}
(r/'scenario-validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(bool(report['failed']))
