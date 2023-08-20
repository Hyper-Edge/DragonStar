from dragon_star.models.data.buildings.base import *

from dragon_star.sdk.models.progression import ProgressionLadder
from dragon_star.sdk.models import DataModel, DataRef


class BuildingBase(DataModel):
    Level: int = 0


#######################################
class BuildingCastle(BuildingBase):
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
class BuildingMarket(BuildingBase):
    Data: DataRef[MarketBuildingData]


class BuildingMarketLadderLevelData(BaseData):
    pass


MarketBuildingLadder = ProgressionLadder(
    Entity=BuildingMarket,
    IsExperienceBased=False,
    LadderLevelData=BuildingMarketLadderLevelData)


#######################################
class BuildingMine(BuildingBase):
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
class BuildingIncubator(BuildingBase):
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
class BuildingAcademy(BuildingBase):
    Data: DataRef[AcademyBuildingData]


class BuildingAcademyLadderLevelData(BaseData):
    pass

AcademyBuildingLadder = ProgressionLadder(
    Entity=BuildingAcademy,
    IsExperienceBased=False,
    LadderLevelData=BuildingAcademyLadderLevelData)


#######################################
class BuildingForgery(BuildingBase):
    pass


#######################################
# Nest
#######################################
class BuildingNest(BuildingBase):
    Data: DataRef[NestBuildingData]


class BuildingNestLadderLevelData(BaseData):
    pass


NestBuildingLadder = ProgressionLadder(
    Entity=BuildingNest,
    IsExperienceBased=False,
    LadderLevelData=BuildingNestLadderLevelData)
