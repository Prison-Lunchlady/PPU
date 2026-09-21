"""Offline adversarial examples and invariant checks; not a financial backtest."""
import json
from pathlib import Path
from fractions import Fraction as F
from dataclasses import replace
from datetime import timedelta
from reference_model import *

checks = {}
examples = {}
def check(name, condition):
    checks[name] = bool(condition)
def pair(m, v, received=None, **kw):
    t = instant(received) if received else first(shift(m,1))+timedelta(days=19)
    kw.setdefault('release_hash',hashlib.sha256((m+'-original-synthetic').encode()).hexdigest())
    kw.setdefault('source_url','https://example.invalid/synthetic/'+m)
    return [Packet(m, str(v), m+'-first', p, t, t-timedelta(hours=1), **kw)
            for p in ['A', 'B']]

packets = pair('2026-01', 300) + pair('2026-02', 303)
base, april = initialize('2026-04', packets)
a = value(april, instant('2026-04-16T00:00:00Z'), base)
examples['A'] = a
check('A_midmonth_independent_1_005', a['binding'] == '1.005000000000000000')
check('A_first_1', value(april, first('2026-04'), base)['binding'] == '1.000000000000000000')
may = plan('2026-05', april, base, pair('2026-03',306, '2026-04-20T00:00:00Z'))
check('A_month_boundary_1_01', value(may, first('2026-05'), base)['binding'] == '1.010000000000000000')
check('A_boundary_one_daily_increment', may.start - F(value(april, instant('2026-04-30T00:00:00Z'),base)['reference_index']) == F(1,10))

high = plan('2026-04', None, 300, pair('2026-02',330))
examples['B'] = value(high, instant('2026-04-16T00:00:00Z'), 300)
check('B_halfway_1_05', examples['B']['binding'] == '1.050000000000000000')
prev = high
for m, idx in [('2026-05',363),('2026-06','399.3'),('2026-07','439.23')]:
    nxt = plan(m,prev,300,pair(shift(m,-2),idx))
    check('B_extended_'+m,nxt.end>nxt.start and nxt.mode=='NORMAL')
    prev=nxt

down = plan('2026-04',None,300,pair('2026-02',294))
down2 = plan('2026-05',down,300,pair('2026-03',288))
examples['C'] = {'first_endpoint':rounded(down.end/F(300)), 'second_endpoint':rounded(down2.end/F(300))}
check('C_no_floor', examples['C']=={'first_endpoint':'0.980000000000000000','second_endpoint':'0.960000000000000000'})

dec = plan('2025-12',None,F('324.800'),[])
jan = plan('2026-01',dec,F('324.800'),pair('2025-11','324.122','2025-12-20T00:00:00Z'))
examples['D']={'december_end':str(dec.end),'january':value(jan,instant('2026-01-16T00:00:00Z'),F('324.800'))}
check('D_absence_not_zero',dec.end==F('324.800') and dec.mode=='FROZEN')
check('D_recovery_can_decline',jan.end==F('324.122') and jan.mode=='CATCH_UP' and jan.end<jan.start)

late = pair('2026-02',303,'2026-03-31T00:00:00Z')
e = plan('2026-04',None,300,late)
check('E_equal_cutoff_is_late',e.mode=='FROZEN')
early=[replace(p,received=cutoff('2026-04')-timedelta(microseconds=1),published=cutoff('2026-04')-timedelta(hours=1)) for p in late]
check('E_before_cutoff_eligible',plan('2026-04',None,300,early).end==303)
examples['E']={'at_cutoff':e.mode,'one_microsecond_before':'NORMAL'}

correction=[replace(p,value='302',edition='corrected',original_edition=False) for p in pair('2026-02',303)]
check('F_corrected_vintage_not_selected',plan('2026-04',None,300,packets+correction)==april)
check('F_past_target_unchanged',value(april,instant('2026-04-16T00:00:00Z'),300)==a)
f=plan('2026-05',april,300,pair('2026-03',306),review_hold=True)
check('F_future_hold',f.mode=='FROZEN' and f.end==303)
examples['F']={'historical':a['binding'],'future_endpoint':str(f.end)}

g=april
for m in ['2026-05','2026-06','2026-07']:
    g=plan(m,g,300,[])
