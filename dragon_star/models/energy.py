from dragon_star.sdk.models.energy_system import EnergySystem


LevelEnergy = EnergySystem(Name='LevelEnergy')

USER_LEVEL_ENERGY = LevelEnergy.define(
    Name='UserLevelEnergy',
    InitialValue=80,
    RegenValue=1,
    RegenRate=1,
    MaxCapacity=100)
