import typing

from dragon_star.sdk.models.types import Ulid
from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.handler import Handler


class EquipDragonReq(_BaseModel):
    DragonId: Ulid
    SlotIdx: int
    EquipmentId: Ulid


class EquipDragonResp(_BaseModel):
    Success: bool


EquipDragonHandler = Handler(
    Name='EquipDragon',
    RequestClass=EquipDragonReq,
    ResponseClass=EquipDragonResp)


EquipDragonHandler.Code = """
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var dragon =  user.GetDragon(req.DragonId);
var dragonData = GameDb.GetDragonData(dragon.Data);
if (dragon.EquipSlots.Count == 0)
{
    for (int i = 0; i < dragonData.EquipSlots.Count; i++)
    {
        dragon.EquipSlots.Add(Ulid.Empty);
    }
}

var dragonEquipment = user.GetDragonEquippable(req.EquipmentId);
var dragonEquipmentData = GameDb.GetDragonEquippableData(dragonEquipment.Data);

var failResp = new EquipDragonResp { Success = false };

var slotDataId = dragonData.EquipSlots[req.SlotIdx];
var slotData = GameDb.GetDragonEquipSlotData(slotDataId);
if (slotData.Id != (int)dragonEquipmentData.Slot)
{
    return failResp;
}

dragon.EquipSlots[req.SlotIdx] = dragonEquipment.Id;
user.UpdateDragon(dragon);

return new EquipDragonResp { Success = true };
"""
