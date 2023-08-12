from dragon_star.sdk.models import BaseData, DataRef
from dragon_star.sdk.models.crafting import CraftRule

from dragon_star.models.data.slots.equip_slots.element_slots import *
from dragon_star.models.data.equips.equippables.equippable import DragonEquippableData
from dragon_star.models.data.element import ElementData
from dragon_star.models.data.tier import *


################################################################################
# Element stones for elemental dragons
################################################################################
STONES_BY_ELEMENT = {el_data: dict() for el_data in ElementData.instances()}


for el_data in ElementData.instances():
    for ti, tier_data in enumerate(ALL_TIERS):
        if tier_data == TIER_C:
            continue
        stone_data = DragonEquippableData.define(
            Name=f'{tier_data.Name} {el_data.Name} Stone',
            Description='',
            Slot=DE_ELEMENT_STONE,
            Tier=tier_data)
        #
        STONES_BY_ELEMENT[el_data][tier_data] = stone_data
        craft_rule = CraftRule(f'{stone_data}.Name crafting')
        craft_rule.require(stone_data, 3)
        craft_rule.produce(stone_data, 1)


DE_ELEMENT_STONE = DragonEquippableData.define(
    Name=f'Elements Stone',
    Description='',
    Slot=DE_ELEMENT_STONE,
    Tier=TIER_SSR
)
DE_ELEMENT_STONE_CRAFT = CraftRule('')
for el_data in ElementData.instances():
    DE_ELEMENT_STONE_CRAFT.require(STONES_BY_ELEMENT[el_data][TIER_SSR])
DE_ELEMENT_STONE_CRAFT.produce(DE_ELEMENT_STONE, 1)
