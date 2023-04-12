from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tareas inicial
tasks = [
    {'id': 1, 'title': 'Comprar leche', 'description': 'Ir al supermercado y comprar leche', 'done': False},
    {'id': 2, 'title': 'Sacar al perro', 'description': 'Sacar al perro a pasear por la tarde', 'done': False},
    {'id': 3, 'title': 'Hacer la cama', 'description': 'Hacer la cama antes de salir de casa', 'done': True},
]

# Obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Obtener una tarea específica
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# Crear una nueva tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Actualizar una tarea existente
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# Eliminar una tarea existente
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = [task for task in tasks if task['id'] == id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

