from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de usuarios
users = [{'id': 1, 'name': 'Juan'}, {'id': 2, 'name': 'Pedro'}, {'id': 3, 'name': 'Ana'}]

# Endpoint para crear un nuevo usuario utilizando el método POST
@app.route('/users', methods=['POST'])
def create_user():
    # Obtener los datos del usuario desde el body del request
    data = request.get_json()
    # Crear el nuevo usuario con un id único
    new_user = {'id': len(users) + 1, 'name': data['name']}
    # Agregar el usuario a la lista de usuarios
    users.append(new_user)
    # Devolver la respuesta con el nuevo usuario creado y un código 201 (creado)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)

