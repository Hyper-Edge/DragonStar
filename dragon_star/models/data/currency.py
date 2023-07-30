from dragon_star.dragon_star.sdk.models import BaseData, DataRef
from dragon_star.dragon_star.models.data.tier import *


class CurrencyData(BaseData):
    Name: str
    Symbol: str
    Tier: DataRef[TierData]


CURR_DRAX = CurrencyData.define(
    Name='Drax',
    Symbol='DRX',
    TIER_C=TIER_U
)

CURR_GOLD = CurrencyData.define(
    Name='Gold',
    Symbol='GLD',
    TIER_C=TIER_R
)
