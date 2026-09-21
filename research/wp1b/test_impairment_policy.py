"""Adversarial state and alternative-policy calculations, synthetic unless labeled."""
from pathlib import Path
from fractions import Fraction as F
from datetime import timedelta
from dataclasses import replace
import json
from reference_model import Packet, first, shift, replay, instant
from impairment_policy import ImpairmentEvent as E, replay_with_impairment as run

checks={}
def ck(n,v):checks[n]=bool(v)
def pair(m,v):
 t=first(shift(m,1))+timedelta(days=15)
 return [Packet(m,str(v),'original',p,t,t-timedelta(hours=1),release_hash='a'*64,source_url='https://example.invalid/synthetic') for p in ['A','B']]
def fresh(t):return {'A':t-timedelta(hours=1),'B':t-timedelta(hours=2)}
def event(t,kind,id='notice',same=False,valid=True):
 at=instant(t)
 return E(at,kind,id,'b'*64,valid,same,tuple(fresh(at).items()) if kind=='CLEAR_IMPAIRMENT' else (),kind=='CLEAR_IMPAIRMENT')
ps=sum((pair(shift('2026-01',i),300+i) for i in range(10)),[])
april=instant('2026-04-15T00:00:00Z');july=instant('2026-07-15T00:00:00Z')
base=run('2026-04',april,ps,monitor_times=fresh(april))
ck('normal_status',base['benchmark_status']=='NORMAL')
ck('numeric_formula_unchanged',base['binding']==replay('2026-04',april,ps)['binding'])
ck('uninitialized_not_impaired',run('2026-04',april,[])['benchmark_status']=='NOT_ACTIVE')
short=run('2026-04',instant('2026-05-15T00:00:00Z'),ps[:4])
ck('one_missing_month_temporary',short['benchmark_status']=='TEMPORARY_DATA_FAILURE')
long=run('2026-04',july,ps[:4],monitor_times=fresh(july))
ck('three_frozen_impaired',long['benchmark_status']=='BENCHMARK_IMPAIRED')
ck('duration_does_not_prove_structural',long['impairment_incidents'][0]['cause_class']=='PERSISTENT_UNRESOLVED')
ck('frozen_positive_target_retained',F(long['binding'])>0)
ck('impaired_never_data_eligible',not long['issuanceDataOK'])
ck('no_fallback_or_trueup',long['policy_action']=='NO_AUTOMATIC_TRUE_UP_OR_SUBSTITUTE')
notice=event('2026-04-15T00:00:00Z','DISCONTINUED')
atnotice=run('2026-04',april,ps,[notice],monitor_times=fresh(april))
ck('notice_immediate_state',atnotice['benchmark_status']=='BENCHMARK_IMPAIRED')
ck('committed_path_not_rewritten',atnotice['binding']==base['binding'])
ck('structural_class_explicit',atnotice['impairment_incidents'][0]['cause_class']=='STRUCTURAL_CONFIRMED')
before=april-timedelta(seconds=1)
ck('future_notice_no_effect',run('2026-04',before,ps,[notice],monitor_times=fresh(before))==run('2026-04',before,ps,monitor_times=fresh(before)))
ck('unvalidated_notice_ignored',run('2026-04',april,ps,[replace(notice,validated=False)],monitor_times=fresh(april))==base)
ck('malformed_evidence_ignored',run('2026-04',april,ps,[replace(notice,evidence_hash='bad')],monitor_times=fresh(april))==base)
ck('duplicate_active_notice_idempotent',run('2026-04',april,ps,[notice,notice],monitor_times=fresh(april))==atnotice)
may=instant('2026-05-15T00:00:00Z')
ck('future_uncommitted_plan_frozen',run('2026-04',may,ps,[notice])['mode']=='FROZEN')
restore=event('2026-04-20T00:00:00Z','SAME_BENCHMARK_RESTORED',same=True)
ck('different_benchmark_cannot_restore',run('2026-04',may,ps,[notice,replace(restore,same_benchmark=False)])['mode']=='FROZEN')
recovered=run('2026-04',may,ps,[notice,restore],monitor_times=fresh(may))
ck('restored_numeric_path_can_resume',recovered['mode']=='NORMAL')
ck('restoration_alone_does_not_clear',recovered['benchmark_status']=='BENCHMARK_IMPAIRED')
clear=event('2026-06-15T00:00:00Z','CLEAR_IMPAIRMENT','STRUCTURAL:notice',same=True)
june=clear.received
released=run('2026-04',june,ps,[notice,restore,clear],monitor_times=fresh(june))
ck('two_normal_plans_and_exact_clearance',released['benchmark_status']=='NORMAL')
ck('clearance_has_evidence',len(released['impairment_clearances'])==1)
ck('wrong_incident_no_clear',run('2026-04',june,ps,[notice,restore,replace(clear,incident='other')],monitor_times=fresh(june))['benchmark_status']=='BENCHMARK_IMPAIRED')
early=replace(clear,received=may)
ck('one_normal_plan_insufficient',run('2026-04',may,ps,[notice,restore,early],monitor_times=fresh(may))['benchmark_status']=='BENCHMARK_IMPAIRED')
ck('stale_monitors_prevent_clearance',run('2026-04',june,ps,[notice,restore,replace(clear,monitor_times=tuple(fresh(april).items()))],monitor_times=fresh(june))['benchmark_status']=='BENCHMARK_IMPAIRED')
ck('no_backdated_clearance_effect',run('2026-04',may,ps,[notice,restore,clear],monitor_times=fresh(may))==recovered)
again=event('2026-06-15T00:00:00Z','MATERIAL_CONCEPT_CHANGE')
ck('same_instant_open_wins',run('2026-04',june,ps,[notice,restore,clear,again],monitor_times=fresh(june))['benchmark_status']=='BENCHMARK_IMPAIRED')
ck('event_permutation_invariant',run('2026-04',june,ps,[clear,restore,notice],monitor_times=fresh(june))==released)
other=event('2026-06-14T00:00:00Z','DISCONTINUED','second')
ck('one_clear_never_clears_other_incident',run('2026-04',june,ps,[notice,restore,clear,other],monitor_times=fresh(june))['benchmark_status']=='BENCHMARK_IMPAIRED')
ck('deflation_arithmetic_unchanged',run('2026-04',april,pair('2026-01',300)+pair('2026-02',290),[notice])['binding']==replay('2026-04',april,pair('2026-01',300)+pair('2026-02',290))['binding'])
for field,bad in [('query',april.replace(tzinfo=None)),('event',replace(notice,received=april.replace(tzinfo=None)))]:
 try:run('2026-04',bad if field=='query' else april,ps,[] if field=='query' else [bad]);ck('naive_'+field+'_rejected',False)
 except ValueError:ck('naive_'+field+'_rejected',True)
