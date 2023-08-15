from dragon_star.models.data.dragons.dragon import *
from dragon_star.models.dragons import *
from dragon_star.models.data.ladders.dragons.tier1 import BasicDragonCommonLadder
from dragon_star.sdk.utils import to_underscore


for dragon_type in BASIC_DRAGONS:
    DragonData.define(
        id=to_underscore(dragon_type),
        Name=dragon_type,
        ShortDescription='',
        Description='',
        EquipSlots=[],
        Tier=TIER_C,
        Ladder=BasicDragonCommonLadder)
