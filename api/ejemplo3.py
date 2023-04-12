import requests
import sys

# Obtenemos el primer argumento que se pasa al script
user_id = sys.argv[1]

# Hacemos una petición GET a la API de JSONPlaceholder con el ID del usuario
response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')

# Comprobamos si la petición fue exitosa
if response.status_code == 200:
    # Obtenemos la información del usuario en formato JSON
    user_info = response.json()

    # Imprimimos el nombre y la dirección del usuario
    print(f"Nombre: {user_info['name']}")
    print(f"Dirección: {user_info['address']['street']} {user_info['address']['suite']}, {user_info['address']['city']}")
else:
    print("No se pudo obtener la información del usuario")
