from lxml import html, etree
import requests
import json


def get_capture_rate(pokemon):
    page = requests.get(f"https://www.pokepedia.fr/{pokemon.lower()}")
    html_tree = html.fromstring(page.content)
    etree_object = html_tree.xpath("(//td[@colspan='3'])[14]/text()")
    capture_rate = str(etree_object[0])

    return capture_rate

