"""WP1B executable mathematical reference; not production or authentication code.

Validated evidence/hold facts are inputs. See 01 and 10 for their required proof.
No network, contracts, funds or transactions. Standard Python library only.
"""
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from calendar import monthrange
from fractions import Fraction as F
import hashlib
import json
import re

UTC = timezone.utc

def instant(s):
    t = datetime.fromisoformat(s.replace('Z', '+00:00'))
    if t.tzinfo is None:
        raise ValueError('timezone required')
    return t.astimezone(UTC)

def shift(m, n):
    y, mo = map(int, m.split('-'))
    q = y * 12 + mo - 1 + n
    return f'{q // 12:04d}-{q % 12 + 1:02d}'

def first(m):
    return instant(m + '-01T00:00:00Z')

def cutoff(m):
    return first(m) - timedelta(days=1)

def rounded(x, places=18):
    """Exact rational, nearest decimal, ties to even; no binary floating point."""
    x = F(x)
    if x < 0:
        return '-' + rounded(-x, places)
    n, rem = divmod(x.numerator * 10**places, x.denominator)
    if rem * 2 > x.denominator or (rem * 2 == x.denominator and n % 2):
        n += 1
    return f'{n // 10**places}.{n % 10**places:0{places}d}'

@dataclass(frozen=True)
class Packet:
    month: str
    value: str
    edition: str
    path: str
    received: datetime
    published: datetime
    authenticated: bool = True
    series: str = 'CUUR0000SA0'
    original_edition: bool = True
    # Exact normalization is a validated input; default original base.
    factor: str = '1'
    normalization_verified: bool = True
    release_hash: str = ''
    source_url: str = ''
    seasonally_adjusted: bool = False
    base_label: str = '1982-1984=100'

def edition_key(p):
    # Friendly edition label has no authority; canonical publisher artifact does.
    return (p.series,p.month,p.published.astimezone(UTC).isoformat(),p.release_hash)

def packet_key(p):
    item={**p.__dict__,'received':p.received.isoformat(),'published':p.published.isoformat()}
    return hashlib.sha256(json.dumps(item,sort_keys=True).encode()).hexdigest()

def packets_before_resolution(packets,events,at,inclusive=False):
    rejected={e.identity for e in events if e.validated and e.kind=='REJECT_PACKET'
              and (e.received<at or (inclusive and e.received==at))}
    return [p for p in packets if packet_key(p) not in rejected]

def decimal(s):
    if not re.fullmatch(r'(0|[1-9][0-9]*)(\.[0-9]+)?',s):
        raise ValueError('positive plain decimal required')
    v=F(s)
    if v<=0: raise ValueError('positive value required')
    return v

def select(month, boundary, packets, configured_paths=frozenset({'A','B','C'}),include_boundary=False):
    candidates = []
    failures=set()
    for p in packets:
        if p.month != month or p.received>boundary or (p.received==boundary and not include_boundary):
            continue
        if p.path not in configured_paths:
            failures.add('UNCONFIGURED_PATH');continue
        if not p.authenticated:
            failures.add('AUTHENTICATION_FAILED');continue
        if p.series != 'CUUR0000SA0' or p.seasonally_adjusted:
            failures.add('WRONG_IDENTITY');continue
        if not p.normalization_verified:
            failures.add('NORMALIZATION_UNVERIFIED');continue
        if not p.original_edition:
            failures.add('CORRECTION_EDITION');continue
        if not re.fullmatch('[a-f0-9]{64}',p.release_hash) or not p.source_url:
            failures.add('ARTIFACT_INCOMPLETE');continue
        if p.published > p.received or p.published < first(shift(p.month,1)):
            failures.add('INVALID_PUBLICATION_TIME')
            continue
        try:
            v = decimal(p.value) * F(p.factor)
        except (ValueError, ZeroDivisionError):
            failures.add('INVALID_VALUE');continue
        if F(p.factor) <= 0:
            failures.add('INVALID_VALUE');continue
        candidates.append((p, v))
    identities = {(edition_key(p), v) for p, v in candidates}
    if len(identities) > 1:
        return None, 'CONFLICT'
    if not candidates or len({p.path for p, _ in candidates}) < 2:
        priority=['NORMALIZATION_UNVERIFIED','CORRECTION_EDITION','WRONG_IDENTITY','INVALID_VALUE','INVALID_PUBLICATION_TIME','ARTIFACT_INCOMPLETE','AUTHENTICATION_FAILED','UNCONFIGURED_PATH']
        return None,next((s for s in priority if s in failures),'DELIVERY_INSUFFICIENT' if candidates else 'SOURCE_ABSENT')
    return candidates[0][1], 'ELIGIBLE'

