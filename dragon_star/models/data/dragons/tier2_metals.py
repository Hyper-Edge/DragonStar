from dragon_star.dragon_star.models.data.affinity import *
from dragon_star.dragon_star.models.data.tier import *
from dragon_star.dragon_star.models.data.dragons.dragon import DragonData
from dragon_star.dragon_star.models.data.metals import MetalData


################################################################################
# Metallic Dragons
################################################################################
for metal_data in MetalData.iter_instances(predicate=lambda m: m.HasMetallicDragon):
    #
    DragonData.define(
        Name=f'{metal_data.Name} Dragon',
        Tier=TIER_U,
        Affinity=AFFINITY_ELEMENTS)
    #
    DragonData.define(
        Name=f'{metal_data.Name} Drake',
        Tier=TIER_U,
        Affinity=AFFINITY_ELEMENTS)
