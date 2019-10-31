"""."""
import os

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

usuarios_emails = []
usuarios_senhas = []

perguntas = ["Ronaldo começou a trabalhar e agora recebe um Vale Refeição (VR)\
             que cobre R$200,00 em compras de alimentos. Ronaldo quer usar \
             metade desse dinheiro para comprar comidas congeladas. Além \
             disso, pretende gastar R$50,00 em bebidas. O preço da comida \
             congelada e da bebida do mercado que frequenta é de R$10,00 e \
             R$3,00, respectivamente. Quantas comidas congeladas e bebidas \
             Ronaldo conseguiu comprar? Quanto dinheiro do VR sobrou?",
             "Um fazendeiro precisa cercar um terreno retângular, de 150 \
             metros de comprimento e 70 metros de largura. Considerando que \
             cada metro da cerca que o fazendeiro deseja instalar custe \
             R$125,70, quanto ele deverá gastar de modo que fique sem falta \
             ou excesso de materiais?",
             "Um caminhão de entregas percorreu uma distância que corresponde \
             a 1300 milhas. Considerando que cada milha equivale a 1,609 \
             quilometros, calcule a distância que o veiculo percorreu em \
             quilometros.",
             "Em uma fábrica, 300 peças são fabricadas em 1 hora e meia. \
             Quantas peças são fabricadas em 1 dia?",
             "Todo mês Paula compra 60L (litros) em garrafas de água potável \
             para poder se hidratar ao longo desse período. No entanto, \
             certa vez um amigo seu lhe disse que poderia gastar menos do que \
             atualmente gasta comprando galões de água ao invés de \
             garrafas. Para verificar a veracidade dessa informação, Paula \
             decidiu analisar os preços e tamanhos de cada recipiente dos \
             produtos oferecidos no centro de reabastecimento: a garrafa \
             que costuma comprar, custa R$3,50 e tem 500ml (mililitros) de \
             água. Já o galão custa R$6,00 e tem 1L. Dada essas \
             informações, pergunta-se: Quanto custa o litro de água em \
             garrafas? O amigo de Paula estava certo ao afirmar que \
             gastaria menos comprando galões de água ao invés de garrafas?",
             "Leonardo decidiu parcelar um guarda-roupas de R$480,00 em 6 \
             vezes com juros simples. Considerando que a taxa é de 4%, \
             quanto ele deverá pagar pelo imóvel no total?",
             "Um empresário investiu R$1.500,00 em um fundo de investimento \
             que opera no regime de juros simples. Após 10 mêses, verificou \
             que havia R$2.000,00 em seu montante. Qual é a porcentagem da \
             taxa de juros desse fundo de investimento?",
             "Júlia investiu uma quantidade de R$5.000,00 em um fundo de \
             investimento que opera no regime de juros composto. Considerado \
             que a porcentagem desse juros seja de 1% ao mês, quanto \
             dinheiro irá ganhar após 6 mêses?",
             "Um capital de R$5.000,00 foi aplicado durante 8 meses no \
             sistema de juros compostos sob uma taxa mensal fixa e rendeu \
             um montante de R$10.000,00. Qual é o valor dessa taxa de juros?"]

respostas = [{"1": "17 comidas, 12 bebidas e R$50,00",
              "2": "10 comidas, 16 bebidas e R$52,00",
              "3": "20 comidas, 17 bebidas e R$48,00",
              "4": "15 comidas, 12 bebidas e R$75,00"},
             {"1": "R$65.400,00",
              "2": "R$59.900,00",
              "3": "R$15.900,00",
              "4": "R$55.308,00"},
             {"1": "2091.7Km",
              "2": "3020.2Km",
              "3": "4075.5Km",
              "4": "1100.1Km"},
             {"1": "5.100 peças",
              "2": "9.900 peças",
              "3": "1.200 peças",
              "4": "4.800 peças"},
             {"1": "R$9,00; Não",
              "2": "R$7,00; Sim",
              "3": "R$3,50; Sim",
              "4": "R$5,00; Não"},
             {"1": "R$499,20",
              "2": "R$480,00",
              "3": "R$550,00",
              "4": "R$600,50"},
             {"1": "7%",
              "2": "5%",
              "3": "3%",
              "4": "9%"},
             {"1": "R$7.377,80",
              "2": "R$9.444,20",
              "3": "R$6.500,00",
              "4": "R$8.857,80"},
             {"1": "7%",
              "2": "9%",
              "3": "5%",
              "4": "8%"}]


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

    usuarios_emails.append(dados.get("email"))
    usuarios_senhas.append(str(dados.get("senha")))

    return login()


@app.route("/inicio_exercicios")
def inicio_exercicios():
    """."""
    return render_template("exercicios.html",
                           pergunta=perguntas[0],
                           respostas=respostas[0],
                           num=0)


@app.route("/exercicios", methods=['POST'])
def exercicios():
    """."""
    dados = request.form
    num = int(dados["num"])
    return render_template("exercicios.html",
                           pergunta=perguntas[num],
                           respostas=respostas[num],
                           num=num)


@app.route("/processar_login", methods=['POST'])
def processar_login():
    """Processa dados de login e retorna para a index caso esteja tudo ok."""
    dados = request.form

    email = dados.get("email")
    senha = dados.get("senha")

    if email in usuarios_emails and str(senha) in usuarios_senhas:
        return index()
    else:
        msg = 'Email ou senha invalidos'
        return login(msg=msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

app.run(host='0.0.0.0', port=port)
