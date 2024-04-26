import typing

from hyperedge.sdk.models import BaseData


class TierData(BaseData):
    Name: str
    Symbol: str


TIER_C = TierData.define(id='common', Symbol='C', Name='Common')
TIER_U = TierData.define(id='uncommon', Symbol='U', Name='Uncommon')
TIER_R = TierData.define(id='rare', Symbol='R', Name='Rare')
TIER_SR = TierData.define(id='super_rare', Symbol='SR', Name='SuperRare')
TIER_SSR = TierData.define(id='ultra_rare', Symbol='SSR', Name='UltraRare')

ALL_TIERS = TierData.instances()


def prev_tier(tier: TierData) -> typing.Optional[TierData]:
    for jj, t in enumerate(ALL_TIERS[1:]):
        if t == tier:
            return ALL_TIERS[jj]
    return None


def next_tier(tier: TierData) -> typing.Optional[TierData]:
    for jj, t in enumerate(ALL_TIERS[:-1]):
        if t == tier:
            return ALL_TIERS[jj+1]
    return None
