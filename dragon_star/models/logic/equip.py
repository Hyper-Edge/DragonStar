import typing

from dragon_star.sdk.models.types import Ulid
from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.handler import Handler


class EquipDragonReq(_BaseModel):
    DragonId: Ulid
    SlotId: Ulid
    EquipmentId: Ulid


class EquipDragonResp(_BaseModel):
    Success: bool


EquipDragonHandler = Handler(
    Name='EquipDragon',
    RequestClass=EquipDragonReq,
    ResponseClass=EquipDragonResp)


EquipDragonHandler.Code = """
return new EquipDragonResp { Success = false };
"""

#FIXME
_FIXME_EquipDragonHandler = """
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var dragon =  user.GetDragon(req.DragonId);

var dragonEquipment = user.GetDragonEquippable(req.EquipmentId);
var dragonEquipmentData = GameDb.GetDragonEquippableData(dragonEquipment.Data);

var dragonData = GameDb.GetDragonData(dragon.Data);

var failResp = new EquipDragonResp { Success = false };

var slot = dragon.GetEquipmentSlot(req.SlotId);
var slotData = GameDb.GetDragonEquipSlotData(slot.Data);
if (slotData.Id != (int)dragonEquipmentData.Slot)
{
    return failResp;
}

slot.EquipmentId = dragonEquipment.Id;
user.UpdateDragon(dragon);

return new EquipDragonResp { Success = true };
"""
