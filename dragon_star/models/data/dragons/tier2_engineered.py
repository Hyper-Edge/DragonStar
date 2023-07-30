from dragon_star.dragon_star.models.data.dragons import *
from dragon_star.dragon_star.models.data.tier import *
from dragon_star.dragon_star.models.data.slots.equip_slots.weapon_slots import *


################################################################################
# Warrior Dragons
################################################################################
D_WARRIOR_DRAKE = DragonData.define(
    Name='Warrior Drake',
    Description='',
    Tier=TIER_U,
    Slots=[DE_TURRET_WEAPON]
)

D_WARRIOR_VYWERN = DragonData.define(
    Name='Warrior Vywern',
    Description='',
    Tier=TIER_U,
    Slots=[DE_AERIAL_WEAPON]
)

D_WARRIOR_DRAGON = DragonData.define(
    Name='Warrior Dragon',
    Description='',
    Tier=TIER_U,
    Slots=[DE_AERIAL_WEAPON]
)

################################################################################
# Warrior Heavy Dragons
################################################################################
D_WARRIOR_HEAVY_DRAKE = DragonData.define(
    Name='Warrior Drake',
    Description='',
    Tier=TIER_U,
    Slots=[DE_TURRET_WEAPON, DE_TURRET_WEAPON]
)

D_WARRIOR_HEAVY_VYWERN = DragonData.define(
    Name='Warrior Vywern',
    Description='',
    Tier=TIER_U,
    Slots=[DE_AERIAL_WEAPON, DE_AERIAL_WEAPON]
)

D_WARRIOR_HEAVY_DRAGON = DragonData.define(
    Name='Warrior Dragon',
    Description='',
    Tier=TIER_U,
    Slots=[DE_AERIAL_WEAPON, DE_AERIAL_WEAPON]
)
