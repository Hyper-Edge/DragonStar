from hyperedge.sdk.models import DataModel, DataRef
from dragon_star.models.data.equips.equippables.equippable import DragonEquippableData


class DragonEquippable(DataModel):
    Exp: int
    Level: int
    Data: DataRef[DragonEquippableData]
