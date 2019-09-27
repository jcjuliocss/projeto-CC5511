import os
from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('index_html.html')

@app.route("/cadastro")
def cadastro():
	return render_template("signup.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
