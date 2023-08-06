from dragon_star.dragon_star.sdk.models import DataModel, DataRef
from dragon_star.dragon_star.models.data.equips.equippables.equippable import DragonEquippableData


class DragonEquippable(DataModel):
    Exp: int
    Level: int
    Data: DataRef[DragonEquippableData]
