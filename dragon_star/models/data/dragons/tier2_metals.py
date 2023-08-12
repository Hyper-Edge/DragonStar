from dragon_star.models.data.affinity import *
from dragon_star.models.data.tier import *
from dragon_star.models.data.dragons.dragon import DragonData
from dragon_star.models.data.metals import MetalData


################################################################################
# Metallic Dragons
################################################################################
for metal_data in MetalData.iter_instances(predicate=lambda m: m.HasMetallicDragon):
    #
    DragonData.define(
        id=f'dragon_metallic_{metal_data.id}_dragon',
        Name=f'{metal_data.Name} Dragon',
        ShortDescription='',
        Description='',
        Tier=TIER_U,
        Affinity=AFFINITY_ELEMENTS)
    #
    DragonData.define(
        id=f'dragon_metallic_{metal_data.id}_drake',
        Name=f'{metal_data.Name} Drake',
        ShortDescription='',
        Description='',
        Tier=TIER_U,
        Affinity=AFFINITY_ELEMENTS)
