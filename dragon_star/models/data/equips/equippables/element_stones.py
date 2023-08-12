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

for ti, tier_data in enumerate(ALL_TIERS):
    for el_data in ElementData.instances():
        if tier_data == TIER_C:
            continue
        stone_data = DragonEquippableData.define(
            Name=f'{tier_data.Name} {el_data.Name} Stone',
            Description='',
            Slot=DE_ELEMENT_STONE,
            Tier=tier_data)
        #
        STONES_BY_ELEMENT[el_data][tier_data] = stone_data
        minor_tier = prev_tier(tier_data)
        if minor_tier and minor_tier != TIER_C:
            req_stone = STONES_BY_ELEMENT[el_data][minor_tier]
            craft_rule = CraftRule(f'craft_rule_{stone_data.id}')
            craft_rule.require(req_stone, 3)
            craft_rule.produce(stone_data, 1)


DE_ELEMENT_STONE = DragonEquippableData.define(
    Name=f'Elements Stone',
    Description='',
    Slot=DE_ELEMENT_STONE,
    Tier=TIER_SSR
)
DE_ELEMENT_STONE_CRAFT = CraftRule(f'craft_rule_{DE_ELEMENT_STONE.id}')
for el_data in ElementData.instances():
    DE_ELEMENT_STONE_CRAFT.require(STONES_BY_ELEMENT[el_data][TIER_SSR])
DE_ELEMENT_STONE_CRAFT.produce(DE_ELEMENT_STONE)
