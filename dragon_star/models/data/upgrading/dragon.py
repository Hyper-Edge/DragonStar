from dragon_star.dragon_star.sdk.models import BaseData, DataRef
from dragon_star.dragon_star.models.data.element import *
from dragon_star.dragon_star.models.data.affinity import *
from dragon_star.dragon_star.models.data.tier import *


class DragonExpMaterialData(BaseData):
    Name: str
    Description: str
    Value: int
    Tier: DataRef[TierData]
    Affinity: DataRef[AffinityData]
    DraxPerValue: typing.Optional[int] = 0


_AFFINITY_TO_CORENAME = {
    AFFINITY_ELEMENTS.id: "Elemental",
    AFFINITY_TECHNO.id: "NanoMachine",
    AFFINITY_BIO.id: "Life",
    AFFINITY_PSYCHO.id: "Mind",
    AFFINITY_AETHER.id: "Void"
}
################################################################################
for a_idx, affinity_data in enumerate(AffinityData.instances()):
    for tier_data in [TIER_R, TIER_SR, TIER_SSR]:
        DragonExpMaterialData.define(
            Name=f'{_AFFINITY_TO_CORENAME[affinity_data.id]} Core',
            Description='',
            Tier=tier_data,
            Value=100,
            Affinity=affinity_data,
            DraxPerValue=1 if a_idx == 0 else a_idx*2
        )
