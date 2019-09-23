from flask import Flask, render_template
from flask.views import Teste

t = Teste()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b>Voce e um FANFARRAO</b>"

@app.route('/teste')
def teste():
    return 'Teste'

@app.route('/temp')
def temp():
    return render_template('hello.html')

@app.route('/testar')
def testar():
    return t.testar()
