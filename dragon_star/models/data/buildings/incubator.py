from dragon_star.models.data.buildings.base import *
from dragon_star.models.data.ladders.buildings import *


BUILDING_INCUBATOR = IncubatorBuildingData.define(
    Name='Incubator',
    ShortDescription='',
    Description='',
    Ladder=IncubatorBaseLadder
)