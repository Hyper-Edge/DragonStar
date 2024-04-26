import typing

from hyperedge.sdk.models.types import *
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


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

