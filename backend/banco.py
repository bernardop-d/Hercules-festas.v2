import sqlite3

def criar_banco():
    conn = sqlite3.connect("alugueis.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alugueis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            contato TEXT,
            endereco TEXT,
            data_entrega TEXT,
            itens TEXT,
            total REAL
        )
    ''')
    conn.commit()
    conn.close()