# Independent signed contingent-adjustment and mismatch examples from the analysis.
positive=F(100)*90*F('0.10')/365
ck('trueup_is_additional_time_weighted_promise',positive==F(180,73))
ck('deflation_trueup_signed',F(100)*90*F('-0.10')/365==-positive)
ck('normalization_changes_compensation',F(100)*90*F('0.10')/90==10)
ck('transfer_debt_evasion_counterexample',F(0)>-positive)
ck('fallback_2_vs_cpi_10_shortfall',1-F('1.02')/F('1.10')==F(4,55))
ck('opposite_sign_fallback_worse',1-F('.98')/F('1.10')>1-F('1.02')/F('1.10'))
ck('freeze_loss_unbounded_in_nominal_gap',F(1000)-1>F(10)-1)
gapped=[p for p in ps if p.month not in {'2026-03','2026-04','2026-05'}]
october=instant('2026-10-15T00:00:00Z')
persistent=run('2026-04',october,gapped,monitor_times=fresh(october))
ck('persistent_label_survives_numeric_recovery',persistent['mode']=='NORMAL' and persistent['benchmark_status']=='BENCHMARK_IMPAIRED')
clear_p=event('2026-10-15T00:00:00Z','CLEAR_IMPAIRMENT','PERSISTENT:2026-07',same=True)
ck('persistent_incident_explicit_clear',run('2026-04',october,gapped,[clear_p],monitor_times=fresh(october))['benchmark_status']=='NORMAL')
alternating=[p for p in ps if p.month not in {'2026-03','2026-06'}]
august=instant('2026-08-15T00:00:00Z')
alt=run('2026-04',august,alternating,monitor_times=fresh(august))
ck('rolling_non_normal_trigger_without_three_freezes',alt['benchmark_status']=='BENCHMARK_IMPAIRED' and max(p['frozen_count'] for p in alt['plans'])<3)
ck('precutoff_notice_freezes_next_month',run('2026-04',may,ps,[replace(notice,received=instant('2026-04-29T00:00:00Z'))])['mode']=='FROZEN')
ck('cutoff_equal_notice_preserves_committed_plan',run('2026-04',may,ps,[replace(notice,received=instant('2026-04-30T00:00:00Z'))])['mode']=='NORMAL')
ck('cpi_hold_not_reference_price_floor',F(run('2026-04',april,pair('2026-01',300)+pair('2026-02',290),[notice])['binding'])<1)
ck('clearance_uses_archived_event_time_monitor_evidence',run('2026-04',july,ps,[notice,restore,clear],monitor_times=fresh(july))['benchmark_status']=='NORMAL')
ck('later_monitor_outage_does_not_undo_valid_clearance',run('2026-04',july,ps,[notice,restore,clear])['benchmark_status']=='TEMPORARY_DATA_FAILURE')
ck('later_adverse_flag_does_not_rewrite_clearance',run('2026-04',july,ps,[notice,restore,clear],monitor_times=fresh(july),unresolved_adverse=True)['benchmark_status']=='TEMPORARY_DATA_FAILURE')
ck('unproven_clearance_health_fails_closed',run('2026-04',june,ps,[notice,restore,replace(clear,clearance_adverse_free=False)],monitor_times=fresh(june))['benchmark_status']=='BENCHMARK_IMPAIRED')
out={'revision':'0.3','scope':'proposed impairment overlay and synthetic alternative-policy counterexamples','checks':checks,'passed':sum(checks.values()),'failed':[k for k,v in checks.items() if not v], 'examples':{'positive_trueup':str(positive),'negative_trueup':str(-positive),'fallback_shortfall':str(F(4,55))}}
Path(__file__).with_name('impairment-validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2));assert not out['failed']
