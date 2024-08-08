import pydantic
import typing

from hyperedge.sdk.models import BaseData, DataRef, optional_field


class ElementData(BaseData):
    Name: str
    HasStone: typing.Optional[bool]


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
