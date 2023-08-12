from pydantic import Field, ValidationError

from dragon_star.sdk.models.types import *
from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.utils import to_underscore


class BaseData(_BaseModel):
    _abstract = True

    _registry = {}
    _lists = {}

    id: str = Field(...)

    def __init__(self, **data):
        super().__init__(**data)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

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
        if 'id' not in kwargs and 'Name' in kwargs:
            kwargs['id'] = to_underscore(kwargs['Name'])
        #
        for fname, fdef in cls.__fields__.items():
            if fname not in kwargs:
                if not fdef.required:
                    continue
                raise Exception(f"Can't create instance of '{cls.__name__}': field '{fname}' is undefined")
            #
            t_origin = typing.get_origin(fdef.outer_type_)
            if t_origin is DataRef:
                t_args = typing.get_args(fdef.outer_type_)
                arg = kwargs[fname]
                if not isinstance(arg, t_args[0]):
                    raise Exception(f"Can't create instance of '{cls.__name__}': field '{fname}' should be of type {fdef.outer_type_}")
                kwargs[fname] = DataRef[t_args[0]](ref=arg.id, dt=t_args[0])
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

    def __init__(self, ref: str, dt: typing.Type):
        self._ref = ref
        self._dt = dt

    @property
    def ref_str(self):
        return f"{self._dt.__name__}/{self._ref}"

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_ref

    @classmethod
    def validate_ref(cls, v):
        if not isinstance(v, cls):
            raise ValidationError("Data reference should be DataRef")
        try:
            kls, id_ = v.ref_str.split('/')
        except:
            raise ValidationError(f"Invalid data reference: {v}")
        return v

    def __repr__(self):
        return self.ref_str
