import package.pokeapi as pokeapi
import pytest


@pytest.mark.parametrize(
    "input_pokemon_name,expected_status_code",
    (
        ("Chenipan", 200),
        ("chenipan", 200),
        ("m. mime", 200),
        ("hello", 404),
    ),
)
def test_check_pokemon_name(input_pokemon_name: str, expected_status_code: int):
    assert pokeapi.check_pokemon_name(input_pokemon_name) == expected_status_code


@pytest.mark.parametrize(
    "input_pokemon_name,expected_capture_rate",
    (
        ("Chenipan", 255),
        ("chenipan", 255),
        ("m. mime", 45),
    ),
)
def test_capture_rate(input_pokemon_name: str, expected_capture_rate: int):
    assert pokeapi.get_capture_rate(input_pokemon_name) == expected_capture_rate


@pytest.mark.parametrize(
    "input_pokemon_name,expected_base_hp",
    (
        ("Chenipan", 45),
        ("chenipan", 45),
        ("m. mime", 40),
    ),
)
def test_base_hp(input_pokemon_name: str, expected_base_hp: int):
    assert pokeapi.get_base_hp(input_pokemon_name) == expected_base_hp