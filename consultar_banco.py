import sqlite3

conexao = sqlite3.connect("pousada.db")

reservas = conexao.execute("SELECT * FROM reservas").fetchall()

for reserva in reservas:
    print(reserva)

conexao.close()