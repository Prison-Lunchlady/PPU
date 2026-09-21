from liability_model import Ledger,binding
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import json

checks={};examples={}
def ck(n,v):checks[n]=bool(v)
def base():
 l=Ledger('synthetic-v1');l.apply('issue',1,'RECOGNIZE_UNITS',units='100');return l
def accepted(basis):
 l=base();l.apply('request',2,'REQUEST',claim='r',units='20');l.apply('accept',3,'ACCEPT',claim='r',basis=basis,target='1.10');return l
def reject(name,l,*a,**kw):
 before=deepcopy(l.__dict__)
 try:l.apply(*a,**kw);ck(name,False)
 except (ValueError,KeyError):ck(name,l.__dict__==before)

l=base();ck('issuance_recognition_110',l.measure('1.10')['L_PPU']=='110')
l.apply('request',2,'REQUEST',claim='r',units='20');ck('request_does_not_reduce_liability',l.measure('1.10')['L_PPU']=='110')
l.apply('cancel',3,'CANCEL_REQUEST',claim='r');ck('unaccepted_cancel_restores_units',l.live==100 and not l.requests)
for basis,up,down in [('FIXED','118','94'),('INDEXED','120','90')]:
 l=accepted(basis);ck(basis+'_acceptance_conserves_110',l.measure('1.10')['L_PPU']=='110')
 ck(basis+'_inflation',l.measure('1.20')['L_PPU']==up)
 ck(basis+'_deflation',l.measure('0.90')['L_PPU']==down)
 ck(basis+'_no_double_count',l.live==80 and not l.requests and len(l.accepted)==1)
 examples[basis]={'at_acceptance':l.measure('1.10'),'after_rise':l.measure('1.20'),'after_fall':l.measure('0.90')}
 amount='11' if basis=='FIXED' else '10'
 l.apply('partial',4,'DISCHARGE',claim='r',amount=amount,effective=True)
 ck(basis+'_partial_residual_units',l.accepted['r']['units']==10)
 ck(basis+'_partial_conserves_original_units',l.issued==l.live+l.accepted['r']['units']+l.discharged)
 ck(basis+'_duplicate_discharge_idempotent',not l.apply('partial',4,'DISCHARGE',claim='r',amount=amount,effective=True))
 reject(basis+'_conflicting_duplicate_rejected',l,'partial',4,'DISCHARGE',claim='r',amount='1',effective=True)
 reject(basis+'_over_discharge_atomic',l,'bad',5,'DISCHARGE',claim='r',amount='1000',effective=True)
 reject(basis+'_unproved_payment_atomic',l,'fail',5,'DISCHARGE',claim='r',amount='1',effective=False)
 reject(basis+'_accepted_cancellation_not_invented',l,'cancel-accepted',5,'CANCEL_REQUEST',claim='r')
 l.apply('finish',5,'DISCHARGE',claim='r',amount=amount,effective=True)
 ck(basis+'_final_zero_queue',not l.accepted and l.discharged==20)
 reject(basis+'_second_discharge_new_id_rejected',l,'again',6,'DISCHARGE',claim='r',amount='1',effective=True)

l=base();before=l.measure('1.10');l.apply('xfer',2,'TRANSFER',units='30');ck('transfer_no_aggregate_change',l.measure('1.10')==before)
reject('over_request_atomic',l,'too-many',3,'REQUEST',claim='r',units='101')
reject('negative_recognition_rejected',l,'negative',3,'RECOGNIZE_UNITS',units='-1')
reject('float_amount_rejected',l,'float',3,'RECOGNIZE_UNITS',units=0.1)
reject('out_of_order_rejected',l,'old',1,'RECOGNIZE_UNITS',units='1')
l.apply('request',3,'REQUEST',claim='r',units='20')
reject('unknown_queue_type_rejected',l,'unknown',4,'ACCEPT',claim='r',basis='DEFAULT',target='1.10')
reject('duplicate_claim_request_rejected',l,'duplicate',4,'REQUEST',claim='r',units='1')
reject('burn_is_not_discharge',l,'burn',4,'BURN',units='20')
ck('unavailable_target_not_zero',l.measure(None)['L_PPU'] is None)
ck('incomplete_inventory_explicit',l.measure('1')['total_completeness']=='TOTAL_UNDETERMINED')
ck('other_obligations_separate',l.measure('1',other_known=7)['known_subtotal']=='107')
impaired=l.measure('1.10','BENCHMARK_IMPAIRED');ck('impairment_does_not_erase_liability',impaired['L_PPU']=='110')
ck('structural_remedy_stays_open',impaired['Q023']=='OPEN_PRODUCTION_ACTIVATION_BLOCKER')
ck('no_trueup_field_or_added_face',set(impaired)==set(l.measure('1.10')) and impaired['L_PPU']==l.measure('1.10')['L_PPU'])
l=Ledger('fixed-only');l.apply('i',1,'RECOGNIZE_UNITS',units='20');l.apply('r',2,'REQUEST',claim='r',units='20');l.apply('a',3,'ACCEPT',claim='r',basis='FIXED',target='1.10')
ck('known_fixed_face_without_target',l.measure(None)['L_PPU']=='22')
l.apply('p',4,'DISCHARGE',claim='r',amount='0.01',effective=True);ck('fractional_residual_not_rounded_away',l.accepted['r']['face']==F('21.99') and l.accepted['r']['units']==F('21.99')/F('1.10'))
ck('exact_18place_binding_used',binding('1.000000000000000001')*10==F('10.00000000000000001'))
for invalid in ['0','-1','NaN','1e0','1.0000000000000000001']:
 try:binding(invalid);ck('invalid_target_'+invalid,False)
 except ValueError:ck('invalid_target_'+invalid,True)
# Snapshot decomposition includes cross term, and accepted-fixed cancellation is not neutral.
ck('simultaneous_delta_cross_term',F(120)*F('1.2')-F(100)*F('1.1')==F(100)*F('.1')+F('1.2')*20)
ck('original_units_return_can_change_face',20*F('1.2')!=22)
ck('value_equivalent_return_changes_units',F(22)/F('1.2')!=20)
ck('queue_double_count_counterexample',100*F('1.1')+22!=80*F('1.1')+22)
ck('asset_shortfall_is_not_liability_reduction',F(100)-F(90)==10)
z=base();z.apply('r',2,'REQUEST',claim='old',units='1');z.apply('c',3,'CANCEL_REQUEST',claim='old')
reject('historical_claim_id_cannot_be_reused',z,'reuse',4,'REQUEST',claim='old',units='1')
try:z.measure('1',other_known=0.1);ck('floating_other_amount_rejected',False)
except ValueError:ck('floating_other_amount_rejected',True)
result={'scope':'synthetic claim-accounting checks only; not legal, reserve, production or independent economic validation','checks':checks,'passed':sum(checks.values()),'failed':[k for k,v in checks.items() if not v],'examples':examples}
Path(__file__).with_name('liability-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':result['passed'],'failed':result['failed']}));assert not result['failed']
