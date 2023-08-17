import typing

from dragon_star.sdk.models import BaseData, DataModel, StructModel
from dragon_star.models.data.dragons.dragon import *
from dragon_star.sdk.models.types import Ulid

from dragon_star.sdk.models.progression import ProgressionLadder


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
