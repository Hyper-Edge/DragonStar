import typing
from .base import _BaseModel
from .types import optional_field


class BaseEvent(_BaseModel):
    _abstract = True

    @classmethod
    def to_dict(cls):
        d = super().to_dict()
        base = cls.base(BaseEvent)
        d['Base'] = base.__name__ if base else None
        return d


class OnRegisterEvent(BaseEvent):
    pass


class OnLoginEvent(BaseEvent):
    pass


class EventHandler(_BaseModel):
    Name: str = optional_field('')
    EventClass: typing.Type[BaseEvent]
    Code: str = optional_field('')

    def to_dict(self):
        return dict(
            Name=self.Name,
            EventClass=self.EventClass.__name__,
            Code=self.Code)
