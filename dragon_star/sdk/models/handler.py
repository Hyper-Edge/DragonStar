import typing

from .base import _BaseModel
from .types import optional_field


class Handler(_BaseModel):
    Name: str
    RequestClass: typing.Type[_BaseModel]
    ResponseClass: typing.Type[_BaseModel]
    Code: str = optional_field('')

    def to_dict(self):
        return dict(
            Name=self.Name,
            RequestClassName=self.RequestClass.__name__,
            ResponseClassName=self.ResponseClass.__name__,
            Code=self.Code
        )
