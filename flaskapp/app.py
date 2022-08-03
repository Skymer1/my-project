from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<body style="background-color:Gray;"><h1 style="color:DarkOrange;">BaGit with Schnitzel</h1></body>'

app.run(host='0.0.0.0', port=8081)
