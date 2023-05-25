#!/usr/bin/python3
from flask import Flask, jsonify

from models import estorage
from models import state

app = Flask(__name__)

@app.route("/")
def index():
    states = estorage.all(state)
    state_list = []
    for state in states:
        state_list.append(state.to_dict())
    return jsonify(state_list)

if __name__ == "__main__":
    app.run(debug=True)
