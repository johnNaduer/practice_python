file_path = 'ejemplo.txt'
content = 'Este es un ejemplo de contenido para el archivo.'

def callback(err):
    if err:
        print(err)
        return
    print(f"El contenido se ha guardado correctamente en {file_path}.")

try:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    callback(None)
except Exception as e:
    callback(e)
