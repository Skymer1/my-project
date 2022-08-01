from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<body style="background-color:DarkGrey;"><h1 style="color:Orange;">BaGit with Shnitzel</h1></body>'

app.run(host='0.0.0.0', port=8081)
