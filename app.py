from flask import Flask, render_template
app=Flask('projeto')

@app.route("/")
def hello_world():
    nome = "Gabriel Travaini"
    produtos = [
        {"nome":'PC',"preço":"R$15000,00"},
        {"nome":"Deck de magic","preço":"R$700,00"}]
    return render_template("alo.html",n=nome,aProdutos=produtos),200


@app.route("/teste")
def testeroute():
    return render_template ("testeroute.html"),200

app.run()