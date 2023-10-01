import typing

from .base import _BaseModel
from .types import optional_field


class Job(_BaseModel):
    Name: str
    JobDataClass: typing.Type[_BaseModel]
    Code: str = optional_field('')

    def to_dict(self):
        return dict(
            Name=self.Name,
            JobDataClass=self.JobDataClass.__name__,
            Code=self.Code)
