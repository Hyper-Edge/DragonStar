from dragon_star.dragon_star.models.data.dragons.dragon import *
from dragon_star.dragon_star.models.data.slots.equip_slots.element_slots import *


################################################################################
# Elemental Dragons
################################################################################
for el_data in ElementData.instances():
    for dr_type in BASIC_DRAGONS:
        DragonData.define(
            Name=f'{el_data.Name} {dr_type}',
            Tier=TIER_U,
            Slots=[DE_ELEMENT_STONE],
            Affinity=AFFINITY_ELEMENTS)


D_SKYHIGH_DRAGON = DragonData.define(
    Name='Skyhigh Dragon',
    Tier=TIER_U,
    Affinity=AFFINITY_ELEMENTS)
