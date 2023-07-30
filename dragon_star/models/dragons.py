from dragon_star.dragon_star.sdk.models import DataModel
from dragon_star.dragon_star.models.data.dragons.dragon import *


class Dragon(DataModel):
    Data: DataRef[DragonData]
