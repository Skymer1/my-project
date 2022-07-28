from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<body style="background-color:DarkViolet;"><h1 style="color:Fuchsia;">Ayra is definitely Gay</h1></body>'

app.run(host='0.0.0.0', port=8081)
