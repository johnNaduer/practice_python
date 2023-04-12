#!/usr/bin/python3
from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de prueba para verificar las credenciales
users = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return render_template('success.html', username=username)
        else:
            error = 'Nombre de usuario o contraseña incorrectos'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)

