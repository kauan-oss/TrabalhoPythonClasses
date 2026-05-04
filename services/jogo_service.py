import json
from models.jogo import Jogo

# CAMINHO = "data/jogos.json"

def carregar_jogos():
    jogos = []
    try:
        with open("jogos.json", "r", encoding="utf-8") as arquivos:
            dados = json.load(arquivos)
            jogo = Jogo(
                item["nome"],
                item["genero"],
                item["ano"],
            )
            jogos.append(jogo)

    except:
        pass
    return jogos


def salvar_jogos(lista_jogos):
    dados = []

    for jogo in lista_jogos:
        dados.append(jogo.para_dict())
    with open("jogos.json", "w") as arquivo:
        json.dump(dados, arquivo, indent = 4)
    pass