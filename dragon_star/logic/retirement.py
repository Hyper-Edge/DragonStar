from dragon_star.dragon_star.sdk.models.types import Ulid
from dragon_star.dragon_star.sdk.models.base import _BaseModel
from dragon_star.dragon_star.sdk.models.handler import Handler


class RetireDragonReq(_BaseModel):
    DragonId: Ulid


class RetireDragonResp(_BaseModel):
    Success: bool


RetireDragonHandler = Handler(
    Name='RetireDragon',
    RequestClass=RetireDragonReq,
    ResponseClass=RetireDragonResp)

RetireDragonHandler.Code = """
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var dragon =  user.GetDragon(req.DragonId);

var failResp = new RetireDragonResp { Success = false; }

if (dragon is null)
{
    return failResp;
}

var dragonData = GameDb.GetDragonData(dragon.Data);
if (!GameContext.RemoveDragon(dragon))
{
    return failResp;
}

if (!RewardService.Give(user, dragonData.RetirementReward))
{
    return failResp;
}

return new RetireDragonResp { Success = true; };
"""


class RecycleDragonEquipmentReq(_BaseModel):
    DragonEquipmentId: Ulid


class RecycleDragonEquipmentResp(_BaseModel):
    Success: bool


RecycleDragonEquipmentHandler = Handler(
    Name='RecycleDragonEquipment',
    RequestClass=RecycleDragonEquipmentReq,
    ResponseClass=RecycleDragonEquipmentResp)

RecycleDragonEquipmentHandler.Code = """
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var de =  user.GetDragonEquipment(req.DragonEquipmentId);

var failResp = new RecycleDragonEquipmentResp { Success = false; }

if (de is null)
{
    return failResp;
}

var deData = GameDb.GetDragonEquipmentData(de.Data);
if (!GameContext.RemoveDragonEquipment(de))
{
    return failResp;
}

if (!RewardService.Give(user, deData.RecycleReward))
{
    return failResp;
}

return new RecycleDragonEquipmentResp { Success = true; };
"""