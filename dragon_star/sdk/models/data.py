from pydantic import Field, ValidationError

from .types import *
from .base import _BaseModel


class BaseData(_BaseModel):
    _abstract = True

    _registry = {}
    _lists = {}

    id: str = Field(...)

    def __init__(self, **data):
        super().__init__(**data)

    @staticmethod
    def dataclasses():
        for cls in BaseData._registry:
            yield cls

    @classmethod
    def instances(cls, predicate=None):
        return list(cls.iter_instances(predicate=predicate))

    @classmethod
    def iter_instances(cls, predicate=None):
        for inst in BaseData._lists[cls]:
            if predicate and not predicate(inst):
                continue
            yield inst

    @classmethod
    def define(cls, **kwargs):
        for fname in cls.__fields__.keys():
            if fname not in kwargs:
                raise Exception(f"Can't create instance of '{cls.__name__}': field '{fname}' is undefined")
        inst = cls(**kwargs)
        if cls not in BaseData._registry:
            BaseData._registry[cls] = {}
            BaseData._lists[cls] = []
        if inst.id in BaseData._registry[cls]:
            raise Exception(f"Instance of '{cls.__name__}' with id='{inst.id}' is already defined")
        BaseData._registry[cls][inst.id] = inst
        BaseData._lists[cls].append(inst)
        return inst


ReferencedType = typing.TypeVar('ReferencedType')


class DataRef(typing.Generic[ReferencedType]):

    def __init__(self, data_type: ReferencedType, id_: str):
        self.data_type = data_type
        self.id = id_

    def get_id(self):
        return BaseData.get(self.data_type, self.id)

    def ref_str(self):
        return f"{self.data_type}/{self.id}"

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_ref

    @classmethod
    def validate_ref(cls, v):
        if not isinstance(v, str):
            raise ValidationError("Data reference should be string")
        try:
            kls, id_ = v.split('/')
        except:
            raise ValidationError(f"Invalid data reference: {v}")
        return DataRef(kls, id_)

    def __repr__(self):
        return f"'{self.data_type}/{self.id}'"
