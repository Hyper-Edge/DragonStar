from hyperedge.sdk.models.data import BaseData, DataRef
from hyperedge.sdk.models.reward import Reward
from hyperedge.sdk.models.progression import GenericLadder


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

