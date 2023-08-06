from dragon_star.dragon_star.models.data.dragons.dragon import *
from dragon_star.dragon_star.models.dragons import *

for dragon_type in BASIC_DRAGONS:
    DragonData.define(
        Name=dragon_type,
        Tier=TIER_C)

BasicDragonCommonLadder = DragonLadder.new_ladder('BasicDragonCommonLadder')
exp = 100
step = 100
for lvl in range(1, 40):
    BasicDragonCommonLadder.add_level(BasicDragonCommonLadder.ladder_level_data_class(Exp=exp))
    exp += step
    step += 100
