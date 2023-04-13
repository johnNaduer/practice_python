import requests

origin = "Lima, Peru"
destination = "Cusco, Peru"
api_key = "AIzaSyCh-VeMjr5XU6ZkfdbAspKj8IiBmCFvQQA"

# Hacemos una petición GET a la API de Google Maps para obtener la ruta entre los puntos de origen y destino
response = requests.get(f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}')

# Comprobamos si la petición fue exitosa
if response.ok:
    # Obtenemos la información en formato JSON
    directions_info = response.json()

    # Comprobamos si se encontraron resultados para la ruta
    if directions_info['status'] == 'OK':
        # Obtenemos la distancia y duración de la ruta
        distance = directions_info['routes'][0]['legs'][0]['distance']['text']
        duration = directions_info['routes'][0]['legs'][0]['duration']['text']
        print(f"La distancia entre {origin} y {destination} es de {distance} y el tiempo de viaje es de {duration}.")
    else:
        print("No se encontraron resultados para la ruta")
else:
    print("No se pudo obtener la información de la ruta")

