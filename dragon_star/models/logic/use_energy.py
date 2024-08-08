import typing

from hyperedge.sdk.models.types import *
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.handler import Handler


class UseEnergyReq(_BaseModel):
    Amount: int


class UseEnergyResp(_BaseModel):
    Success: bool


UpgradeDragonHandler = Handler(
    Name='UseEnergy',
    RequestClass=UseEnergyReq,
    ResponseClass=UseEnergyResp)