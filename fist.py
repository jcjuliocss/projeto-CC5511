from flask import Flask

t = Teste()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<b>Voce e um FANFARRAO</b>"
