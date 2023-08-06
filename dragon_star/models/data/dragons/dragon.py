from dragon_star.dragon_star.models.data.affinity import *
from dragon_star.dragon_star.models.data.tier import *
from dragon_star.dragon_star.models.data.element import *
from dragon_star.dragon_star.models.data.slots.equip_slots import DragonEquipSlotData
from dragon_star.dragon_star.sdk.models.reward import Reward


BASIC_DRAGONS = ('Drake', 'Dragon', 'Wyvern', 'Wyrm', 'Lindwurm')


class DragonData(BaseData):
    Name: str
    ShortDescription: str
    Description: str
    Affinity: typing.Optional[DataRef[AffinityData]]
    Element: typing.Optional[DataRef[ElementData]]
    Tier: DataRef[TierData]
    EquipSlots: typing.List[DragonEquipSlotData] = list()
    Clonable: typing.Optional[bool] = False
    RetirementReward: typing.Optional[Reward]


D_PHOEINX = DragonData.define(
    Name='Phoenix',
    Tier=TIER_R,
    Affinity=AFFINITY_AETHER)

D_COSMIC_PHOEINX = DragonData.define(
    Name='Cosmic Phoenix',
    Tier=TIER_SSR,
    Affinity=AFFINITY_AETHER)
