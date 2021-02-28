import math


def calculate_a(actual_hp, max_hp, rate, ball, status):
    a = (((3 * max_hp - 2 * actual_hp) * (int(rate) * ball)) / (3 * max_hp)) * status
    return a


def calculate_capture_chance(a):
    y = 1048560 / (math.sqrt(math.sqrt(16711680 / a)))
    p = round((y / 65536) ** 4, 4)
    return p

