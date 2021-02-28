from lxml import html, etree
import requests


def get_capture_rate(pokemon):
    page = requests.get(f"https://www.pokepedia.fr/{pokemon.lower()}")
    html_tree = html.fromstring(page.content)
    etree_object = html_tree.xpath("(//td[@colspan='3'])[14]/text()")
    capture_rate = int(str(etree_object[0]))

    return capture_rate


def get_base_hp(pokemon):
    page = requests.get(f"https://www.pokepedia.fr/{pokemon.lower()}")
    html_tree = html.fromstring(page.content)
    etree_object = html_tree.xpath("(//td[contains(., 'PV')]/following-sibling::td)[1]/text()")
    base_hp = int(str(etree_object[0]).replace("\n", ""))

    return base_hp


def get_bonus_ball():
    bonus_ball = 0
    is_found = False

    while not is_found:
        ball = input("Which ball will you use? ")
        if ball.lower() == "poke ball":
            bonus_ball = 1
            is_found = True
        elif ball.lower() == "super ball":
            bonus_ball = 1.5
            is_found = True
        elif ball.lower() == "hyper ball":
            bonus_ball = 2
            is_found = True
        else:
            print("Your ball's choice wasn't recognized. Please choose between Poke ball, Super ball or Hyper ball.")
    return bonus_ball


def get_bonus_status():
    bonus_status = 0
    is_found = False

    while not is_found:
        status = input("Has the Pokemon a status condition? (Paralized, Sleep, None...) \nPlease type short code status: ")
        if status.lower() in ["brn", "par", "psn"]:
            bonus_status = 1.5
            is_found = True
        elif status.lower() in ["frz", "slp"]:
            bonus_status = 2
            is_found = True
        elif status.lower() == "none":
            bonus_status = 1
            is_found = True
        else:
            print("Your status' choice wasnt't recognized. Please type status with its short name, like it appears on the Pokemon life.")
    return bonus_status

