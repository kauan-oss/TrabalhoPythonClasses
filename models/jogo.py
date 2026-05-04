class Jogo:
    def __init__(self, nome, genero, ano):
        self.__nome = nome
        self.__genero = genero
        self.__ano = ano

    @property
    def nome(self):
        return self.__nome

    @property
    def genero(self):
        return self.__genero

    @property
    def ano(self):
        return self.__ano

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 2:
            print("Titulo invalido")
        else:
            self.__nome = novo_nome

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    def exibir(self):
        print(f"{self.__nome} - {self.__genero} ({self.__ano})")

    def para_dict(self):
        return {
            "nome": self.__nome,
            "genero": self.__genero,
            "ano": self.__ano,
        }

    @staticmethod
    def de_dict(dados):
        return Jogo(
            dados["nome"],
            dados["genero"],
            dados["ano"],
        )