check('G_three_frozen_triggers_reassessment',g.frozen_count==3 and g.end==303)
examples['G']={'frozen_months':g.frozen_count,'endpoint':str(g.end)}
for case in ['H','I']:
    held=plan('2026-05',april,300,pair('2026-03',306),review_hold=True)
    check(case+'_hold_no_automatic_successor',held.end==303 and held.reason=='INDEX_REVIEW_HOLD')
    examples[case]={'next_plan':held.mode,'endpoint':str(held.end)}

jpack=pair('2026-02',303)+[replace(pair('2026-02',304)[0],path='C')]
j=plan('2026-04',None,300,jpack)
check('J_authenticated_conflict_blocks_even_two_agree',j.mode=='FROZEN' and j.reason=='CONFLICT')
examples['J']={'mode':j.mode,'reason':j.reason}
check('K_late_delivery_same_as_missing',plan('2026-04',None,300,late).end==300)
check('K_downtime_does_not_rewrite_precommit',F(value(april,instant('2026-04-20T00:00:00Z'),300)['exact'])==F(3019,3000))
examples['K']={'precommitted':value(april,instant('2026-04-20T00:00:00Z'),300),'late_delivery':'FROZEN'}
bad=replace(pair('2026-02',999999)[0],path='C',authenticated=False)
check('L_unauthenticated_abnormal_quarantined',plan('2026-04',None,300,packets+[bad])==april)
auth_high=plan('2026-04',None,300,pair('2026-02',999999))
check('L_authentic_extreme_not_price_capped',auth_high.end==999999)
examples['L']={'spoof_ignored':True,'authenticated_extreme_endpoint':str(auth_high.end)}

at=instant('2026-04-16T00:00:00Z')
fresh={'A':at-timedelta(hours=1),'B':at-timedelta(hours=2)}
check('health_normal_fresh',issuance_data_ok(april,at,fresh))
check('health_age_equality_stale',not issuance_data_ok(april,at,{'A':at-timedelta(days=1),'B':at-timedelta(hours=1)}))
check('health_adverse_blocks',not issuance_data_ok(april,at,fresh,True))
check('health_frozen_cannot_restore_by_monitor',not issuance_data_ok(e,at,fresh))
check('health_catchup_cannot_restore_by_monitor',not issuance_data_ok(jan,at,fresh))
check('health_no_future_attestations',not issuance_data_ok(april,at,{'A':at,'B':at+timedelta(seconds=1)}))
check('round_tie_even_down',rounded(F(5,2),0)=='2.0')
check('round_tie_even_up',rounded(F(7,2),0)=='4.0')
check('round_18_tie',rounded(F(1)+F(5,10**19))=='1.000000000000000000')
check('round_18_odd_tie',rounded(F(1)+F(15,10**19))=='1.000000000000000002')

leap=plan('2024-02',None,300,pair('2023-12',329,'2024-01-20T00:00:00Z'))
check('leap_29_days',F(value(leap,instant('2024-02-29T23:59:59Z'),300)['reference_index'])==328)
check('UTC_equivalent_instants',instant('2026-03-11T08:30:00-04:00')==instant('2026-03-11T12:30:00Z'))
check('UTC_standard_offset',instant('2026-02-13T08:30:00-05:00')==instant('2026-02-13T13:30:00Z'))
treasury=F('154.40')+F(14,30)*(F('154.90')-F('154.40'))
check('Treasury_external_vector_15463333',rounded(treasury,5)=='154.63333')
rebased=plan('2026-04',None,300,pair('2026-02',101,factor='3'))
check('exact_rebase_invariance',rebased.end==april.end)
check('unverified_rebase_blocked',plan('2026-04',None,300,pair('2026-02',101,factor='3',normalization_verified=False)).mode=='FROZEN')
for invalid in ['-', '0', '-1', 'NaN']:
    check('invalid_'+invalid,plan('2026-04',None,300,pair('2026-02',invalid)).mode=='FROZEN')
tiny=plan('2026-04',None,F('0.0000000000000000000001'),[])
check('round_to_zero_explicit',value(tiny,first('2026-04'),300)['status']=='UNREPRESENTABLE')
try:
    initialize('2026-04',[])
    check('genesis_requires_both',False)
except ValueError:
    check('genesis_requires_both',True)
