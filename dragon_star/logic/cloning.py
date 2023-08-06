import typing

from dragon_star.dragon_star.sdk.models.types import Ulid
from dragon_star.dragon_star.sdk.models.base import _BaseModel
from dragon_star.dragon_star.sdk.models.handler import Handler


class CloneDragonReq(_BaseModel):
    DragonId: Ulid


class CloneDragonResp(_BaseModel):
    Success: bool


CloneDragonHandler = Handler(
    Name='CloneDragon',
    RequestClass=CloneDragonReq,
    ResponseClass=CloneDragonResp)

CloneDragonHandler.Code = """
"""