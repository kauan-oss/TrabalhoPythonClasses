from models.jogo import Jogo
from services.jogo_service import carregar_jogos, salvar_jogos

print("=== SISTEMA DE JOGOS ===")

jogos = carregar_jogos()

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
        print("\nJogo cadastrado!")

    elif opcao == "2":
        if not jogos:
            print("\nNenhum jogo cadastrado.")
        else:
            print("\n=== LISTA DE JOGOS ===")
            for jogo in jogos:
                jogo.exibir()

    elif opcao == "3":
        break
