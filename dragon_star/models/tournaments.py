from hyperedge.sdk.models.tournament import Tournament
from hyperedge.sdk.models.reward import Reward

from dragon_star.models.data.currency import *


EnergyUsageTournament = Tournament(Name='EnergyUsage')

ENERGY_USAGE_EVENT = EnergyUsageTournament.define(Name='EnergyUsageEvent')


