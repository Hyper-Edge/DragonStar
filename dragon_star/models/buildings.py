from dragon_star.dragon_star.sdk.models import DataModel


class BuildingBase(DataModel):
    Level: int = 0


class BuildingCastle(BuildingBase):
    pass


class BuildingMine(BuildingBase):
    pass


class BuildingIncubator(BuildingBase):
    pass


class BuildingAcademy(BuildingBase):
    pass


class BuildingForgery(BuildingBase):
    pass


class BuildingNest(BuildingBase):
    pass
