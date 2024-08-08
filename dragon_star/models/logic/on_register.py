import typing

from hyperedge.sdk.models.types import Ulid
from hyperedge.sdk.models.base import _BaseModel
from hyperedge.sdk.models.event import EventHandler, OnRegisterEvent


OnRegisterHandler = EventHandler(
    Name='OnRegister',
    EventClass=OnRegisterEvent)

