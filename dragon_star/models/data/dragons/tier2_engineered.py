from dragon_star.models.data.dragons import *
from dragon_star.models.data.tier import *
from dragon_star.models.data.slots.equip_slots.weapon_slots import *
from dragon_star.models.data.ladders.dragons.tier1 import BasicDragonCommonLadder


################################################################################
# Warrior Dragons
################################################################################
D_WARRIOR_DRAKE = DragonData.define(
    id='warrior_drake',
    Name='Warrior Drake',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    EquipSlots=[DE_TURRET_WEAPON],
    Ladder=BasicDragonCommonLadder
)

D_WARRIOR_VYWERN = DragonData.define(
    id='warrior_vywern',
    Name='Warrior Vywern',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    EquipSlots=[DE_AERIAL_WEAPON],
    Ladder=BasicDragonCommonLadder
)

D_WARRIOR_DRAGON = DragonData.define(
    id='warrior_dragon',
    Name='Warrior Dragon',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    EquipSlots=[DE_AERIAL_WEAPON],
    Ladder=BasicDragonCommonLadder
)

################################################################################
# Warrior Heavy Dragons
################################################################################
D_WARRIOR_HEAVY_DRAKE = DragonData.define(
    id='warrior_drake_heavy',
    Name='Warrior Drake',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    EquipSlots=[DE_TURRET_WEAPON, DE_TURRET_WEAPON],
    Ladder=BasicDragonCommonLadder
)

D_WARRIOR_HEAVY_VYWERN = DragonData.define(
    id='warrior_vywern_heavy',
    Name='Warrior Vywern',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    EquipSlots=[DE_AERIAL_WEAPON, DE_AERIAL_WEAPON],
    Ladder=BasicDragonCommonLadder
)

D_WARRIOR_HEAVY_DRAGON = DragonData.define(
    id='warrior_dragon_heavy',
    Name='Warrior Dragon',
    ShortDescription='',
    Description='',
    Tier=TIER_U,
    EquipSlots=[DE_AERIAL_WEAPON, DE_AERIAL_WEAPON],
    Ladder=BasicDragonCommonLadder
)
