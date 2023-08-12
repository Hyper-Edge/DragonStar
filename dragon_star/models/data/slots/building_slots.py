from dragon_star.sdk.models import BaseData, DataRef
from dragon_star.models.data.tier import *


class CityBuildingSlotData(BaseData):
    Name: str
    Description: str


BUILDING_SLOT_CASTLE = CityBuildingSlotData.define(
    Name='Castle',
    Description='')

BUILDING_SLOT_MINE = CityBuildingSlotData.define(
    Name='Mine',
    Description='')

BUILDING_SLOT_INCUBATOR = CityBuildingSlotData.define(
    Name='Incubator',
    Description='')

BUILDING_SLOT_NEST = CityBuildingSlotData.define(
    Name='Nest',
    Description='')

BUILDING_SLOT_MARKET = CityBuildingSlotData.define(
    Name='Market',
    Description='')

BUILDING_SLOT_ACADEMY = CityBuildingSlotData.define(
    Name='Academy',
    Description='')

BUILDING_SLOT_FORGERY = CityBuildingSlotData.define(
    Name='Forgery',
    Description='')

BUILDING_SLOT_DEPOT = CityBuildingSlotData.define(
    Name='Depot',
    Description='')

BUILDING_SLOT_HUB = CityBuildingSlotData.define(
    Name='Hub',
    Description='')
