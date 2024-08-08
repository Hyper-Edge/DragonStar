from hyperedge.sdk.models import *
from dragon_star.models.dragons import Dragon


Mobs = TurnBattleUnit(Name='Mob')
Dragons = ModelTurnBattleUnit(Name='Dragon', Model=Dragon)

TBS = TurnBattlerSystem("TurnBattler")
TBS.add_unit_type(Mobs)
TBS.add_unit_type(Dragons)
