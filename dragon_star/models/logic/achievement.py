import typing

from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


class ClaimAchievementRewardReq(_BaseModel):
    AchievementId: Ulid


class ClaimAchievementRewardResp(_BaseModel):
    Success: bool


ClaimAchievementRewardHandler = Handler(
    Name='ClaimAchievementReward',
    RequestClass=ClaimAchievementRewardReq,
    ResponseClass=ClaimAchievementRewardResp)

