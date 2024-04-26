import typing

from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


class CraftDragonEquipmentReq(_BaseModel):
    CraftId: int


class CraftDragonEquipmentResp(_BaseModel):
    Success: bool


CraftDragonEquipmentHandler = Handler(
    Name='CraftDragonEquipment',
    RequestClass=CraftDragonEquipmentReq,
    ResponseClass=CraftDragonEquipmentResp)

