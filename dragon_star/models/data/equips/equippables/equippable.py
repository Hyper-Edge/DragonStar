from dragon_star.dragon_star.sdk.models import BaseData, DataRef
from dragon_star.dragon_star.models.data.tier import TierData
from dragon_star.dragon_star.models.data.slots.equip_slots.equip_slot import DragonEquipSlotData


class DragonEquippableData(BaseData):
    Name: str
    Description: str
    Slot: DataRef[DragonEquipSlotData]
    Tier: DataRef[TierData]
