__author__ = 'mmoisen'
from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "haii"

def start():
    app.run(host='169.254.0.2', port=5001, debug=True)