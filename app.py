from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def buscar_reservas():
    conexao = sqlite3.connect("pousada.db")
    reservas = conexao.execute(
        "SELECT id, nome_hospede, telefone, data_entrada, data_saida, pessoas, pet, valor FROM reservas"
    ).fetchall()
    conexao.close()
    return reservas


@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nome_hospede = request.form["nome_hospede"]
        telefone = request.form["telefone"]
        data_entrada = request.form["data_entrada"]
        data_saida = request.form["data_saida"]
        pessoas = request.form["pessoas"]
        pet = request.form["pet"]
        valor = request.form["valor"]

        # Converte o valor brasileiro para número
        valor = valor.replace(".", "").replace(",", ".")
        valor = float(valor)

        conexao = sqlite3.connect("pousada.db")

        conexao.execute(
            "INSERT INTO reservas (nome_hospede, telefone, data_entrada, data_saida, pessoas, pet, valor) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (nome_hospede, telefone, data_entrada, data_saida, pessoas, pet, valor)
        )

        conexao.commit()
        conexao.close()

        return redirect("/")

    reservas = buscar_reservas()

    return render_template("index.html", reservas=reservas)


app.run(debug=True)