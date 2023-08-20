from dragon_star.models.data.buildings.base import *
from dragon_star.models.data.ladders.buildings import *


BULIDING_MINE = MiningBuildingData.define(
    Name='Mine',
    ShortDescription='',
    Description='',
    Ladder=MineBaseLadder
)