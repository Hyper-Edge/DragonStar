import typing

from dragon_star.dragon_star.sdk.models.types import Ulid
from dragon_star.dragon_star.sdk.models.base import _BaseModel
from dragon_star.dragon_star.sdk.models.handler import Handler


class ClaimQuestRewardReq(_BaseModel):
    QuestId: Ulid


class ClaimQuestRewardResp(_BaseModel):
    Success: bool


ClaimQuestRewardHandler = Handler(
    Name='ClaimQuestReward',
    RequestClass=ClaimQuestRewardReq,
    ResponseClass=ClaimQuestRewardResp)

ClaimQuestRewardHandler.Code = """
var failResp = new ClaimQuestRewardResp { Success = false; };

var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var quest = user.GetQuest(req.QuestId);

if (!quest.Finished)
{
    return failResp;
}

if (quest.RewardClaimed)
{
    return failResp;
}

var questData = GameDb.GetQuestData(quest.Data);
if (!RewardService.Give(user, questData.Reward))
{
    return failResp;
}

quest.RewardClaimed = true;
user.UpdateQuest(quest);

return new ClaimQuestRewardResp { Success = true; };
"""