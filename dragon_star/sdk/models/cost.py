from .types import *
from .models import DataModelTemplate
from .data import BaseData


class Cost(pydantic.BaseModel):
    assets: typing.List[typing.Tuple[DataModelTemplate, int]]
    items: typing.List[typing.Tuple[BaseData, int]]

    def __init__(self):
        super().__init__(assets=[], items=[])

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
            Erc721Costs=[],
            Erc1155Costs=[dict(
                ItemId=item.id,
                Amount=amount
            ) for item, amount in self.items]
        )
