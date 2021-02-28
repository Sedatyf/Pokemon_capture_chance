from pokeapi import get_capture_rate
from calculate import calculate_a, calculate_capture_chance

pokemon = input("Which pokemon do you want to check your capture chance? ")

capture_rate = get_capture_rate(pokemon)
a = calculate_a(20.0, 20.0, capture_rate, 1.0, 1.0)

if a >= 255:
    print(f"You have a 100% chance to capture {pokemon}!")
else:
    p = calculate_capture_chance(a)
    print(f"You have a {p * 100}% chance to capture {pokemon} per ball.")