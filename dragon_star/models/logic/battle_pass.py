import typing

from dragon_star.sdk.models.types import Ulid
from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.handler import Handler


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

ClaimBattlePassRewardsHandler.Code = """
var failResp = new ClaimBattlePassRewardsResp { Success = false };

var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var bp = user.GetBattlePass(req.BpId);

if (!GameContext.ClaimBattlePassReward(bp, user, req.Level))
{
    return failResp;
}

return new ClaimBattlePassRewardsResp { Success = true };
"""


ClaimBattlePassAllRewardsHandler = Handler(
    Name='ClaimBattlePassAllRewards',
    RequestClass=ClaimBattlePassAllRewardsReq,
    ResponseClass=ClaimBattlePassAllRewardsResp)

ClaimBattlePassAllRewardsHandler.Code = """
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var bp = user.GetBattlePass(req.BpId);

var failResp = new ClaimBattlePassAllRewardsResp { Success = false };

if (!GameContext.ClaimAllBattlePassRewards(bp, user))
{
    return failResp;
}

return new ClaimBattlePassAllRewardsResp { Success = true };
"""
