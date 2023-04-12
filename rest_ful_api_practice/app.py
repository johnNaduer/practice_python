#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Comprar leche", "descripcion": "Ir al supermercado y comprar leche"},
    {"id": 2, "titulo": "Hacer ejercicio", "descripcion": "Ir al gimnasio y hacer ejercicio durante una hora"},
    {"id": 3, "titulo": "Leer un libro", "descripcion": "Leer el libro 'El Quijote' durante una hora"}
]

@app.route('/tareas', methods=['GET', 'POST'])
def tareas_handler():
    if request.method == 'GET':
        return jsonify(tareas)
    elif request.method == 'POST':
        tarea_nueva = request.json
        tarea_nueva["id"] = len(tareas) + 1
        tareas.append(tarea_nueva)
        return jsonify(tarea_nueva), 201

@app.route('/tareas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tarea_handler(id):
    tarea = next((t for t in tareas if t["id"] == id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    elif request.method == 'GET':
        return jsonify(tarea)
    elif request.method == 'PUT':
        tarea_actualizada = request.json
        tarea["titulo"] = tarea_actualizada["titulo"]
        tarea["descripcion"] = tarea_actualizada["descripcion"]
        return jsonify(tarea)
    elif request.method == 'DELETE':
        tareas.remove(tarea)
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
