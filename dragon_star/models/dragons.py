from dragon_star.dragon_star.sdk.models import BaseData, DataModel
from dragon_star.dragon_star.models.data.dragons.dragon import *

from dragon_star.dragon_star.sdk.models.progression import ProgressionLadder


class Dragon(DataModel):
    Level: int
    Exp: int
    Data: DataRef[DragonData]


class DragonLadderLevelData(BaseData):
    pass


DragonLadder = ProgressionLadder(
    Entity=Dragon,
    IsExperienceBased=True,
    LadderLevelData=DragonLadderLevelData)
