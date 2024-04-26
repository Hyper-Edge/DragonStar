from hyperedge.sdk.models import BaseData, DataRef
from dragon_star.models.data.tier import *


class CurrencyData(BaseData):
    Name: str
    Symbol: str
    Tier: DataRef[TierData]


CURR_DRAX = CurrencyData.define(
    Name='Drax',
    Symbol='DRX',
    Tier=TIER_U
)

CURR_GOLD = CurrencyData.define(
    Name='Gold',
    Symbol='GLD',
    Tier=TIER_R
)
