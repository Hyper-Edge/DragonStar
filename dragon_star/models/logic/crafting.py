import typing

from dragon_star.sdk.models.types import Ulid
from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.handler import Handler


class CraftDragonEquipmentReq(_BaseModel):
    CraftId: int


class CraftDragonEquipmentResp(_BaseModel):
    Success: bool


CraftDragonEquipmentHandler = Handler(
    Name='CraftDragonEquipment',
    RequestClass=CraftDragonEquipmentReq,
    ResponseClass=CraftDragonEquipmentResp)


CraftDragonEquipmentHandler.Code = """
var failResp = new CraftDragonEquipmentResp { Success = false };
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var craftSuccess = await GameContext.CraftItems(user, (CraftSystem.Types)req.CraftId);
if (!craftSuccess)
{
    return failResp;
}
return new CraftDragonEquipmentResp { Success = true };
"""