check('month_shift_year',shift('2026-01',-3)=='2025-10')
for y,m in [(2024,2),(2025,2),(2026,4),(2026,5)]:
    days=monthrange(y,m)[1]
    for s,e_ in [(F(300),F(303)),(F(303),F(300)),(F(300),F(300))]:
        vals=[s+F(d-1,days)*(e_-s) for d in range(1,days+1)]
        check(f'convex_monotonic_{y}_{m}_{s}_{e_}',all(min(s,e_)<=v<=max(s,e_) for v in vals)
              and all(vals[i+1]-vals[i]==(e_-s)/days for i in range(days-1)))

trace_packets=packets+pair('2026-03',306,'2026-04-20T00:00:00Z')+pair('2026-04',309,'2026-05-20T00:00:00Z')
trace_before=replay('2026-04',instant('2026-04-16T00:00:00Z'),trace_packets)
check('replay_valid_genesis',trace_before['binding']=='1.005000000000000000')
opened=ControlEvent(instant('2026-04-20T00:00:00Z'),'OPEN','feb-correction')
cleared=ControlEvent(instant('2026-05-10T00:00:00Z'),'RESOLVE','feb-correction')
check('replay_correction_cannot_change_history',replay('2026-04',instant('2026-04-16T00:00:00Z'),trace_packets,[opened,cleared])['binding']==trace_before['binding'])
trace_may=replay('2026-04',instant('2026-05-16T00:00:00Z'),trace_packets,[opened,cleared])
check('replay_midmonth_clear_cannot_unfreeze_plan',trace_may['binding']=='1.010000000000000000' and trace_may['plans'][-1]['mode']=='FROZEN')
trace_june=replay('2026-04',instant('2026-06-16T00:00:00Z'),trace_packets,[opened,cleared])
check('replay_prospective_recovery_after_clear',trace_june['binding']=='1.020000000000000000' and trace_june['plans'][-1]['mode']=='CATCH_UP')
postcut=ControlEvent(instant('2026-04-30T00:00:00Z'),'OPEN','at-cutoff')
check('replay_hold_at_cutoff_does_not_rewrite_committed_plan',replay('2026-04',instant('2026-05-16T00:00:00Z'),trace_packets,[postcut])['binding']=='1.014838709677419355')
check('replay_hold_at_cutoff_blocks_health',not replay('2026-04',instant('2026-05-16T00:00:00Z'),trace_packets,[postcut])['issuanceDataOK'])
check('replay_pre_genesis_not_active',replay('2026-04',instant('2026-03-15T00:00:00Z'),[])['status']=='NOT_ACTIVE')
outage=replay('2026-04',instant('2026-07-16T00:00:00Z'),packets)
check('replay_three_missing_with_valid_genesis',outage['reassessment_required'] and outage['binding']=='1.010000000000000000')
ack=instant('2026-07-10T00:00:00Z')
check('replay_reassessment_ack_does_not_unfreeze',not replay('2026-04',instant('2026-07-16T00:00:00Z'),packets,reassessment_dispositions=[ack])['reassessment_required'] and outage['plans'][-1]['mode']=='FROZEN')
other=ControlEvent(instant('2026-04-21T00:00:00Z'),'OPEN','other')
check('replay_clear_only_named_hold',holds_before([opened,other,cleared],instant('2026-05-11T00:00:00Z'))=={'other'})
sameclear=ControlEvent(opened.received,'RESOLVE','feb-correction')
check('replay_simultaneous_open_wins',holds_before([opened,sameclear],instant('2026-05-11T00:00:00Z'))=={'feb-correction'})
check('replay_invalid_control_ignored',not holds_before([replace(opened,validated=False)],instant('2026-05-11T00:00:00Z')))

check('method_shock_release_gap',F(43,11)==sum([F(1,11)]*43))
check('method_shock_monthly_gap',F(59,11)==sum([F(1,11)]*59))
daily_gap=F(59,11)+sum((1-(F(1)+F(d-1,310))/F(11,10) for d in range(1,32)),F(0))
check('method_shock_daily_gap',daily_gap==F(75,11))
check('six_missing_months_catchup',F(105,100)**6==F('1.340095640625'))

