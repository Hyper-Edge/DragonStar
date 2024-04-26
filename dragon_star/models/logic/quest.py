import typing

from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


class ClaimQuestRewardReq(_BaseModel):
    QuestId: Ulid


class ClaimQuestRewardResp(_BaseModel):
    Success: bool


ClaimQuestRewardHandler = Handler(
    Name='ClaimQuestReward',
    RequestClass=ClaimQuestRewardReq,
    ResponseClass=ClaimQuestRewardResp)

