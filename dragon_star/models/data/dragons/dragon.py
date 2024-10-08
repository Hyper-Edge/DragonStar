from dragon_star.models.data.affinity import *
from dragon_star.models.data.tier import *
from dragon_star.models.data.element import *
from dragon_star.models.data.slots.equip_slots import DragonEquipSlotData
from hyperedge.sdk.models import UGCData
from hyperedge.sdk.models.reward import Reward
from hyperedge.sdk.models.progression import GenericExpLadder


BASIC_DRAGONS = ('Drake', 'Dragon', 'Wyvern', 'Wyrm', 'Lindwurm')


class DragonData(UGCData):
    Name: str
    ShortDescription: str
    Description: str
    Affinity: typing.Optional[DataRef[AffinityData]]
    Element: typing.Optional[DataRef[ElementData]]
    Tier: DataRef[TierData]
    EquipSlots: typing.List[DataRef[DragonEquipSlotData]] = optional_field(list())
    Clonable: bool = optional_field(False)
    RetirementReward: typing.Optional[Reward]
    Ladder: DataRef[GenericExpLadder]
