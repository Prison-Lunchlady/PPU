"""Proposed impairment disclosure/control overlay; no claims or fallback execution.

Validated event facts are inputs, not evidence authenticated by this model.
The unchanged reference_model implements target arithmetic.
"""
from dataclasses import dataclass
from datetime import datetime
import re
from reference_model import replay, ControlEvent, cutoff, first, UTC, holds_before

@dataclass(frozen=True)
class ImpairmentEvent:
    received: datetime
    kind: str
    incident: str
    evidence_hash: str
    validated: bool = False
    same_benchmark: bool = False
    # Archived clean attestations at the clearance instant, not latest query data.
    monitor_times: tuple = ()
    clearance_adverse_free: bool = False

KINDS={'DISCONTINUED','MATERIAL_CONCEPT_CHANGE','SAME_BENCHMARK_RESTORED','CLEAR_IMPAIRMENT'}
OPEN={'DISCONTINUED','MATERIAL_CONCEPT_CHANGE'}

def replay_with_impairment(genesis_month, at, packets, impairment_events=(), **kwargs):
    if at.tzinfo is None: raise ValueError('timezone required')
    at=at.astimezone(UTC)
    events=[]
    for e in impairment_events:
        if e.received.tzinfo is None: raise ValueError('event timezone required')
        if e.kind not in KINDS: raise ValueError('unknown impairment event')
        if e.validated and e.incident and re.fullmatch('[a-f0-9]{64}',e.evidence_hash) and e.received<=at:
            events.append(e)
    # OPEN wins if evidence restoration/clearance shares a receipt instant.
    events.sort(key=lambda e:(e.received,1 if e.kind in OPEN else 0,e.incident,e.kind))
    controls=list(kwargs.get('control_events',()))
    active_structural={}
    structural=[]
    for e in events:
        key='STRUCTURAL:'+e.incident
        if e.kind in OPEN:
            # Repeated evidence for one active incident does not reset its clock.
            if key not in active_structural:
                active_structural[key]=e.received
                controls.append(ControlEvent(e.received,'OPEN',key))
                structural.append((e.received,key,'STRUCTURAL_CONFIRMED'))
        elif e.kind=='SAME_BENCHMARK_RESTORED' and e.same_benchmark and key in active_structural:
            controls.append(ControlEvent(e.received,'RESOLVE',key))
            del active_structural[key]
    options={**kwargs,'control_events':controls}
    result=replay(genesis_month,at,packets,**options)
    if result['status']=='NOT_ACTIVE':
        return {**result,'benchmark_status':'NOT_ACTIVE','impairment_incidents':[]}
    incidents=list(structural)
    previous_trigger=False
    plans=result['plans']
    for i,p in enumerate(plans):
        trigger=p['frozen_count']>=3 or sum(x['mode']!='NORMAL' for x in plans[max(0,i-5):i+1])>=3
        if trigger and not previous_trigger:
            incidents.append((cutoff(p['month']),'PERSISTENT:'+p['month'],'PERSISTENT_UNRESOLVED'))
        previous_trigger=trigger
    # Replay event-time facts so later evidence cannot retroactively clear an incident.
    timeline=[(t,1,k,kind) for t,k,kind in incidents]
    timeline += [(e.received,0,e.incident,e) for e in events if e.kind=='CLEAR_IMPAIRMENT']
    active={};clearances=[]
    for t,priority,key,event in sorted(timeline,key=lambda x:(x[0],x[1],x[2])):
        if priority==1:
            active[key]={'id':key,'since':t.isoformat(),'cause_class':event}
            continue
        if key not in active or not event.same_benchmark:continue
        r=replay(genesis_month,t,packets,**{**options,'monitor_times':dict(event.monitor_times),
                                          'unresolved_adverse':not event.clearance_adverse_free})
        if r['status']=='NOT_ACTIVE':continue
        started=[p for p in r['plans'] if first(p['month'])<=t]
        last=started[-2:]
        since=datetime.fromisoformat(active[key]['since'])
        # Original replay folds authenticated correction holds and conflicts too.
        clean=r['issuanceDataOK']
        after= len(last)==2 and all(p['mode']=='NORMAL' and cutoff(p['month'])>since for p in last)
        if clean and after:
            del active[key];clearances.append({'incident':key,'at':t.isoformat(),'evidence_hash':event.evidence_hash})
    status='BENCHMARK_IMPAIRED' if active else ('NORMAL' if result['mode']=='NORMAL' and result['issuanceDataOK'] else 'TEMPORARY_DATA_FAILURE')
    return {**result,'issuanceDataOK':result['issuanceDataOK'] and not active,
            'health_status':'BENCHMARK_IMPAIRED' if active else result['health_status'],
            'benchmark_status':status,'impairment_incidents':sorted(active.values(),key=lambda x:x['id']),
            'impairment_clearances':clearances,
            'policy_action':'NO_AUTOMATIC_TRUE_UP_OR_SUBSTITUTE'}
