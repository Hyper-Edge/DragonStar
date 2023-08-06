import typing

from dragon_star.dragon_star.sdk.models.types import Ulid
from dragon_star.dragon_star.sdk.models.base import _BaseModel
from dragon_star.dragon_star.sdk.models.handler import Handler


class CraftDragonEquipmentReq(_BaseModel):
    CraftId: Ulid


class CraftDragonEquipmentResp(_BaseModel):
    Success: bool


CraftDragonEquipmentHandler = Handler(
    Name='CraftDragonEquipment',
    RequestClass=CraftDragonEquipmentReq,
    ResponseClass=CraftDragonEquipmentResp)


CraftDragonEquipmentHandler.Code = """
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);

var failResp = new CraftDragonEquipmentResp { Success = false; }

if (!CraftService.CraftItems(GameContext, user, req.CraftId))
{
    return failResp;
}

return new CraftDragonEquipmentResp { Success = true; };
"""