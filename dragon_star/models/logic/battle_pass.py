import typing

from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


class ClaimBattlePassRewardsReq(_BaseModel):
    BpId: Ulid
    Level: int


class ClaimBattlePassRewardsResp(_BaseModel):
    Success: bool


class ClaimBattlePassAllRewardsReq(_BaseModel):
    BpId: Ulid


class ClaimBattlePassAllRewardsResp(_BaseModel):
    Success: bool


ClaimBattlePassRewardsHandler = Handler(
    Name='ClaimBattlePassRewards',
    RequestClass=ClaimBattlePassRewardsReq,
    ResponseClass=ClaimBattlePassRewardsResp)


ClaimBattlePassAllRewardsHandler = Handler(
    Name='ClaimBattlePassAllRewards',
    RequestClass=ClaimBattlePassAllRewardsReq,
    ResponseClass=ClaimBattlePassAllRewardsResp)

