from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


class RetireDragonReq(_BaseModel):
    DragonId: Ulid


class RetireDragonResp(_BaseModel):
    Success: bool


RetireDragonHandler = Handler(
    Name='RetireDragon',
    RequestClass=RetireDragonReq,
    ResponseClass=RetireDragonResp)


class RecycleDragonEquipmentReq(_BaseModel):
    DragonEquipmentId: Ulid


class RecycleDragonEquipmentResp(_BaseModel):
    Success: bool


RecycleDragonEquipmentHandler = Handler(
    Name='RecycleDragonEquipment',
    RequestClass=RecycleDragonEquipmentReq,
    ResponseClass=RecycleDragonEquipmentResp)

