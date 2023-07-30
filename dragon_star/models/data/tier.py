import typing

from dragon_star.dragon_star.sdk.models import BaseData


class TierData(BaseData):
    Name: str
    Symbol: str


TIER_C = TierData.define(Symbol='C', Name='Common')
TIER_U = TierData.define(Symbol='U', Name='Uncommon')
TIER_R = TierData.define(Symbol='R', Name='Rare')
TIER_SR = TierData.define(Symbol='SR', Name='SuperRare')
TIER_SSR = TierData.define(Symbol='SSR', Name='UltraRare')

ALL_TIERS = TierData.instances()


def prev_tier(tier: TierData) -> typing.Optional[TierData]:
    pass


def next_tier(tier: TierData) -> typing.Optional[TierData]:
    pass
