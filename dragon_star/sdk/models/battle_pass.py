from .base import _BaseModel
from .progression import *
from .types import optional_field


class BattlePass(_BaseModel):
    Name: str
    ScoreFieldName: str = optional_field('Score')
    LevelData: typing.Type[BaseData] = optional_field(None)
    Model: typing.Type[DataModel] = optional_field(None)
    Data: typing.Type[BaseData] = optional_field(None)
    #
    FullModelClass: typing.Type[DataModel] = optional_field(None)
    FullDataClass: typing.Type[BaseData] = optional_field(None)
    FullLadderLevelDataClass: typing.Type[GenericLadderLevel] = optional_field(None)
    FullLadderClass: typing.Type[GenericExpLadder] = optional_field(None)

    @property
    def name(self):
        return inflection.camelize(self.Name)

    @property
    def ladder_class(self) -> typing.Type[GenericExpLadder]:
        if self.FullLadderClass:
            return self.FullLadderClass
        cls_name = f'{self.name}BattlePassLadder'
        dyn_cls_args = dict(__base__=GenericExpLadder)
        dyn_cls_args['Levels'] = (typing.List[self.ladder_level_data_class], ...)
        self.FullLadderClass = pydantic.create_model(cls_name, **dyn_cls_args)
        return self.FullLadderClass

    def define(self, name: str):
        return self.ladder_class.define(
            id=f'{inflection.underscore(self.name)}_battle_pass_ladder_{inflection.underscore(name)}',
            Name=name,
            LadderType='BattlePass',
            ProgressionName=self.Name,
            FullLadderLevelData=self.ladder_level_data_class,
            Levels=list())

    @property
    def model_class(self) -> typing.Type[DataModel]:
        if self.FullModelClass:
            return self.FullModelClass
        cls_name = f'{self.name}BattlePass'
        if self.Model:
            dyn_cls_args = dict(__base__=self.Model)
        else:
            dyn_cls_args = dict(__base__=DataModel)
        if self.ScoreFieldName not in dyn_cls_args:
            dyn_cls_args[self.ScoreFieldName] = (int, ...)
        self.FullModelClass = pydantic.create_model(cls_name, **dyn_cls_args)
        return self.FullModelClass

    @property
    def data_class(self) -> typing.Type[BaseData]:
        if self.FullDataClass:
            return self.FullDataClass
        cls_name = f'{self.name}BattlePassData'
        if self.Data:
            dyn_cls_args = dict(__base__=self.Data)
        else:
            dyn_cls_args = dict(__base__=BaseData)
        if 'Name' not in dyn_cls_args:
            dyn_cls_args['Name'] = (str, ...)
        #
        self.FullDataClass = pydantic.create_model(cls_name, **dyn_cls_args)
        return self.FullDataClass

    @property
    def ladder_level_data_class(self) -> typing.Type[BaseData]:
        if self.FullLadderLevelDataClass:
            return self.FullLadderLevelDataClass
        cls_name = f'{self.name}BattlePassLadderData'
        dyn_cls_args = dict(__base__=GenericExpLadderLevel)
        if self.Data:
            dyn_cls_args['Data'] = (self.LevelData, ...)
        self.FullLadderLevelDataClass = pydantic.create_model(cls_name, **dyn_cls_args)
        return self.FullLadderLevelDataClass

    def to_dict(self):
        return dict(
            Name=self.Name,
            LevelData=self.LevelData.to_dict() if self.LevelData else None,
            Model=self.model_class.to_dict(),
            Data=self.data_class.to_dict()
        )