# Public target interface A-L, all from admissible genesis. Earlier tests are
# deliberately isolated helper/negative-state tests, not activation evidence.
public_cases={}
public_cases['A']=replay('2026-04',at,packets,monitor_times=fresh)
public_cases['B']=replay('2026-04',at,pair('2026-01',300)+pair('2026-02',330))
public_cases['C']=replay('2026-04',first('2026-06'),pair('2026-01',300)+pair('2026-02',294)+pair('2026-03',288)+pair('2026-04',282))
dp=pair('2025-08',320)+pair('2025-09','324.800')+pair('2025-11','324.122')
public_cases['D']=replay('2025-11',instant('2026-01-16T00:00:00Z'),dp)
delay=pair('2026-03',306,'2026-04-30T00:00:00Z')
public_cases['E']=replay('2026-04',instant('2026-05-16T00:00:00Z'),packets+delay)
corrected=[replace(p,original_edition=False,edition='corrected',release_hash=hashlib.sha256(b'feb-correction').hexdigest()) for p in pair('2026-02',302,'2026-04-20T00:00:00Z')]
public_cases['F']=replay('2026-04',instant('2026-05-16T00:00:00Z'),trace_packets+corrected)
public_cases['G']=outage
public_cases['H']=replay('2026-04',instant('2026-05-16T00:00:00Z'),trace_packets,[ControlEvent(instant('2026-04-20T00:00:00Z'),'OPEN','material-methodology')])
public_cases['I']=replay('2026-04',instant('2026-05-16T00:00:00Z'),trace_packets,[ControlEvent(instant('2026-04-20T00:00:00Z'),'OPEN','discontinuation')])
j3=pair('2026-03',306)+[replace(pair('2026-03',307)[0],path='C')]
public_cases['J']=replay('2026-04',instant('2026-05-16T00:00:00Z'),packets+j3)
public_cases['K']=replay('2026-04',instant('2026-05-16T00:00:00Z'),packets+delay)
public_cases['L']=replay('2026-04',instant('2026-05-16T00:00:00Z'),trace_packets+[replace(pair('2026-03',999999)[0],path='C',authenticated=False)])
for label in 'ABCDEFGHIJKL':check('public_case_'+label+'_valid_genesis',public_cases[label]['status']=='VALUE' and public_cases[label]['plans'][0]['mode']=='NORMAL')
for label in 'EFGHIJK':check('public_case_'+label+'_frozen',public_cases[label]['mode']=='FROZEN')
check('public_D_catchup_valid_genesis',public_cases['D']['mode']=='CATCH_UP' and F(public_cases['D']['reference_index'])==F(1005863,3100))
check('public_C_below_base',public_cases['C']['binding']=='0.960000000000000000')
check('public_F_automatic_correction_hold',public_cases['F']['plans'][-1]['reason']=='INDEX_REVIEW_HOLD')
check('public_L_spoof_cannot_block_valid',public_cases['L']['mode']=='NORMAL')
check('public_timezone_day_normalized',replay('2026-04',instant('2026-04-16T23:00:00-05:00'),packets)['binding']=='1.005333333333333333')
check('public_timezone_direct_datetime',replay('2026-04',datetime.fromisoformat('2026-04-16T23:00:00-05:00'),packets)['binding']=='1.005333333333333333')
try:
    replay('2026-04',datetime(2026,4,16),packets);check('naive_time_rejected',False)
except ValueError:check('naive_time_rejected',True)
for badformat in ['3/2','1e3','1_0','03.0',' 300','+300']:
    check('decimal_grammar_'+badformat,replay('2026-04',at,pair('2026-01',300)+pair('2026-02',badformat))['status']=='NOT_ACTIVE')
labels=[replace(p,edition='different friendly '+p.path) for p in packets]
check('canonical_edition_ignores_labels',replay('2026-04',at,labels)['binding']==a['binding'])
check('unconfigured_paths_cannot_vote',replay('2026-04',at,[replace(p,path='X'+p.path) for p in packets])['status']=='NOT_ACTIVE')
check('unconfigured_monitor_cannot_vote',not replay('2026-04',at,packets,monitor_times={'X':at-timedelta(hours=1),'Y':at-timedelta(hours=1)})['issuanceDataOK'])
unverified=pair('2026-03',102,factor='3',normalization_verified=False)
unv=replay('2026-04',instant('2026-06-16T00:00:00Z'),trace_packets+unverified)
check('unverified_normalization_latches_hold',unv['mode']=='FROZEN')
alternating=packets+pair('2026-04',309)+pair('2026-06',315)+pair('2026-08',321)
alt=replay('2026-04',instant('2026-08-16T00:00:00Z'),alternating)
check('rolling_impairment_trigger',alt['reassessment_required'])
returned=packets+pair('2026-06',315)+pair('2026-07',318)+pair('2026-08',321)
check('reassessment_survives_normal_return',replay('2026-04',instant('2026-10-16T00:00:00Z'),returned)['reassessment_required'])
check('public_tuple_metadata',all(k in public_cases['A'] for k in ['cutoff','source_observation_month','vintage_ids','plan_prefix_hash','health_status']))
check('non_value_display_suppressed',value(tiny,first('2026-04'),300)['display'] is None)

