#!/usr/bin/python3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/', methods=["POST"])
def process_form():
    name = request.form["name"]
    return "hola, {}".format(name)
    
if __name__ == '__main__':
    app.run(port=5001)
