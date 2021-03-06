__author__ = 'mmoisen'
from flask import Flask, jsonify

app = Flask(__name__)

from models import Heater

relay = Heater(23)

@app.route("/home")
def home():
    return "haii"

@app.route("/lamp/")
def lamp():
    try:

        print "is it on?", relay.is_on
        if relay.is_on:
            relay.turn_off()
        else:
            relay.turn_on()
    except Exception as ex:
        print "Exception: ", ex.message
        return jsonify({"success": False}), 200

    return jsonify({"success": True}), 200

def start():
    app.run(host='0.0.0.0', port=5000, debug=True)