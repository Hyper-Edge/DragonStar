from dragon_star.models.data.buildings.base import *
from dragon_star.models.data.ladders.buildings import *


BULIDING_ACADEMY = AcademyBuildingData.define(
    Name='Academy',
    ShortDescription='',
    Description='',
    Ladder=AcademyBaseLadder
)
