from hyperedge.sdk.models import BaseData
from hyperedge.sdk.models.reward import Reward


class AchievementData(BaseData):
    Name: str
    Description: str
    Reward: Reward
