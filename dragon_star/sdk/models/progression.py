from .types import *
from .models import DataModel
from .data import BaseData
from .reward import Reward
from .cost import Cost
from dragon_star.sdk.utils import to_underscore


class GenericLadderLevel(BaseData):
    def __init__(self, **kwargs):
        lvl = kwargs.get('Level')
        id_ = to_underscore(type(self).__name__) + f'_{lvl}'
        super().__init__(id=id_, **kwargs)

    Level: int = optional_field(0)
    Exp: int = 0
    Reward: typing.Optional[Reward] = None
    Cost: typing.Optional[Cost] = None
    Conditions: typing.List[str] = optional_field(list())

    def to_dict(self):
        return dict(
            Exp=self.Exp,
            Reward=self.Reward.to_dict() if self.Reward else None,
            Cost=self.Cost.to_dict() if self.Cost else None,
            Conditions=self.Conditions,
            Data=self.Data.to_dict()
        )


class GenericLadder(BaseData):
    Name: str
    ProgressionId: typing.Optional[str]
    ProgressionName: str
    Levels: typing.List[GenericLadderLevel]
    FullLadderLevelData: typing.Type[GenericLadderLevel] = optional_field(None)

    def add_level(self, **kwargs):
        curr_lvl = len(self.Levels)
        ll = self.FullLadderLevelData(Level=curr_lvl, **kwargs)
        self.Levels.append(ll)

    def to_dict(self):
        return dict(
            Name=self.Name,
            ProgressionId=self.ProgressionId,
            ProgressionName=self.ProgressionName,
            Levels=[l.to_dict() for l in self.Levels]
        )


class ProgressionLadder(BaseData):
    def __init__(self, **kwargs):
        entity_name = inflection.camelize(kwargs.get('Entity').__name__)
        id_ = f"progression_{entity_name}_{kwargs.get('LevelField', 'Level')}"
        super().__init__(id=id_, **kwargs)

    Entity: typing.Type[DataModel]
    IsExperienceBased: bool
    LevelField: str = 'Level'
    ExperienceField: str = 'Exp'
    LadderLevelData: typing.Type[BaseData]

    FullLadderLevelData: typing.Type[GenericLadderLevel] = optional_field(None)
    LadderClass: typing.Type[GenericLadder] = optional_field(None)

    @property
    def EntityName(self):
        return inflection.camelize(self.Entity.__name__)

    @property
    def ladder_class(self) -> typing.Type:
        if self.LadderClass:
            return self.LadderClass
        cls_name = f'{self.EntityName}{self.LevelField}{self.ExperienceField}Ladder'
        dyn_cls_args = dict(__base__=GenericLadder)
        dyn_cls_args['Levels'] = (typing.List[self.ladder_level_data_class], ...)
        self.LadderClass = pydantic.create_model(cls_name, **dyn_cls_args)
        return self.LadderClass

    @property
    def ladder_level_data_class(self) -> typing.Type:
        if self.FullLadderLevelData:
            return self.FullLadderLevelData
        cls_name = f'{self.EntityName}{self.LevelField}{self.ExperienceField}LadderData'
        dyn_cls_args = dict(__base__=GenericLadderLevel)
        dyn_cls_args['Data'] = (self.LadderLevelData, ...)
        self.FullLadderLevelData = pydantic.create_model(cls_name, **dyn_cls_args)
        return self.FullLadderLevelData

    def new_ladder(self, name: str):
        return self.ladder_class.define(
            id=f'{self.id}_{inflection.underscore(name)}',
            Name=name,
            ProgressionName=f"Progression{self.EntityName}{self.LevelField}",
            FullLadderLevelData=self.ladder_level_data_class,
            Levels=list())

    def to_dict(self):
        return dict(
            EntityName=self.EntityName,
            IsExperienceBased=self.IsExperienceBased,
            LevelField=self.LevelField,
            ExperienceField=self.ExperienceField,
            LadderLevelData=self.LadderLevelData.to_dict()
        )
