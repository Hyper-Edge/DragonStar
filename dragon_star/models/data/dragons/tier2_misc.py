from dragon_star.models.data.affinity import *
from dragon_star.models.data.tier import *
from dragon_star.models.data.dragons.dragon import DragonData
from dragon_star.models.data.ladders.dragons.tier1 import BasicDragonCommonLadder


################################################################################
# Misc Dragons
################################################################################
D_BUBBLE_DRAGON = DragonData.define(
    id='dragon_bubble',
    Name='Bubble Dragon',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    Affinity=AFFINITY_ELEMENTS,
    Ladder=BasicDragonCommonLadder)

D_SKULL_DRAGON = DragonData.define(
    id='dragon_skull',
    Name='Skull Dragon',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    Affinity=AFFINITY_PSYCHO,
    Ladder=BasicDragonCommonLadder)

D_FUTURE_DRAGON = DragonData.define(
    id='dragon_future',
    Name='Future Dragon',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    Affinity=AFFINITY_TECHNO,
    Ladder=BasicDragonCommonLadder)