@dataclass(frozen=True)
class Plan:
    month: str
    start: F
    end: F
    endpoint_month: str
    mode: str
    frozen_count: int
    reason: str

def plan(month, previous, base, packets, review_hold=False, configured_paths=frozenset({'A','B','C'})):
    expected = shift(month, -2)
    start = F(base) if previous is None else previous.end
    value, reason = select(expected, cutoff(month), packets,configured_paths)
    if review_hold:
        value, reason = None, 'INDEX_REVIEW_HOLD'
    if value is None:
        return Plan(month, start, start,
                    shift(month, -3) if previous is None else previous.endpoint_month,
                    'FROZEN', 1 + (previous.frozen_count if previous else 0), reason)
    normal = previous is None or previous.endpoint_month == shift(month, -3)
    return Plan(month, start, value, expected,
                'NORMAL' if normal else 'CATCH_UP', 0, 'ELIGIBLE')

def initialize(month, packets, review_hold=False,configured_paths=frozenset({'A','B','C'})):
    base, reason = select(shift(month, -3), cutoff(month), packets,configured_paths)
    endpoint, _ = select(shift(month, -2), cutoff(month), packets,configured_paths)
    if base is None or endpoint is None or review_hold:
        raise ValueError('NOT_ACTIVE: genesis evidence incomplete or held')
    return base, plan(month, None, base, packets,configured_paths=configured_paths)

def value(plan_, at, base):
    if at.tzinfo is None:
        raise ValueError('timezone required')
    at = at.astimezone(UTC)
    if at.strftime('%Y-%m') != plan_.month:
        raise ValueError('wrong plan month')
    d = at.day
    days = monthrange(at.year, at.month)[1]
    ref = plan_.start + F(d - 1, days) * (plan_.end - plan_.start)
    exact = ref / F(base)
    output = rounded(exact)
    return {'exact': str(exact), 'reference_index': str(ref),
            'binding': output if F(output) > 0 else None,
            'status': 'VALUE' if F(output) > 0 else 'UNREPRESENTABLE',
            'display': rounded(exact, 6) if F(output)>0 else None, 'mode': plan_.mode}

def issuance_data_ok(plan_, at, monitor_times, unresolved_adverse=False,configured_paths=frozenset({'A','B','C'})):
    # monitor_times maps distinct validated clean path IDs to finalized instants.
    fresh = sum(path in configured_paths and t < at and at-t < timedelta(days=1) for path,t in monitor_times.items())
    return plan_.mode == 'NORMAL' and fresh >= 2 and not unresolved_adverse

# Normative event folding (machine-readable algorithm in addition to functions):
EVENT_RULES = {
  'plan_prefix': 'use only finalized events with receipt_time < cutoff(month)',
  'monthly_order': 'generate every Gregorian month from G, no skipped state transitions',
  'hold_open': ['relevant official correction', 'material methodology change',
                'discontinuation', 'uncertain base conversion'],
  'hold_close': 'explicit prospective authorized original-terms clearance only',
  'correction': 'archive corrected edition, never overwrite original packet',
  'late_event': 'never modify a previously computed plan prefix',
  'reassessment': '3 consecutive frozen plans latch public review-required flag',
  'reassessment_clear': 'recorded primary review disposition only',
  'numeric_hold': 'effective first not-yet-committed month; no cancellation of committed plans',
  'health_hold': 'effective immediately upon finalized adverse event',
  'not_active': 'before G or failed initialization, no target',
}

@dataclass(frozen=True)
class ControlEvent:
    """Validated index-review fact; identity refers to the exact hold resolved."""
    received: datetime
    kind: str  # OPEN, RESOLVE or REJECT_PACKET (proved original-artifact mismatch)
    identity: str
    validated: bool = True

def holds_before(events, at, inclusive=False):
    active=set()
    # For simultaneous events OPEN wins over RESOLVE (fail closed).
    for e in sorted(events,key=lambda e:(e.received,0 if e.kind=='RESOLVE' else 1,e.identity)):
        if not e.validated or e.received>at or (e.received==at and not inclusive):
            continue
        if e.kind=='OPEN': active.add(e.identity)
        elif e.kind=='RESOLVE': active.discard(e.identity)
        elif e.kind=='REJECT_PACKET': pass
        else: raise ValueError('unknown control event')
    return active

