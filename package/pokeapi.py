from lxml import html, etree
import requests


def get_capture_rate(pokemon):
    page = requests.get(f"https://www.pokepedia.fr/{pokemon.lower()}")
    html_tree = html.fromstring(page.content)
    etree_object = html_tree.xpath("(//td[@colspan='3'])[14]/text()")
    capture_rate = int(etree_object[0])

    return capture_rate


def get_base_hp(pokemon):
    page = requests.get(f"https://www.pokepedia.fr/{pokemon.lower()}")
    html_tree = html.fromstring(page.content)
    etree_object = html_tree.xpath("(//td[contains(., 'PV')]/following-sibling::td)[1]/text()")
    base_hp = int(str(etree_object[0]).replace("\n", ""))

    return base_hp


def get_bonus_ball(ball):
    if ball == 1: # Poke Ball
        bonus_ball = 1
    elif ball == 2: # Super Ball
        bonus_ball = 1.5
    elif ball == 3: # Hyper Ball
        bonus_ball = 2

    return bonus_ball


def get_bonus_status(status):
    if status in [1, 2, 3]: # BRN, PAR, PSN
        bonus_status = 1.5
    elif status in [4, 5]: # FRZ, SLP
        bonus_status = 2
    elif status == 6: # None
        bonus_status = 1
    return bonus_status

