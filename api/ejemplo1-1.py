#!/usr/bin/python3

import requests
import sys

# Obtener el nombre de usuario del primer argumento de la línea de comandos
username = sys.argv[1]

# Hacemos una petición GET a la API de GitHub con el username del usuario
response = requests.get(f'https://api.github.com/users/{username}')

# Comprobamos si la petición fue exitosa
if response.status_code == 200:
    # Obtenemos la información del usuario en formato JSON
    user_info = response.json()

    # Imprimimos el nombre y la descripción del usuario si están disponibles
    if user_info['name'] is not None:
        print(f"Nombre: {user_info['name']}")
    elif user_info['bio'] is not None:
        print(f"Descripción: {user_info['bio']}")
    else:
        print("No se pudo obtener la información del usuario")
