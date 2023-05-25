#!/usr/bin/python3
from flask import Flask, request, render_template
from models.state2 import state
import models

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        name = request.form['name']
        id = int(request.form['id'])
        
        # Crear una nueva instancia de la clase state con los datos recibidos
        new_state = state(id=id, name=name)
        
        # Agregar la nueva instancia a la base de datos
        models.estorage.new(new_state)
        models.estorage.save()
        
        return 'Datos agregados correctamente'
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(port=5001)
