from banco import criar_banco
from aluguel import registrar_aluguel, visualizar_alugueis, excluir_aluguel

def menu():
    criar_banco()
    while True:
        print("\n==== HÉRCULES FESTAS ====")
        print("1. Registrar aluguel")
        print("2. Visualizar aluguéis")
        print("3. Excluir aluguel")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_aluguel()
        elif opcao == "2":
            visualizar_alugueis()
        elif opcao == "3":
            excluir_aluguel()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
