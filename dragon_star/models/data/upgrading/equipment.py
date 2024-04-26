from hyperedge.sdk.models import BaseData, DataRef
from dragon_star.models.data.element import *
from dragon_star.models.data.affinity import *
from dragon_star.models.data.tier import *


class DragonEquippableExpMaterialData(BaseData):
    Name: str
    Description: str
    Value: int
    Tier: DataRef[TierData]
    Affinity: DataRef[AffinityData]
    DraxPerValue: int = optional_field(0)


################################################################################
# Elemental-based equippable upgrades
################################################################################
for el_data in ElementData.instances():
    for tier_data in [TIER_R, TIER_SR, TIER_SSR]:
        DragonEquippableExpMaterialData.define(
            id=f'dragon_equip_exp_mat_elem_{el_data.id}_{tier_data.id}',
            Name='Elemental Essence Crystal',
            Description='',
            Tier=tier_data,
            Value=100,
            Affinity=AFFINITY_ELEMENTS,
            DraxPerValue=0
        )

_AFFINITY_TO_CRYSTAL_NAME = {
    AFFINITY_ELEMENTS.id: "Elemental Essences",
    AFFINITY_TECHNO.id: "NanoMachine",
    AFFINITY_BIO.id: "Life",
    AFFINITY_PSYCHO.id: "Mind",
    AFFINITY_AETHER.id: "Void"
}
################################################################################
for a_idx, affinity_data in enumerate(AffinityData.instances()):
    for tier_data in [TIER_R, TIER_SR, TIER_SSR]:
        DragonEquippableExpMaterialData.define(
            id=f'dragon_equip_exp_mat_{affinity_data.id}_{tier_data.id}',
            Name=f'{_AFFINITY_TO_CRYSTAL_NAME[affinity_data.id]} Crystal',
            Description='',
            Tier=tier_data,
            Value=100,
            Affinity=AFFINITY_TECHNO,
            DraxPerValue=1 if a_idx == 0 else a_idx*2
        )
