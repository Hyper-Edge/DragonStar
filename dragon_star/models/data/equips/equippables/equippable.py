import typing

from hyperedge.sdk.models import *
from dragon_star.models.data.tier import TierData
from dragon_star.models.data.slots.equip_slots.equip_slot import DragonEquipSlotData


class DragonEquippableData(BaseData):
    Name: str
    Description: str
    Slot: DataRef[DragonEquipSlotData]
    Tier: DataRef[TierData]
    RecycleReward: typing.Optional[Reward] = optional_field(None)
