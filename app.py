from flask import Flask, render_template

app=Flask('projeto')

@app.route("/")
def hello_world():
    return render_template("alo.html"),200

app.run()