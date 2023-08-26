from .base import _BaseModel


class BaseEvent(_BaseModel):
    _abstract = True

    @classmethod
    def to_dict(cls):
        d = super().to_dict()
        base = cls.base(BaseEvent)
        d['Base'] = base.__name__ if base else None
        return d
