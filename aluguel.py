import sqlite3
from precos import PRECOS

def registrar_aluguel():
    nome = input("Nome do cliente: ").strip()
    contato = input(f"Contato de {nome}: ").strip()
    endereco = input(f"Endereço de {nome}: ").strip()
    data_entrega = input("Data de entrega: ").strip()

    print("\nItens disponíveis:")
    for i, (item, preco) in enumerate(PRECOS.items(), start=1):
        print(f"{i}. {item} - R$ {preco:.2f}")

    itens_escolhidos = []
    total = 0

    while True:
        try:
            escolha = int(input("\nEscolha o número do item (0 para finalizar): "))
            if escolha == 0:
                break
            item_nome = list(PRECOS.keys())[escolha - 1]
            quantidade = int(input(f"Quantas unidades de {item_nome}? "))
            itens_escolhidos.append((item_nome, quantidade))
            total += PRECOS[item_nome] * quantidade
        except (ValueError, IndexError):
            print("Opção inválida.")

    if not itens_escolhidos:
        print("Nenhum item selecionado.")
        return

    itens_str = ", ".join([f"{item} (x{qtd})" for item, qtd in itens_escolhidos])

    conn = sqlite3.connect("alugueis.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alugueis (nome, contato, endereco, data_entrega, itens, total) VALUES (?, ?, ?, ?, ?, ?)",
                   (nome, contato, endereco, data_entrega, itens_str, total))
    conn.commit()
    conn.close()
    print(f"\nAluguel registrado com sucesso! Total: R$ {total:.2f}")

def visualizar_alugueis():
    conn = sqlite3.connect("alugueis.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alugueis")
    registros = cursor.fetchall()
    conn.close()

    if not registros:
        print("Nenhum aluguel registrado.")
        return

    for aluguel in registros:
        print("="*40)
        print(f"ID: {aluguel[0]} | Cliente: {aluguel[1]} | Total: R$ {aluguel[6]:.2f}")

def excluir_aluguel():
    try:
        id_aluguel = int(input("ID do aluguel para excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    conn = sqlite3.connect("alugueis.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM alugueis WHERE id=?", (id_aluguel,))
    aluguel = cursor.fetchone()

    if not aluguel:
        print("Aluguel não encontrado.")
        conn.close()
        return

    confirm = input(f"Excluir aluguel de {aluguel[0]}? (s/n): ").lower()
    if confirm == "s":
        cursor.execute("DELETE FROM alugueis WHERE id=?", (id_aluguel,))
        conn.commit()
        print("Aluguel excluído.")
    conn.close()
