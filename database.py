import sqlite3

conexao = sqlite3.connect("pousada.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS hospedes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    cpf TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()

print("Tabela de hóspedes criada!")