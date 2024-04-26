import typing

from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


class CloneDragonReq(_BaseModel):
    DragonId: Ulid


class CloneDragonResp(_BaseModel):
    Success: bool


CloneDragonHandler = Handler(
    Name='CloneDragon',
    RequestClass=CloneDragonReq,
    ResponseClass=CloneDragonResp)

