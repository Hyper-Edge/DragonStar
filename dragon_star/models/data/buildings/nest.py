from dragon_star.models.data.buildings.base import *
from dragon_star.models.data.ladders.buildings import *


BULIDING_NEST = NestBuildingData.define(
    Name='Nest',
    ShortDescription='',
    Description='',
    Ladder=NestBaseLadder
)