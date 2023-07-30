import typing

from dragon_star.dragon_star.sdk.models import BaseData, DataRef
from dragon_star.dragon_star.models.data.tier import *


class MetalData(BaseData):
    Name: str
    Description: str
    Tier: DataRef[TierData]
    HasMetallicDragon: typing.Optional[bool] = False


METAL_COPPER = MetalData.define(
    Name='Copper',
    Desciption='',
    Tier=TIER_C,
    HasMetallicDragon=True)

METAL_IRON = MetalData.define(
    Name='Iron',
    Desciption='',
    Tier=TIER_C,
    HasMetallicDragon=True)

METAL_SILVER = MetalData.define(
    Name='Silver',
    Desciption='',
    Tier=TIER_U,
    HasMetallicDragon=True)

METAL_GOLD = MetalData.define(
    Name='Gold',
    Desciption='',
    Tier=TIER_U,
    HasMetallicDragon=True)

METAL_TUNGSTEN = MetalData.define(
    Name='Tungsten',
    Desciption='',
    Tier=TIER_U,
    HasMetallicDragon=True)

METAL_IRIDIUM = MetalData.define(
    Name='Iridium',
    Desciption='',
    Tier=TIER_U,
    HasMetallicDragon=True)
