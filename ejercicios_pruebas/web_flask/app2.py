#!/usr/bin/python3
from flask import Flask, jsonify

import models
from models.state2 import state

app = Flask(__name__)

@app.route("/")
def index():
    states = models.estorage.all(state)
    state_list = []
    for state in states:
        state_list.append(state.to_dict())
    return jsonify(state_list)

if __name__ == "__main__":
    app.run(debug=True)
