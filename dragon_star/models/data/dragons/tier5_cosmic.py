from dragon_star.models.data.affinity import *
from dragon_star.models.data.tier import *
from dragon_star.models.data.dragons.dragon import DragonData
from dragon_star.models.data.ladders.dragons.tier1 import BasicDragonCommonLadder


D_CONCEPTUAL_DRAGON = DragonData.define(
    Name='Conceptual Dragon',
    ShortDescription='',
    Description='',
    Tier=TIER_SSR,
    Ladder=BasicDragonCommonLadder
)
