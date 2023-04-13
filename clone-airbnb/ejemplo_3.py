# Definimos los argumentos como una lista
argumentos = ['basemodel', 'name="John Doe"']

# Iteramos sobre los elementos de la lista a partir del segundo elemento
for i in range(1, len(argumentos)):
    # Separamos el elemento en clave y valor
    diccionario = {}
    item = argumentos[i].split('=')
    key = item[0]
    val = item[1]
    
    # Limpiamos el valor: reemplazamos guiones bajos por espacios y eliminamos comillas dobles
    val = val.replace("_", " ")
    val = val.replace("\"", "")
    
    # Agregamos la clave y el valor al diccionario
    diccionario[key] = val

# Imprimimos el diccionario resultante
print(diccionario)
