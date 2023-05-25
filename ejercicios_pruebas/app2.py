#!/usr/bin/python3
from flask import Flask, jsonify, render_template

import models
from models.state2 import state

app = Flask(__name__)

@app.route("/")
def index():
    states = models.estorage.all(state)
    return render_template("index.html", states=states)

if __name__ == "__main__":
    app.run(debug=True)

""" hay una primera forma de hacerlo 
def index():
    states = models.estorage.all(state)
    states_data = []
    for s in states:
        state_data = {
            'id': s.id,
            'name': s.name,
            # Otros atributos del objeto state
        }
        states_data.append(state_data)
    return jsonify(states_data)
"""

"""
@app.route("/")
def index():
    states = models.estorage.all(state)
    states_data = []
    for s in states:
        state_data = {
            'id': s.id,
            'name': s.name,
            # Otros atributos del objeto state
        }
        states_data.append(state_data)
    return "{}".format(states_data)
"""

if __name__ == "__main__":
    app.run(debug=True)
