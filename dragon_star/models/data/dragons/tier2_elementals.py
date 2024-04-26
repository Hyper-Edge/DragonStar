from dragon_star.models.data.dragons.dragon import *
from dragon_star.models.data.slots.equip_slots.element_slots import *
from hyperedge.sdk.utils import to_underscore
from .tier1_basic import BasicDragonCommonLadder


################################################################################
# Elemental Dragons
################################################################################
for el_data in ElementData.instances():
    for dr_type in BASIC_DRAGONS:
        DragonData.define(
            id=f'dragon_elem_{el_data.id}_{to_underscore(dr_type)}',
            Name=f'{el_data.Name} {dr_type}',
            ShortDescription='',
            Description='',
            Tier=TIER_U,
            EquipSlots=[DE_ELEMENT_STONE],
            Affinity=AFFINITY_ELEMENTS,
            Ladder=BasicDragonCommonLadder)


D_SKYHIGH_DRAGON = DragonData.define(
    id='skyhigh_dragon',
    Name='Skyhigh Dragon',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    Affinity=AFFINITY_ELEMENTS,
    Ladder=BasicDragonCommonLadder)
