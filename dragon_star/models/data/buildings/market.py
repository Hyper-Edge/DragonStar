from dragon_star.models.data.buildings.base import *
from dragon_star.models.data.ladders.buildings import *


BUILDING_MARKET = MarketBuildingData.define(
    Name='Market',
    ShortDescription='',
    Description='',
    Ladder=MarketBaseLadder
)
