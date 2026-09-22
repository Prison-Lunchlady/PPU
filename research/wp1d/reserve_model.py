"""WP1D exact synthetic stress diagnostics; not pricing/eligibility certification.

Inputs are explicitly assumed facts. No live feeds, trading, minting, or legal rules.
"""
from dataclasses import dataclass
from fractions import Fraction as F

def exact(x):
    if isinstance(x, (float, bool)):
        raise ValueError('binary float/bool not accepted')
    return F(x)

def nonnegative(x):
    x = exact(x)
    if x < 0: raise ValueError('negative quantity')
    return x

def fraction(x):
    x = nonnegative(x)
    if x > 1: raise ValueError('fraction outside [0,1]')
    return x

def liability(units, target, fixed):
    fixed = nonnegative(fixed)
    units = nonnegative(units)
    if target is None: return None
    target = exact(target)
    if target <= 0: raise ValueError('nonpositive target')
    if (target*10**18).denominator != 1: raise ValueError('target exceeds 18-place binding grid')
    return units * target + fixed

def zero_coupon_ratio(years, old_yield, new_yield):
    """Exact semiannual zero-coupon ratio; not a coupon TIPS or floor valuation.

    Maturity is held fixed to isolate instantaneous rate repricing.
    """
    periods = nonnegative(years) * 2
    if periods.denominator != 1: raise ValueError('half-year grid required')
    y0, y1 = exact(old_yield), exact(new_yield)
    if min(y0,y1) <= -2: raise ValueError('invalid discount base')
    return ((1+y0/2)/(1+y1/2)) ** int(periods)

@dataclass(frozen=True)
class Asset:
    asset_id: str
    market_usd: object
    accessible_after_hours: object = 0
    encumbered_usd: object = 0
    shock_factor: object = 1
    sale_discount: object = 0
    authenticated: bool = False
    ownership_verified: bool = False
    stale: bool = True
    secured_claim_id: str = ''
    secured_obligation_usd: object = 0
    maturity_after_hours: object = None
    maturity_receipt_usd: object = None

@dataclass(frozen=True)
class OtherClaim:
    claim_id: str
    amount_usd: object

def reserve_view(assets, horizon_hours, inventory_complete=True):
    """Distinct market, stress-realizable and horizon values. Never sum them.

    Encumbered USD is a disjoint market-value portion, removed before shocks.
    Secured debt is explicitly paired by unique claim ID. Allocated covered debt
    is min(reserved market portion, paired debt) solely for a conditional pool
    reconciliation. This does NOT establish legal netting, priority, or separability.
    """
    horizon = nonnegative(horizon_hours)
    if type(inventory_complete) is not bool: raise ValueError('explicit completeness required')
    seen=set(); claims=set(); inventory=F(0); eligible=F(0); stressed=F(0); liquid=F(0); exceptions=[]
    encumbered=F(0); secured_debt=F(0); allocated_debt=F(0); stress_allocated_debt=F(0); excluded_free=F(0)
    for a in assets:
        if not a.asset_id or a.asset_id in seen: raise ValueError('duplicate/missing asset identity')
        seen.add(a.asset_id)
        m,e=nonnegative(a.market_usd),nonnegative(a.encumbered_usd)
        delay=nonnegative(a.accessible_after_hours)
        factor=nonnegative(a.shock_factor); discount=fraction(a.sale_discount)
        if e > m: raise ValueError('encumbrance exceeds market value')
        if (a.maturity_after_hours is None)!=(a.maturity_receipt_usd is None):
            raise ValueError('maturity date and scenario receipt must be paired')
        maturity=None if a.maturity_after_hours is None else nonnegative(a.maturity_after_hours)
        receipt=None if a.maturity_receipt_usd is None else nonnegative(a.maturity_receipt_usd)
        if receipt and m==0: raise ValueError('cannot allocate receipt from zero mark')
        debt=nonnegative(a.secured_obligation_usd)
        if e or debt:
            if not a.secured_claim_id or a.secured_claim_id in claims or debt==0:
                raise ValueError('explicit unique paired secured debt required')
            claims.add(a.secured_claim_id)
        elif a.secured_claim_id: raise ValueError('orphan secured claim identity')
        if any(type(x) is not bool for x in (a.authenticated,a.ownership_verified,a.stale)):
            raise ValueError('explicit evidence flags required')
        encumbered+=e; secured_debt+=debt
        inventory += m
        if not a.authenticated or not a.ownership_verified or a.stale:
            exceptions.append(a.asset_id); excluded_free+=m-e; continue
        free=m-e
        allocated_debt+=min(e,debt)
        stress_allocated_debt+=min(e*factor*(1-discount),debt)
        eligible += free
        value=free*factor*(1-discount)
        stressed += value
        # Choose a single scenario route for this snapshot, never both. Maturity
        # amount is an explicit scenario receipt, including default/access loss;
        # it is not automatically derived from par or a market factor.
        if maturity is not None and maturity<=horizon:
            liquid+=receipt*(free/m) if m else 0
        elif delay <= horizon:
            liquid += value
    return dict(inventory_market=inventory,eligible_market=eligible,
                stressed_realizable=stressed,horizon_available=liquid,
                encumbered_market=encumbered,paired_secured_debt=secured_debt,
                conditionally_allocated_secured_debt=allocated_debt,
                stress_allocated_secured_debt=stress_allocated_debt,
                secured_claim_ids=sorted(claims),excluded_free_market=excluded_free,
                complete=inventory_complete and not exceptions,exceptions=exceptions)

