import pytest

from main import required_fuel, fuel_counter


@pytest.mark.parametrize(
    "mass, expecte_fuel", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_required_fuel(mass, expecte_fuel):
    assert required_fuel(mass) == expecte_fuel


def test_fuel_counter():
    assert fuel_counter([12, 14, 1969, 100756]) == 34241
