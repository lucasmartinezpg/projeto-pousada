import sqlite3

conexao = sqlite3.connect("pousada.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_hospede TEXT NOT NULL,
    telefone TEXT NOT NULL,
    data_entrada TEXT NOT NULL,
    data_saida TEXT NOT NULL,
    pessoas INTEGER NOT NULL,
    pet TEXT NOT NULL,
    valor REAL NOT NULL
)
""")

conexao.commit()
conexao.close()

print("Tabela reservas criada com sucesso!")