def adequacy(view, ppu_liability, other_claims=(), benchmark='NORMAL',due_outflows=None,operating_cash=0):
    if benchmark not in ('NORMAL','TEMPORARY_CARRY','BENCHMARK_IMPAIRED'):
        raise ValueError('unknown benchmark state')
    seen=set(view['secured_claim_ids']); other=F(0)
    for c in other_claims:
        if not c.claim_id or c.claim_id in seen: raise ValueError('duplicate/missing claim ID')
        seen.add(c.claim_id);other+=nonnegative(c.amount_usd)
    free_pool_claims=other+view['paired_secured_debt']-view['conditionally_allocated_secured_debt']
    stress_pool_claims=other+view['paired_secured_debt']-view['stress_allocated_secured_debt']
    op=nonnegative(operating_cash)
    due=None if due_outflows is None else nonnegative(due_outflows)
    if ppu_liability is None:
        return dict(status='LIABILITY_UNDETERMINED',ratio=None,free_pool_market_buffer=None,production_activation=False)
    L=nonnegative(ppu_liability)
    status={'NORMAL':'CONDITIONAL_REFERENCE_ONLY','TEMPORARY_CARRY':'CARRIED_TARGET_REFERENCE_ONLY','BENCHMARK_IMPAIRED':'BENCHMARK_IMPAIRED_REFERENCE_ONLY'}[benchmark]
    if not view['complete']:status='INVENTORY_UNDETERMINED'
    return dict(status=status,
                ratio=view['eligible_market']/L if L else None,
                stressed_ratio=view['stressed_realizable']/L if L else None,
                full_inventory_reference_buffer=view['inventory_market']-L-other-view['paired_secured_debt'] if view['complete'] else None,
                free_pool_market_buffer=view['eligible_market']-L-free_pool_claims,
                free_pool_stress_buffer=view['stressed_realizable']-L-stress_pool_claims,
                horizon_gap=None if due is None else view['horizon_available']-due-op,
                free_pool_other_claims=free_pool_claims,
                benchmark=benchmark, production_activation=False)

def liquidity_gap(available, outflows, operating=0):
    return nonnegative(available)-nonnegative(outflows)-nonnegative(operating)

def repo_default_value(receivable, collateral_market, gap_loss, liquidation_cost):
    """Conditional collateral-only recovery; excess collateral not a second asset.

    No separate unsecured deficiency recovery, repo interest, margin calls or netting.
    """
    r,c=nonnegative(receivable),nonnegative(collateral_market)
    return min(r,c*(1-fraction(gap_loss))*(1-fraction(liquidation_cost)))

def run_sale(cash, security_mark, payout, discount):
    """One aggregate synthetic sale then final payout; no priority or queue choice.

    Returns unsatisfied demand, sold mark and irreversible loss. Does not reduce
    any legal claim merely because available assets fail to meet demand.
    """
    c,s,p=map(nonnegative,(cash,security_mark,payout)); d=fraction(discount)
    need=max(F(0),p-c)
    sold=min(s,need/(1-d)) if d<1 else F(0)
    proceeds=sold*(1-d)
    paid=min(p,c+proceeds)
    return dict(paid=paid,unpaid=p-paid,sold_mark=sold,sale_loss=sold-proceeds,
                residual_assets=c+proceeds-paid+s-sold,
                residual_liquidation_value=c+proceeds-paid+(s-sold)*(1-d))
