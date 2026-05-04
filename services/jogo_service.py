import json
from models.jogo import Jogo

CAMINHO = "data/jogos.json"


def carregar_jogos():
    jogos = []
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                jogo = Jogo.de_dict(item)
                jogos.append(jogo)
    except FileNotFoundError:
        pass

    return jogos


def salvar_jogos(lista_jogos):
    dados = []

    for jogo in lista_jogos:
        dados.append(jogo.para_dict())

    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
