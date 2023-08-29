from dragon_star.sdk.models.battle_pass import BattlePass
from dragon_star.sdk.models.reward import Reward

from dragon_star.models.data.currency import *


RegularBattlePass = BattlePass(Name='Regular')

REGULAR_BP_STANDARD = RegularBattlePass.define('Standard')
REGULAR_BP_PREMIUM = RegularBattlePass.define('Premium')

for lvl in range(1, 10):
    regular_reward = Reward()
    regular_reward.add(CURR_DRAX, 100 * lvl)
    REGULAR_BP_STANDARD.add_level(Exp=100*lvl, Reward=regular_reward)

    premium_reward = Reward()
    premium_reward.add(CURR_GOLD, 100 * lvl)
    REGULAR_BP_PREMIUM.add_level(Exp=100*lvl, Reward=premium_reward)
