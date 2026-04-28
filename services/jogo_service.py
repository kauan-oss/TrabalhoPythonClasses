import json
from models.jogo import Jogo

CAMINHO = "data/jogos.json"

def carregar_jogos():
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            jogo = Jogo(
                item["nome"],
                item["genero"],
                item["ano"],
            )
            pass

    except:
        return []


def salvar_jogos(lista):
    dados = []

    for jogo in lista_jogos:
        dados.append(jogo.para_dict())
    with open("jogos.json", "w") as arquivo:
        json.dump(dados, arquivo, indent = 4)
    pass