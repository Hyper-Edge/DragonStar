from dragon_star.models.data.dragons.dragon import *
from dragon_star.models.dragons import *
from dragon_star.sdk.utils import to_underscore

for dragon_type in BASIC_DRAGONS:
    DragonData.define(
        id=to_underscore(dragon_type),
        Name=dragon_type,
        ShortDescription='',
        Description='',
        Tier=TIER_C)

BasicDragonCommonLadder = DragonLadder.new_ladder('BasicDragonCommonLadder')
#assert False, str(BasicDragonCommonLadder)
exp = 100
step = 100
for lvl in range(1, 40):
    #FIXME
    BasicDragonCommonLadder.add_level(DragonLadder.ladder_level_data_class(id=f'xx{lvl}', Exp=exp, Data=DragonLadderLevelData(id=f'xx{lvl}')))
    exp += step
    step += 100
