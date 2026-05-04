from models.jogo import Jogo
from services.jogo_service import carregar_jogos, salvar_jogos

jogos = carregar_jogos()

print("==================================")
print("======== Sistema de Jogos ========")
print("==================================")

while True:
    print("\n1 - Adicionar jogo")
    print("2 - Listar jogos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("\nCadastro de Jogo")

        nome = input("\nNome: ")
        genero = input("\nGênero: ")
        ano = input("\nAno: ")

        jogo = Jogo(nome, genero, ano)
        jogos.append(jogo)
        salvar_jogos(jogos)
        print("\nJogo cadastrado!!")

    elif opcao == "2":
        print("\nLista de Jogos: ")
        if len(jogos) == 0:
            print("Nenhum jogo encontrado!")
        else:
            for i, jogo in enumerate(jogos):
                jogo.exibir()

    elif opcao == "3":
        break