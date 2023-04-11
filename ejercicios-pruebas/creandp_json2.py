#!/usr/bin/python3
import json
import uuid
import os
from sys import argv

# Verificar si el archivo existe
if os.path.exists("persona2.json"):
    with open("persona2.json", "r") as f:
        save_dato = json.load(f)
else:
    save_dato = {}

# Agregar el nuevo dato al diccionario
persona = {"nombre": argv[1], "apellido": argv[2], "edad": argv[3]}
n_id = str(uuid.uuid4())
save_dato[n_id] = persona

# Escribir todo el diccionario en el archivo
with open("persona2.json", "w", encoding='utf-8') as f:
    json.dump(save_dato, f, ensure_ascii=False, indent=4)

# Imprimir el contenido del archivo
with open("persona2.json", "r") as f:
    dato_json = f.read()

print(dato_json)
