import typing

from dragon_star.sdk.models.types import Ulid
from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.handler import Handler


class ClaimAchievementRewardReq(_BaseModel):
    AchievementId: Ulid


class ClaimAchievementRewardResp(_BaseModel):
    Success: bool


ClaimAchievementRewardHandler = Handler(
    Name='ClaimAchievementReward',
    RequestClass=ClaimAchievementRewardReq,
    ResponseClass=ClaimAchievementRewardResp)

ClaimAchievementRewardHandler.Code = """
var failResp = new ClaimAchievementRewardResp { Success = false; };

var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var achievement = user.GetAchievement(req.AchievementId);
if (achievement.Claimed)
{
    return failResp;
}

var achievementData = GameDb.GetAchievementData(achievement.Data);

if (!RewardService.Give(user, achievementData.Reward))
{
    return failResp;
}

achievement.Claimed = true;
user.UpdateAchievement(achievement);

return new ClaimAchievementRewardResp { Success = true; };
"""
