import typing

from hyperedge.sdk.models import BaseData, DataModel, StructModel
from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.progression import ProgressionLadder

from dragon_star.models.data.dragons.dragon import *


class Dragon(DataModel):
    Level: int
    Exp: int
    Data: DataRef[DragonData]
    EquipSlots: typing.List[Ulid]


class DragonLadderLevelData(BaseData):
    pass


DragonLadder = ProgressionLadder(
    Entity=Dragon,
    IsExperienceBased=True,
    LadderLevelData=DragonLadderLevelData)