from decimal import Decimal,localcontext
gap_grid=[]
with localcontext() as ctx:
    ctx.prec=50
    for missing in [2,3,6]:
        for annual in ['0','.03','.20']:
            q=(1+Decimal(annual))**(Decimal(1)/12)
            factor=q**(missing+1) # n missed observations, then next expected: n+1 intervals
            rm=shift('2026-04',missing+1)
            end=format(Decimal(303)*factor,'.18f')
            pp=packets+pair(shift(rm,-2),end)
            out=replay('2026-04',first(rm)+timedelta(days=15),pp)
            check(f'gap_recovery_{missing}_{annual}',out['mode']=='CATCH_UP' and not out['issuanceDataOK'] and F(out['plans'][-1]['end'])==F(end))
            D=monthrange(first(rm).year,first(rm).month)[1]
            gap_grid.append({'missing_observations':missing,'annual_growth':annual,'recovery_month':rm,'elapsed_monthly_intervals':missing+1,
                'recovery_change_percent':str(100*(factor-1)),
                'daily_step_percent_of_old_endpoint':str(100*(factor-1)/D),
                'slope_multiple_vs_one_month_same_start_days':None if q==1 else str((factor-1)/(q-1)),
                'pre_recovery_real_shortfall_percent':str(100*(1-1/factor))})

official=json.loads(Path(__file__).with_name('treasury-may2026-fixture.json').read_text())
official_packets=sum((pair(m,v) for m,v in official['monthly_CPI'].items()),[])
for row in official['rows']:
    official_out=replay('2026-04',first('2026-05')+timedelta(days=row['day']-1),official_packets)
    check('Treasury_May2026_day_'+str(row['day']),rounded(F(official_out['reference_index']),5)==row['ref_cpi'])

conflict_at=instant('2026-04-25T00:00:00Z')
fresh_now={'A':conflict_at-timedelta(hours=1),'B':conflict_at-timedelta(hours=2)}
check('conflict_health_before_next_plan',not replay('2026-04',conflict_at,packets+j3,monitor_times=fresh_now)['issuanceDataOK'])
resolution=ControlEvent(instant('2026-04-26T00:00:00Z'),'REJECT_PACKET',packet_key(j3[-1]))
resolved=replay('2026-04',instant('2026-05-16T00:00:00Z'),packets+j3,[resolution])
check('publisher_mismatch_resolution_prospective',resolved['mode']=='NORMAL')
check('resolution_cannot_rewrite_prior_conflict',not replay('2026-04',conflict_at,packets+j3,[resolution],monitor_times=fresh_now)['issuanceDataOK'])
exact_conflict=j3[-1].received
check('conflict_health_at_exact_receipt',not replay('2026-04',exact_conflict,packets+j3,monitor_times={'A':exact_conflict-timedelta(hours=1),'B':exact_conflict-timedelta(hours=2)})['issuanceDataOK'])

result={'scope':'offline reference arithmetic and validated-input scenarios; not oracle/security/solvency certification',
        'checks':checks,'failed':[k for k,v in checks.items() if not v],
        'case_examples':examples,'public_interface_cases':public_cases,'gap_recovery_grid':gap_grid,
        'full_replay_examples':{'normal':trace_before,'correction_may':trace_may,'correction_june':trace_june,'extended_outage':outage},
        'lag_scenarios':[{'annual_growth':r,'current_over_lagged_percent':100*((1+r)**(2.5/12)-1),
                          'purchasing_power_shortfall_percent':100*(1-(1+r)**(-2.5/12))} for r in [.03,.10,.20,1.0]],
        'pass':all(checks.values())}
Path(__file__).with_name('model-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'failed':result['failed'],'pass':result['pass'],'lag':result['lag_scenarios']},indent=2))
if not result['pass']:
    raise SystemExit(1)
