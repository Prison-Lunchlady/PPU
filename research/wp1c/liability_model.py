"""Synthetic economic-claim ledger, not a token, settlement system or legal ledger."""
from fractions import Fraction as F
from copy import deepcopy
import re

def positive(x):
    if isinstance(x,(float,bool)): raise ValueError('exact amount required')
    n=F(x)
    if n<=0: raise ValueError('positive amount required')
    return n

def binding(x):
    if not isinstance(x,str) or not re.fullmatch(r'(0|[1-9][0-9]*)(\.[0-9]{1,18})?',x):
        raise ValueError('binding target must be exact decimal, at most 18 places')
    return positive(x)

class Ledger:
    def __init__(self,scope):
        if not scope: raise ValueError('scope required')
        self.scope=scope;self.live=F(0);self.requests={};self.accepted={}
        self.issued=F(0);self.discharged=F(0);self.events={};self.sequence=-1
        self.claim_ids=set()

    def apply(self,event_id,seq,kind,**data):
        if not event_id or not isinstance(seq,int) or isinstance(seq,bool):raise ValueError('event identity/order required')
        payload=(seq,kind,data)
        if event_id in self.events:
            if self.events[event_id]!=payload:raise ValueError('conflicting event ID')
            return False
        if seq<=self.sequence:raise ValueError('non-finalized event order')
        candidate=deepcopy(self)
        candidate._apply(kind,data)
        candidate.events[event_id]=deepcopy(payload);candidate.sequence=seq
        candidate.assert_invariants()
        self.__dict__=candidate.__dict__
        return True

    def _apply(self,kind,d):
        if kind=='RECOGNIZE_UNITS':
            q=positive(d['units']);self.live+=q;self.issued+=q
        elif kind=='REQUEST':
            q=positive(d['units']);key=d['claim']
            if not key or key in self.claim_ids or q>self.live:raise ValueError('invalid request')
            self.live-=q;self.requests[key]=q;self.claim_ids.add(key)
        elif kind=='CANCEL_REQUEST':
            self.live+=self.requests.pop(d['claim'])
        elif kind=='ACCEPT':
            key=d['claim'];q=self.requests[key];basis=d['basis']
            if basis not in {'FIXED','INDEXED'}:raise ValueError('queue denomination undecided')
            p=binding(d['target'])
            self.accepted[key]={'basis':basis,'units':q,'face':q*p if basis=='FIXED' else None,'price':p}
            del self.requests[key]
        elif kind=='DISCHARGE':
            a=self.accepted[d['claim']]
            if d.get('effective') is not True:raise ValueError('effective discharge fact required')
            x=positive(d['amount'])
            if a['basis']=='FIXED':
                if x>a['face']:raise ValueError('over-discharge')
                q=x/a['price'];a['face']-=x
            else:
                q=x
                if q>a['units']:raise ValueError('over-discharge')
            a['units']-=q;self.discharged+=q
            if a['units']==0:del self.accepted[d['claim']]
        elif kind=='TRANSFER':
            if positive(d['units'])>self.live:raise ValueError('insufficient LIVE units')
            # Aggregate ownership change only; individual balances not modeled.
        else:raise ValueError('unmodeled economic event')

    def assert_invariants(self):
        assert self.live>=0 and all(q>0 for q in self.requests.values())
        assert not set(self.requests)&set(self.accepted)
        assert all(a['units']>0 for a in self.accepted.values())
        assert all(a['face']==a['units']*a['price'] for a in self.accepted.values() if a['basis']=='FIXED')
        assert self.issued==self.live+sum(self.requests.values())+sum(a['units'] for a in self.accepted.values())+self.discharged

    def measure(self,target,benchmark_status='NORMAL',other_known=0,inventory_complete=False):
        if isinstance(other_known,(float,bool)):raise ValueError('exact other-obligation amount required')
        other=F(other_known)
        if other<0:raise ValueError('no negative offset to gross obligations')
        i=self.live+sum(self.requests.values())+sum(a['units'] for a in self.accepted.values() if a['basis']=='INDEXED')
        fixed=sum((a['face'] for a in self.accepted.values() if a['basis']=='FIXED'),F(0))
        p=None if target is None else binding(target)
        amount=None if p is None and i else i*(p or 0)+fixed
        return {'scope':self.scope,'indexed_units':str(i),'fixed_face_usd':str(fixed),
                'L_PPU':None if amount is None else str(amount),'other_known':str(other),
                'known_subtotal':None if amount is None else str(amount+other),
                'status':'INDEXED_COMPONENT_UNDETERMINED' if amount is None else 'REFERENCE_MEASURABLE',
                'total_completeness':'DECLARED_COMPLETE_INPUT' if inventory_complete else 'TOTAL_UNDETERMINED',
                'benchmark_status':benchmark_status,'Q023':'OPEN_PRODUCTION_ACTIVATION_BLOCKER'}
