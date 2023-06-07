#!/usr/bin/python3
from flask import Flask, render_template
from create_model import place3
from db_storage import estorage
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return 'hola este es mi sitio'

@app.route('/places', methods=['GET'])
def get_places():
    places = estorage.all(place3)
    return render_template('places.html', places=places)


@app.route('/update_disponibilidad', methods=['POST'])
def update_disponibilidad():
    lugar_id = request.form.get('id')
    disponibilidad = request.form.get('disponibilidad')

    # Obtener el objeto lugar de la base de datos según el lugar_id
    lugar = estorage.get(place3, lugar_id)
    if lugar:
        # Actualizar el valor de disponibilidad
        lugar.diponibilidad = disponibilidad
        estorage.save()

        # Obtener todos los lugares actualizados
        places = estorage.get_all()

        # Renderizar el template HTML con los lugares
        return render_template('places.html', places=places)
    else:
        return 'Lugar no encontrado'


"""
@app.route('/update_disponibilidad', methods=['POST'])
def update_disponibilidad():
    lugar_id = request.form.get('id')
    disponibilidad = request.form.get('disponibilidad')

    # Obtener el objeto lugar de la base de datos según el lugar_id
    lugar = estorage.get(place3, lugar_id)
    if lugar:
        # Actualizar el valor de disponibilidad
        lugar.diponibilidad = disponibilidad
        estorage.save()
        return 'Disponibilidad actualizada correctamente'
    else:
        return 'Lugar no encontrado'
"""

if __name__ == '__main__':
    app.run(port=5001)
