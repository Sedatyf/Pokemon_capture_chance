import package.calculate as calculate
import pytest


@pytest.mark.parametrize(
    "input_base_hp,input_level,expected_max_hp",
    (
        (45, 50, 120),
        (45, 100, 231),
    ),
)
def test_calculate_max_hp(input_base_hp: int, input_level: int, expected_max_hp: float):
    assert calculate.calculate_max_hp(input_base_hp, input_level) == expected_max_hp
    assert type(calculate.calculate_max_hp(input_base_hp, input_level)) == float


@pytest.mark.parametrize(
    "input_current_percent,input_max_hp,expected_current_hp",
    (
        (50, 50, 25),
        (33, 50, 16.5),
    ),
)
def test_calculate_current_hp(input_current_percent: int, input_max_hp: int, expected_current_hp: float):
    assert calculate.calculate_current_hp(input_current_percent, input_max_hp) == expected_current_hp
    assert type(calculate.calculate_current_hp(input_current_percent, input_max_hp)) == float

