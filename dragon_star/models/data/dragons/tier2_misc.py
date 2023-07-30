from dragon_star.dragon_star.models.data.affinity import *
from dragon_star.dragon_star.models.data.tier import *
from dragon_star.dragon_star.models.data.dragons.dragon import DragonData


################################################################################
# Misc Dragons
################################################################################
D_BUBBLE_DRAGON = DragonData.define(
    Name='Bubble Dragon',
    Tier=TIER_U,
    Affinity=AFFINITY_ELEMENTS)

D_SKULL_DRAGON = DragonData.define(
    Name='Skull Dragon',
    Tier=TIER_U,
    Affinity=AFFINITY_PSYCHO)

D_FUTURE_DRAGON = DragonData.define(
    Name='Future Dragon',
    Tier=TIER_U,
    Affinity=AFFINITY_TECHNO)
