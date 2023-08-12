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
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var dragon =  user.GetDragon(req.DragonId);

var itemsToUse = 

if (!user.HasItems())
{
    return new UpgradeDragonResp { Success = false }; 
} 

for (int i = 0; i < req.MaterialIds.Count; i++)
{{
    if (!this.Users.HasItems(user, \"{item_type_s}\", matIds[i], amounts[i]))
    {{
        return false;
    }}
}}

for (int i = 0; i < matIds.Count; i++)
{{
    var (success, itemsLeft) = this.Users.UseItems(user, \"{item_type_s}\", matIds[i], amounts[i]);
    if (!success)
    {{
        return false;
    }}
}}

ulong addExp = 0;
for (int i = 0; i < req.MaterialIds.Count; i++)
{{
    var matData = GameDb.GetDragonExpMaterial(req.MaterialIds[i]);
    addExp += matData.Value * req.MaterialAmounts[i];
}}

var dragonData = GameDb.GetDragonData(dragon.Data);
var dragonLadderData = GameDb.GetDragonLadderData((int)dragonData.Ladder);

dragon.Exp += addExp;
var (newLevel, newExp) = dragonLadderData.GetLevel(dragon.Level, dragon.Exp);
dragon.Level = newLevel;
dragon.Exp = newExp;

return new UpgradeDragonResp { Success = true; };
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
var user = await GameContext.GetUserAsync(GameContext.CurrentUserId);
var building =  user.GetBuilding(req.BuildingId);
var buildingData = GameDb.GetBuildingData(building.Data);
var buildingLevelLadderData = GameDb.GetBuildingLevelLadderData(buildingData.Ladder);

var failResp = new UpgradeBuildingResp { Success = false; };
//???
if (!UpgradeService.DoUpgrade(building))
{
    return failResp;
}

return new UpgradeBuildingResp { Success = true; };
"""