from dragon_star.sdk.models.data import BaseData, DataRef
from dragon_star.sdk.models.reward import Reward
from dragon_star.sdk.models.progression import GenericLadder


class BuildingData(BaseData):
    Name: str
    ShortDescription: str
    Description: str
    Ladder: DataRef[GenericLadder]


class AcademyBuildingData(BuildingData):
    pass


class CastleBuildingData(BuildingData):
    pass


class IncubatorBuildingData(BuildingData):
    pass


class MarketBuildingData(BuildingData):
    pass


class MiningBuildingData(BuildingData):
    pass


class NestBuildingData(BuildingData):
    pass

