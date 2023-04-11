import json

# cargar el archivo JSON
with open('ejemplo.json') as f:
    data = json.load(f)

# acceder al valor del campo "email" del primer objeto en la lista
email = data[0]['email']

print(email)
