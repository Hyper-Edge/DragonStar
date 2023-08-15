from dragon_star.models.data.dragons.dragon import *
from dragon_star.models.dragons import *


BasicDragonCommonLadder = DragonLadder.new_ladder('BasicDragonCommonLadder')
exp = 100
step = 100
for lvl in range(1, 40):
    #FIXME
    BasicDragonCommonLadder.add_level(Exp=exp, Data=DragonLadderLevelData(id=f'xx{lvl}'))
    exp += step
    step += 100
