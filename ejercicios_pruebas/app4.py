#!/usr/bin/python3
from flask import Flask, request, render_template
from models.state2 import state
import models

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search_data():
    if request.method == 'POST':
        # Obtener el ID ingresado en el formulario
        id = int(request.form['id'])

        # Buscar el dato en la base de datos por ID
        searched_state = models.estorage.get(state, id)

        if searched_state:
            return f'El estado con ID {id} es: {searched_state.name}'
        else:
            return f'No se encontró ningún estado con ID {id}'
    else:
        return render_template('search.html')

@app.route('/update', methods=['GET', 'POST'])
def update_data():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        id = int(request.form['id'])
        new_name = request.form['new_name']

        # Obtener el objeto state a actualizar
        state_to_update = models.estorage.get(state, id)

        if state_to_update is None:
            return 'El estado con el ID {} no existe'.format(id)

        # Actualizar el nombre del estado
        state_to_update.name = new_name
        models.estorage.save()

        return 'Datos actualizados correctamente'
    else:
        return render_template('form2.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete_data():
    if request.method == 'POST':
        # Obtener el ID del objeto a eliminar desde el formulario
        id = int(request.form['id'])

        # Buscar el objeto en la base de datos
        obj = models.estorage.all(state)
        for item in obj:
            if item.id == id:
                # Eliminar el objeto
                models.estorage.delete(item)
                models.estorage.save()
                return f'Objeto con ID {id} eliminado correctamente'
        return f'No se encontró un objeto con ID {id}'
    else:
        return render_template('delete.html')


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

@app.route("/")
def index():
    states = models.estorage.all(state)
    return render_template("index.html", states=states)

if __name__ == '__main__':
    app.run(debug=True)
