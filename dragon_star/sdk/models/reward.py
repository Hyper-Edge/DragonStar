import pydantic

from .types import *
from .models import DataModelTemplate
from .data import BaseData


class Reward(pydantic.BaseModel):
    assets: typing.List[typing.Tuple[DataModelTemplate, int]]
    items: typing.List[typing.Tuple[BaseData, int]]
    name: str

    def __init__(self, name: str = ''):
        super().__init__(name=name, assets=[], items=[])

    def add(self, item, amount: int = 1):
        if isinstance(item, BaseData):
            self.items.append((item, amount))
        elif isinstance(item, DataModelTemplate):
            self.assets.append((item, amount))
        else:
            assert False
        return self

    def to_dict(self):
        return dict(
            Erc721Rewards=[],
            Erc1155Rewards=[dict(
                ItemId=f'{type(item).__name__}/{item.id}',
                Amount=amount
            ) for item, amount in self.items]
        )
