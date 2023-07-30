from dragon_star.dragon_star.models.data.element import *
from dragon_star.dragon_star.models.data.affinity import *
from dragon_star.dragon_star.models.data.tier import *


class RiderExpMaterialData(BaseData):
    Name: str
    Description: str
    Value: int
    Tier: DataRef[TierData]
    Affinity: DataRef[AffinityData]
    DraxPerValue: typing.Optional[int] = 0


_AFFINITY_TO_KNOWLEDGE_DRIVE_NAME = {
    AFFINITY_ELEMENTS.id: "Elemental Essences",
    AFFINITY_TECHNO.id: "NanoMachine",
    AFFINITY_BIO.id: "Life",
    AFFINITY_PSYCHO.id: "Mind",
    AFFINITY_AETHER.id: "Void"
}
################################################################################
for a_idx, affinity_data in enumerate(AffinityData.instances()):
    for tier_data in [TIER_R, TIER_SR, TIER_SSR]:
        RiderExpMaterialData.define(
            Name=f'{_AFFINITY_TO_KNOWLEDGE_DRIVE_NAME[affinity_data.id]} Knowledge Drive',
            Description='',
            Tier=tier_data,
            Value=100,
            Affinity=AFFINITY_TECHNO,
            DraxPerValue=1 if a_idx == 0 else a_idx*2
        )
