from dragon_star.models.data.dragons.dragon import *
from dragon_star.models.dragons import *
from dragon_star.models.data.ladders.dragons.tier1 import BasicDragonCommonLadder
from dragon_star.models.data.currency import *

from hyperedge.sdk.models.reward import Reward
from hyperedge.sdk.utils import to_underscore


for dragon_type in BASIC_DRAGONS:
    retire_reward = Reward()
    retire_reward.add(CURR_DRAX, 100)
    DragonData.define(
        id=to_underscore(dragon_type),
        Name=dragon_type,
        ShortDescription='',
        Description='',
        EquipSlots=[],
        RetirementReward=retire_reward,
        Tier=TIER_C,
        Ladder=BasicDragonCommonLadder)
