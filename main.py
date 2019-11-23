# -*- coding: UTF-8 -*-
"""."""
import os

from flask import Flask, render_template, request
from Controller import Controller

app = Flask(__name__, static_url_path='/static')

usuarios_emails = []
usuarios_senhas = []


@app.route("/")
def login(msg=''):
    """Pagina de login."""
    return render_template('login.html', msg=msg)


@app.route("/index")
def index():
    """Pagina inicial."""
    return render_template('index_html.html')


@app.route("/cadastro")
def cadastro():
    """Pagina de cadastro."""
    return render_template("signup.html")


@app.route("/processar_cadastro", methods=['POST'])
def processar_cadastro():
    """Adiciona usuario globalmente."""
    dados = request.form

    controller = Controller()

    nome = dados.get("nome")
    email = dados.get("email")
    senha = str(dados.get("senha"))

    controller.add_user(nome=nome, email=email, senha=senha)

    return login()


@app.route("/inicio_exercicios")
def inicio_exercicios():
    """."""
    controller = Controller()

    perguntas = controller.get_perguntas()

    return render_template("exercicios.html",
                           pergunta=perguntas,
                           num=0,
                           acertos=0)


@app.route("/exercicios", methods=['POST'])
def exercicios():
    """."""
    dados = request.form
    num = int(dados["num"])
    resposta = dados['resposta']
    acertos = int(dados['acertos'])

    controller = Controller()
    perguntas = controller.get_perguntas()

    if int(resposta) == int(perguntas[num - 1]['resposta_correta']):
        acertos += 1

    if num == 9:
        msg = r'Parabéns! Você concluiu todos os exercícios! \
              \nTotal de acertos: ' + str(acertos)
        return render_template("index_html.html", msg=msg)

    return render_template("exercicios.html",
                           pergunta=perguntas,
                           num=num,
                           acertos=acertos)


@app.route("/processar_login", methods=['POST'])
def processar_login():
    """Processa dados de login e retorna para a index caso esteja tudo ok."""
    dados = request.form

    email = dados.get("email")
    senha = dados.get("senha")

    controller = Controller()

    usuario = controller.get_usuario(login=email, senha=senha)

    if usuario:
        return index()
    else:
        msg = 'Email ou senha invalidos'
        return login(msg=msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

app.run(host='0.0.0.0', port=port)
