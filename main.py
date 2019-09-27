"""."""
import os
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

usuarios_emails = []
usuarios_senhas = []


@app.route("/")
def login():
    """Pagina de login."""
    return render_template('login.html')


@app.route("/index")
def index():
    """Pagina inicial."""
    return render_template('index_html.html')


@app.route("/cadastro")
def cadastro():
    """Pagina de cadastro."""
    return render_template("signup.html")


@app.route("/processar_cadastro", methods=['GET', 'POST'])
def processar_cadastro():
    """Adiciona usuario globalmente."""
    dados = request.form

    usuarios_emails.append(dados.get("email"))
    usuarios_senhas.append(dados.get("senha"))

    return login()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
