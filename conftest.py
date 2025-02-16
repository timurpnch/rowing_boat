import pytest

from .src.boat import RowingBoat, BoatProperties
from .src.oar import Oar


@pytest.fixture
def boat():
    properties = BoatProperties(
        weight=200.0,
        max_load=500.0,
        max_oars=4
    )
    return RowingBoat(properties)


@pytest.fixture
def oar():
    return Oar(length=2.0, blade_area=0.1)
