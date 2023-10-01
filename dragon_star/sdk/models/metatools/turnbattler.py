import pydantic
import typing

from dragon_star.sdk.models.base import _BaseModel
from dragon_star.sdk.models.data import DataRef, BaseData
from dragon_star.sdk.models.models import DataModel
from dragon_star.sdk.models.types import optional_field


class ActorStat(object):
    def __init__(self, name: str):
        self._name = name

    def __eq__(self, other):
        return isinstance(other, ActorStat) and other._name == self._name

    def __hash__(self):
        return hash(self._name)

    def __repr__(self):
        return f'ActorStat({self._name})'


class ActorBase(DataModel):
    pass


class TurnBattlerSystem(object):
    def __init__(self, name: str):
        self._name = name
        self._all_stats = set()
        #
        self._EquipmentTypes = []
        self._EquipmentDataTypes = []
        #
        self._CombatEntityTypes = []
        self._CombatEntityDataTypes = []
        #
        self._FormationSlotDataTypes = []
        self._FormationTypes = []
        self._FormationDataTypes = []

    def new_stat(self):
        pass

    @property
    def name(self):
        return self._name

    def _extract_stats(self):
        pass

    def add_combat_entity_type(self, e: typing.Type[ActorBase]):
        pass

    def add_equipment_type(self, e: typing.Type[ActorBase]):
        pass

    def add_formation_type(self, e: typing.Type[ActorBase]):
        pass

    def to_dict(self):
        return dict(
            Name=self._name,
            EquipmentTypes=[],
            EquipmentSlotDataTypes=[],
            EquipmentDataTypes=[],
            #
            CombatEntityTypes=[],
            CombatEntityDataTypes=[],
            #
            FormationTypes=[],
            FormationSlotDataTypes=[],
            FormationDataTypes=[]
        )
