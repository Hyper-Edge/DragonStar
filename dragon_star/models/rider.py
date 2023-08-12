from dragon_star.sdk.models import DataModel
from dragon_star.models.data.riders.rider import *


class Rider(DataModel):
    Data: DataRef[RiderData]
