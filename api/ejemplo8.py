import requests

lat = 37.4221
lng = -122.0844
api_key = "AIzaSyCh-VeMjr5XU6ZkfdbAspKj8IiBmCFvQQA"

# Hacemos una petición GET a la API de Google Maps para obtener la dirección correspondiente a las coordenadas
response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}')

# Comprobamos si la petición fue exitosa
if response.ok:
    # Obtenemos la información en formato JSON
    geocode_info = response.json()

    # Comprobamos si se encontraron resultados para las coordenadas
    if geocode_info['status'] == 'OK':
        # Obtenemos la dirección correspondiente a las coordenadas
        address = geocode_info['results'][0]['formatted_address']
        print(f"Las coordenadas ({lat},{lng}) corresponden a la dirección '{address}'.")
    else:
        print("No se encontraron resultados para las coordenadas")
else:
    print("No se pudo obtener la información de las coordenadas")

