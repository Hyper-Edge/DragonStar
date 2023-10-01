import typing

from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.models import DataModel
from dragon_star.sdk.models.types import optional_field, get_cs_type
from dragon_star.sdk.utils import camelize_string


_ValueType = typing.TypeVar('_ValueType')


class SyncedField(typing.Generic[_ValueType]):
    pass


class NetEntity(_BaseModel):
    @classmethod
    def to_dict(cls):
        flds = []
        synced_flds = []
        for fname, fdef in cls.__fields__.items():
            if fname == 'id':
                continue
            t_origin = typing.get_origin(fdef)
            if t_origin is SyncedField:
                fld_type = typing.get_args(fdef.outer_type_)[0]
                synced_flds.append({'Name': fname, 'Typename': get_cs_type(fld_type)})
            else:
                flds.append({'Name': fname, 'Typename': get_cs_type(fdef.outer_type_)})
        return dict(
            Name=cls.__name__,
            Fields=flds,
            SyncedFields=synced_flds
        )


class MultiPlayerSystem(object):
    def __init__(self, name: str):
        self._name = name
        self._entities = []

    def add_entity(self, entity: NetEntity):
        self._entities.append(entity)

    @property
    def name(self):
        return self._name

    def to_dict(self):
        return dict(
            Name=self._name,
            NetEntities=[e.Name for e in self._entities]
        )
