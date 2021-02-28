import math


def calculate_a(actual_hp, max_hp, rate, ball, status):
    a = (((3 * max_hp - 2 * actual_hp) * (int(rate) * ball)) / (3 * max_hp)) * status
    return a


def calculate_max_hp(base_hp, level):
    max_hp = (((2 * base_hp + 31 + (127 / 4)) * level) / 100) + level + 10
    return round(max_hp, 0)


def calculate_current_hp(current_percent, max_hp):
    current_hp = (current_percent / 100) * max_hp
    return current_hp


def calculate_capture_chance(a):
    y = 1048560 / (math.sqrt(math.sqrt(16711680 / a)))
    p = round((y / 65536) ** 4, 4)
    return p

