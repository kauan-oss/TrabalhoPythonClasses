class Jogo:
    def __init__(self, nome, genero, ano):
        self.__nome = nome
        self.__genero = genero
        self.__ano = ano

    @property
    def genero (self):
       return self.__genero

    @property
    def ano (self):
       return self.__ano

    @property
    def nome (self):
       return self.__nome

    @ano.setter
    def ano (self, novo_nome):
        if len(novo_nome) < 2:
            print("Título inválido")
        else:
            self.__nome = novo_nome

    def exibir(self):
        print(f"{self.__nome} - {self.__genero} ({self.__ano})")

    def para_dict(self):
        return {
            "Ano": self.__nome,
            "Genero": self.__genero,
            "Ano": self.__ano
        }
        pass

    @staticmethod
    def de_dict(dados):
       return "de_dict"
        #pass