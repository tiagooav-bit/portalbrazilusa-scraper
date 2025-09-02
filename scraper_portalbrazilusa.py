"""
Script público para extração de contatos do diretório Portal Brazil USA
Autor: comunidade (uso livre e aberto)
Licença: Domínio Público
"""

import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://portalbrazilusa.org"
CATEGORIES = [
    "advocacia",
    "artes-e-cultura",
    "automoveis",
    "comida",
    "educacao-e-esportes",
    "eventos",
    "imoveis",
    "lojas",
    "outros-servicos-gerais-profissionais",
    "religiao-e-fe",
    "saude-beleza-e-bem-estar",
    "servicos-publicos-e-governos",
    "servicos-residenciais",
    "turismo",
]

def scrape_category(category):
    url = f"{BASE_URL}/categoria/{category}/"
    contacts = []

    while url:
        print(f"Coletando: {url}")
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            print(f"Erro {resp.status_code} em {url}")
            break

        soup = BeautifulSoup(resp.text, "html.parser")

        # Cada card de contato
        entries = soup.select(".directorist-listing-single")
        for entry in entries:
            name = entry.select_one(_
