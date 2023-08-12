from dragon_star.sdk.models import BaseData
from dragon_star.sdk.models.reward import Reward


class AchievementData(BaseData):
    Name: str
    Description: str
    Reward: Reward
