from flask import Flask, render_template, request, session, redirect, url_for


app=Flask('projeto')
app.secret_key = "senha"



@app.route("/")
def home():
    return render_template("login.html")

@app.route('/login_validar',methods=['POST'])
def login_validar():
    if request.form['usuario'] == "eu" and request.form['senha'] == 'senha':
        session['usuario'] = request.form['usuario']
        return redirect(url_for("acesso_efetuado"))
    else:
        return 'SOME DAQUI',200

@app.route("/restrito")
def acesso_efetuado():
    if session['usuario'] == 'eu':
        return "bem vindo a zona de usuários <br>USER: {}".format(session['usuario']),200
    else:
        return "para de me hackear, parça",200

@app.route("/hello")
def hello_world():
    nome = "Gabriel Travaini"
    produtos = [
        {"nome":'PC',"preço":"R$15000,00"},
        {"nome":"Deck de magic","preço":"R$700,00"}]
    return render_template("alo.html",n=nome,aProdutos=produtos),200


@app.route("/teste")
def testeroute():
    return render_template ("testeroute.html"),200

@app.route("/soma/<n1>/<n2>")
def soma(n1=0,n2=0):
    res = int(n1)+int(n2)
    return render_template ("soma.html",r=res),200

@app.route("/form")
def get_form():
    return render_template("form.html"),200

@app.route("/form_recebe",methods=["GET","POST"])
def form_recebe():
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome),200
    else:
        return "FEZ ERRADO, BURRO!",200


app.run()