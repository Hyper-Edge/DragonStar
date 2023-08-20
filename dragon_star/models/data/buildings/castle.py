from dragon_star.models.data.buildings.base import *
from dragon_star.models.data.ladders.buildings import *


BULIDING_CASTLE = CastleBuildingData.define(
    Name='Castle',
    ShortDescription='',
    Description='',
    Ladder=CastleBaseLadder
)