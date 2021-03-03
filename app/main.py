import pokeapi
import calculate

pokemon = pokeapi.get_pokemon()
level = pokeapi.get_level()
percent_hp = pokeapi.get_current_hp()
ball = pokeapi.get_bonus_ball()
status = pokeapi.get_bonus_status()

capture_rate = pokeapi.get_capture_rate(pokemon)
base_hp = pokeapi.get_base_hp(pokemon)

max_hp = calculate.calculate_max_hp(base_hp, level)
current_hp = calculate.calculate_current_hp(percent_hp, max_hp)
a = calculate.calculate_a(current_hp, max_hp, capture_rate, ball, status)

if a >= 255:
    print(f"You have a 100% chance to capture {pokemon}!")
else:
    p = calculate.calculate_capture_chance(a)
    print(f"You have, approximately, a {p * 100}% chance to capture {pokemon} per ball with the chosen ball.")