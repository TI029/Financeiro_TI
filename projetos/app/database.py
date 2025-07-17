# database.py - cria e manipula o banco de dados SQLite
import sqlite3

def criar_tabela():
    conn = sqlite3.connect('financeiro_ti.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            nota TEXT,
            quantidade INTEGER,
            valor REAL,
            data_recebimento TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir_compra(nome, nota, quantidade, valor, data_recebimento):
    conn = sqlite3.connect('financeiro_ti.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO compras (nome, nota, quantidade, valor, data_recebimento)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, nota, quantidade, valor, data_recebimento))
    conn.commit()
    conn.close()

def listar_compras():
    conn = sqlite3.connect('financeiro_ti.db')
    c = conn.cursor()
    c.execute('SELECT nome, nota, quantidade, valor, data_recebimento FROM compras')
    dados = c.fetchall()
    conn.close()
    return dados