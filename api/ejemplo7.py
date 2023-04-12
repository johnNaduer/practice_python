import requests

address = "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA"
api_key = "AIzaSyCh-VeMjr5XU6ZkfdbAspKj8IiBmCFvQQA"

# Reemplazar los espacios en blanco por el signo + para formatear la dirección como se espera
formatted_address = address.replace(" ", "+")

# Hacemos una petición GET a la API de Google Maps para obtener la latitud y longitud de la dirección
response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={formatted_address}&key={api_key}')

# Comprobamos si la petición fue exitosa
if response.ok:
    # Obtenemos la información en formato JSON
    geocode_info = response.json()

    # Comprobamos si se encontraron resultados para la dirección
    if geocode_info['status'] == 'OK':
        # Obtenemos la latitud y longitud de la dirección
        latitude = geocode_info['results'][0]['geometry']['location']['lat']
        longitude = geocode_info['results'][0]['geometry']['location']['lng']
        print(f"La dirección '{address}' se encuentra en la latitud {latitude} y longitud {longitude}.")
    else:
        print("No se encontraron resultados para la dirección")
else:
    print("No se pudo obtener la información de la dirección")

