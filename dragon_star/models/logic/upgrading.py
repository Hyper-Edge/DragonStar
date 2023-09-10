import typing

from dragon_star.sdk.models.types import *
from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.handler import Handler


class UpgradeDragonReq(_BaseModel):
    DragonId: Ulid
    MaterialIds: typing.List[int]
    MaterialAmounts: typing.List[UInt64]


class UpgradeDragonResp(_BaseModel):
    Success: bool


UpgradeDragonHandler = Handler(
    Name='UpgradeDragon',
    RequestClass=UpgradeDragonReq,
    ResponseClass=UpgradeDragonResp)

UpgradeDragonHandler.Code = """
var failResp = new UpgradeDragonResp { Success = false };
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var dragon =  user.GetDragon(req.DragonId);

ulong addExp = 0;
var itemsToUse = new Dictionary<Ulid, ulong>();
for (int i = 0; i < req.MaterialIds.Count; i++)
{
    var matData = GameDb.GetDragonExpMaterialData((DragonExpMaterialData.Types)req.MaterialIds[i]);
    if ((matData is null) || !user.HasItems(matData.Uid, req.MaterialAmounts[i]))
    {
        return failResp;
    }
    itemsToUse.Add(matData.Uid, (ulong)req.MaterialAmounts[i]);
    addExp += (ulong)matData.Value * req.MaterialAmounts[i];
}

if (!user.RemoveItems(itemsToUse))
{
    return failResp;
}

var dragonData = GameDb.GetDragonData(dragon.Data);
var ladderData = GameDb.GetExpLadderData(dragonData.Ladder);

var (newLevel, newExp) = ladderData.ExpLadder.GetLevel((uint)dragon.Level, (ulong)(dragon.Exp + (int)addExp));
dragon.Level = (int)newLevel;
dragon.Exp = (int)newExp;
user.UpdateDragon(dragon);

return new UpgradeDragonResp { Success = true };
"""


class UpgradeDragonEquipmentReq(_BaseModel):
    DragonId: Ulid
    MaterialIds: typing.List[int]
    MaterialAmounts: typing.List[UInt64]


class UpgradeDragonEquipmentResp(_BaseModel):
    Success: bool


UpgradeDragonEquipmentHandler = Handler(
    Name='UpgradeDragonEquipment',
    RequestClass=UpgradeDragonEquipmentReq,
    ResponseClass=UpgradeDragonEquipmentResp)

UpgradeDragonEquipmentHandler.Code = """
return new UpgradeDragonEquipmentResp { Success = true };
"""


class UpgradeBuildingReq(_BaseModel):
    BuildingId: Ulid
    MaterialIds: typing.List[int]
    MaterialAmounts: typing.List[UInt64]


class UpgradeBuildingResp(_BaseModel):
    Success: bool


UpgradeBuildingHandler = Handler(
    Name='UpgradeBuilding',
    RequestClass=UpgradeBuildingReq,
    ResponseClass=UpgradeBuildingResp)

UpgradeBuildingHandler.Code = """
var failResp = new UpgradeBuildingResp { Success = false };

var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var building =  user.GetBuilding(req.BuildingId);

var upgradeHelper = new UpgradeLadderHelper(GameContext, GameDb);
if (!upgradeHelper.UpgradeLevel(user, building))
{
    return failResp;
}

return new UpgradeBuildingResp { Success = true };
"""
