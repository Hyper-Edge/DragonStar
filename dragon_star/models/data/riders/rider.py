from dragon_star.dragon_star.sdk.models import BaseData, DataRef, Reward
from dragon_star.dragon_star.models.data.affinity import AffinityData
from dragon_star.dragon_star.models.data.tier import TierData


class RiderData(BaseData):
    Name: str
    ShortDescription: str
    Description: str
    Affinity: DataRef[AffinityData]
    Tier: DataRef[TierData]
    RetirementReward: Reward
