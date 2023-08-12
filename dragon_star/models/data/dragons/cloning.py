from dragon_star.models.data.slots.equip_slots.element_slots import *
from dragon_star.models.data.equips.equippables.equippable import DragonEquippableData
from dragon_star.models.data.dragons import DragonData
from dragon_star.models.data.tier import *


################################################################################
# Clones of legendary Dragons
# * 1 tier weaker than originals
################################################################################
for dragon_data in DragonData.instances(predicate=lambda d: d.Clonable):
    clone = DragonData.define(
        Name=f'{dragon_data.Name} Clone',
        Affinity=dragon_data.Affinity,
        Tier=prev_tier(dragon_data.Tier)
    )
