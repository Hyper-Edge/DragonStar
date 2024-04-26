from dragon_star.models.data.buildings.base import *

from hyperedge.sdk.models.progression import ProgressionLadder
from hyperedge.sdk.models import DataModel, DataRef


class Building(DataModel):
    Level: int = 0


#######################################
class BuildingCastle(Building):
    Data: DataRef[CastleBuildingData]


class BuildingCastleLadderLevelData(BaseData):
    pass


CastleBuildingLadder = ProgressionLadder(
    Entity=BuildingCastle,
    IsExperienceBased=False,
    LadderLevelData=BuildingCastleLadderLevelData)


#######################################
# Market
#######################################
class BuildingMarket(Building):
    Data: DataRef[MarketBuildingData]


class BuildingMarketLadderLevelData(BaseData):
    pass


MarketBuildingLadder = ProgressionLadder(
    Entity=BuildingMarket,
    IsExperienceBased=False,
    LadderLevelData=BuildingMarketLadderLevelData)


#######################################
class BuildingMine(Building):
    Data: DataRef[MiningBuildingData]


class BuildingMineLadderLevelData(BaseData):
    pass


MineBuildingLadder = ProgressionLadder(
    Entity=BuildingMine,
    IsExperienceBased=False,
    LadderLevelData=BuildingMineLadderLevelData)


#######################################
# Incubator
#######################################
class BuildingIncubator(Building):
    Data: DataRef[IncubatorBuildingData]


class BuildingIncubatorLadderLevelData(BaseData):
    pass


IncubatorBuildingLadder = ProgressionLadder(
    Entity=BuildingIncubator,
    IsExperienceBased=False,
    LadderLevelData=BuildingIncubatorLadderLevelData)


#######################################
# Academy
#######################################
class BuildingAcademy(Building):
    Data: DataRef[AcademyBuildingData]


class BuildingAcademyLadderLevelData(BaseData):
    pass

AcademyBuildingLadder = ProgressionLadder(
    Entity=BuildingAcademy,
    IsExperienceBased=False,
    LadderLevelData=BuildingAcademyLadderLevelData)


#######################################
class BuildingForgery(Building):
    pass


#######################################
# Nest
#######################################
class BuildingNest(Building):
    Data: DataRef[NestBuildingData]


class BuildingNestLadderLevelData(BaseData):
    pass


NestBuildingLadder = ProgressionLadder(
    Entity=BuildingNest,
    IsExperienceBased=False,
    LadderLevelData=BuildingNestLadderLevelData)
