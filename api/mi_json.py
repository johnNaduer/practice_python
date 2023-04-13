import json

# Definimos el objeto JSON
personas = [{"nombre": "Juan", "edad": 30}, {"nombre": "María", "edad": 25}]
print(type(personas))

# Convertimos el objeto JSON a objeto Python
personas_json = json.dumps(personas)
personas_python = json.loads(personas_json)

# Imprimimos el objeto Python
print(personas_python)
print(type(personas_python))

# Convertimos el objeto Python a objeto JSON
json_personas = json.dumps(personas)

print(json_personas)
print(type(json_personas))