def replay(genesis_month, at, packets, control_events=(), monitor_times=None,
           unresolved_adverse=False, reassessment_dispositions=(),
           configured_paths=frozenset({'A','B','C'})):
    """Research replay from valid genesis, no skipped months or backdated receipts.

    Caller supplies an immutable authenticated log; this function does not create it.
    Dispositions are validated primary-review instants, never monetary substitutions.
    """
    if at.tzinfo is None: raise ValueError('timezone required')
    at=at.astimezone(UTC)
    if at<first(genesis_month): return {'status':'NOT_ACTIVE','issuanceDataOK':False}
    # Raw packet errors cannot vote. Validated relevant publisher corrections and
    # unresolved official normalization facts do create holds without hand-passed flags.
    derived=list(control_events)
    seen=set()
    for p0 in sorted(packets,key=lambda p:p.received):
        if not p0.authenticated or p0.path not in configured_paths or p0.series!='CUUR0000SA0' or p0.seasonally_adjusted:
            continue
        if p0.month<shift(genesis_month,-3): continue
        cause='CORRECTION' if not p0.original_edition else ('NORMALIZATION' if not p0.normalization_verified else None)
        if cause:
            ident=cause+':'+p0.month+':'+p0.release_hash
            if ident not in seen:
                derived.append(ControlEvent(p0.received,'OPEN',ident));seen.add(ident)
    initial_hold=bool(holds_before(derived,cutoff(genesis_month)))
    try:
        base, p=initialize(genesis_month,packets_before_resolution(packets,derived,cutoff(genesis_month)),initial_hold,configured_paths)
    except ValueError:
        return {'status':'NOT_ACTIVE','issuanceDataOK':False,'reason':'GENESIS_EVIDENCE_OR_HOLD'}
    plans=[p]
    m=genesis_month
    reassessment_at=None
    impaired_episode=False
    while m<at.strftime('%Y-%m'):
        m=shift(m,1)
        p=plan(m,p,base,packets_before_resolution(packets,derived,cutoff(m)),bool(holds_before(derived,cutoff(m))),configured_paths)
        plans.append(p)
        # Three consecutive freezes OR three non-normal plans in trailing six.
        trigger=p.frozen_count>=3 or sum(x.mode!='NORMAL' for x in plans[-6:])>=3
        if trigger and not impaired_episode: reassessment_at=cutoff(m)
        impaired_episode=trigger
    result=value(p,at,base)
    current_packets=packets_before_resolution(packets,derived,at,True)
    current_conflict=any(select(mo,at,current_packets,configured_paths,True)[1]=='CONFLICT'
                         for mo in {x.month for x in current_packets if x.month>=shift(genesis_month,-3)})
    result['issuanceDataOK']=result['status']=='VALUE' and issuance_data_ok(
        p,at,monitor_times or {},unresolved_adverse or current_conflict or bool(holds_before(derived,at,True)),configured_paths)
    result['reassessment_required']=reassessment_at is not None and not any(
        reassessment_at<t<=at for t in reassessment_dispositions)
    result['plans']=[{'month':x.month,'start':str(x.start),'end':str(x.end),
                      'endpoint_month':x.endpoint_month,'mode':x.mode,
                      'reason':x.reason,'frozen_count':x.frozen_count} for x in plans]
    prefix=[{**x.__dict__,'received':x.received.isoformat(),'published':x.published.isoformat()}
            for x in packets if x.received<cutoff(m)]
    controls=[{**x.__dict__,'received':x.received.isoformat()} for x in derived if x.received<cutoff(m)]
    serialized=json.dumps({'packets':sorted(prefix,key=lambda x:json.dumps(x,sort_keys=True)),
                           'controls':sorted(controls,key=lambda x:json.dumps(x,sort_keys=True))},sort_keys=True)
    result['plan_prefix_hash']=hashlib.sha256(serialized.encode()).hexdigest()
    result['cutoff']=cutoff(m).isoformat()
    result['source_observation_month']=p.endpoint_month
    result['vintage_ids']=sorted({str(edition_key(x)) for x in packets if x.month==p.endpoint_month and x.received<cutoff(m) and x.original_edition and x.authenticated and x.path in configured_paths})
    result['health_status']='DATA_OK_NECESSARY_ONLY' if result['issuanceDataOK'] else 'ISSUANCE_DATA_BLOCKED'
    return result
