import pydantic
import typing

from dragon_star.sdk.models import BaseData, DataRef, optional_field


class ElementData(BaseData):
    Name: str
    HasStone: bool = optional_field(False)


ELEMENT_FIRE = ElementData.define(
    Name='Fire',
    HasStone=True
)

ELEMENT_WIND = ElementData.define(
    Name='Wind'
)
ELEMENT_GEO = ElementData.define(
    Name='Geo',
    HasStone=True
)
ELEMENT_WATER = ElementData.define(
    Name='Water',
    HasStone=True
)
ELEMENT_ELECTRO = ElementData.define(
    Name='Electro'
)

ELEMENT_METAL = ElementData.define(
    Name='Metal'
)
