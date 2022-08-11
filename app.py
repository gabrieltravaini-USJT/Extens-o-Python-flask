from flask import Flask

app=Flask('projeto')

@app.route("/")
def hello_world():
    return "Hello World, esse é o meu primeiro código FLASK!"

app.run()