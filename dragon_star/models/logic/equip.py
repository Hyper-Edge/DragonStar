import typing

from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


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

