from hyperedge.sdk.models import NetEntity

from dragon_star.models.dragons import Dragon

dragon_net_e = NetEntity.from_model(Dragon, ['Level'])
