import json
from models.jogo import Jogo

CAMINHO = "data/jogos.json"


def carregar():
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            # TODO: transformar em objetos
            pass

    except:
        return []


def salvar(lista):
    dados = []

    for jogo in lista_jogos
    pass