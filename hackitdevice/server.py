__author__ = 'mmoisen'
from flask import Flask

app = Flask(__name__)

from models import Heater

@app.route("/home")
def home():
    return "haii"

@app.route("/lamp/")
def lamp():
    relay = Heater(23)
    if relay.is_on:
        relay.turn_off()
    else:
        relay.turn_on()

def start():
    app.run(host='0.0.0.0', port=5000, debug=True)