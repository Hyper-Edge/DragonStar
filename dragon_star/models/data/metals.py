import typing

from hyperedge.sdk.models import BaseData, DataRef, optional_field
from dragon_star.models.data.tier import *


class MetalData(BaseData):
    Name: str
    Description: str = optional_field('')
    Tier: DataRef[TierData]
    HasMetallicDragon: bool = optional_field(False)


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
