from hyperedge.sdk.models import BaseData


class AffinityData(BaseData):
    Name: str
    Description: str


AFFINITY_ELEMENTS = AffinityData.define(
    Name='Elemental',
    Description='')

AFFINITY_BIO = AffinityData.define(
    Name='Bio',
    Description='')

AFFINITY_TECHNO = AffinityData.define(
    Name='Techno',
    Description='')

AFFINITY_PSYCHO = AffinityData.define(
    Name='Psycho',
    Description='')

AFFINITY_AETHER = AffinityData.define(
    Name='Aether',
    Description='')
