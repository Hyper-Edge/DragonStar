from dragon_star.sdk.models import BaseData, DataRef, DataModel
from dragon_star.models.data.achievement import AchievementData


class Achievement(DataModel):
    Claimed: bool
    Data: DataRef[AchievementData]
