import package.calculate as calculate
import pytest

@pytest.mark.parametrize(
    "input_base_hp,input_level,expected_max_hp",
    (
        (45, 50, 120),
        (45, 100, 231),
    ),
)
def test_calculate_max_hp(input_base_hp: int, input_level:int, expected_max_hp:int):
    assert calculate.calculate_max_hp(input_base_hp, input_level) == expected_max_hp