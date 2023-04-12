import requests

city = "Lima"
api_key = "d341bf17cdd27ca507de51bea3b0617c"

# Hacemos una petición GET a la API de OpenWeatherMap con el nombre de la ciudad y la API key
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')

# Comprobamos si la petición fue exitosa
if response.status_code == 200:
    # Obtenemos la información del clima en formato JSON
    weather_info = response.json()

    # Imprimimos la temperatura actual en grados Celsius
    temp = round(weather_info['main']['temp'] - 273.15, 1)
    print(f"La temperatura actual en {city} es de {temp}°C.")
else:
    print("No se pudo obtener la información del clima")

