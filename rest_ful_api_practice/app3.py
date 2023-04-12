#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenido a mi API REST'})

if __name__ == '__main__':
    app.run(debug=True)
