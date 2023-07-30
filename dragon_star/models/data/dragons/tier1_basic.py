from dragon_star.dragon_star.models.data.dragons.dragon import *

for dragon_type in BASIC_DRAGONS:
    DragonData.define(
        Name=dragon_type,
        Tier=TIER_C)
