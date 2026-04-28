from models.jogo import Jogo
from services.jogo_service import carregar_jogos, salvar_jogos

print("=== SISTEMA DE JOGOS ===")

while True:
    print("\n1 - Adicionar jogo")
    print("2 - Listar jogos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("\nCadastro de Livro")

        nome = input("\nNome: ")
        genero = input("\nGenêro: ")
        ano = input("\nAno: ")

        jogo = Jogo(nome, genero, ano)
        jogos.append(jogo)
        salvar_jogos(jogos)
        print("\nJogo cadastrado!!")

        pass

    elif opcao == "2":
        # TODO: listar jogos
        pass

    elif opcao == "3":
        break
