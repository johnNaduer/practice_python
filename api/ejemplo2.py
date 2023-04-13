import requests

# Definimos la URL de la API y la ciudad que deseamos obtener el clima
url = 'https://api.openweathermap.org/data/2.5/weather'
ciudad = 'New York'

# Definimos los parámetros que necesitamos para hacer la petición a la API
params = {
    'q': ciudad,
    'appid': 'TU_API_KEY_AQUI',
    'units': 'metric'
}

# Realizamos la petición GET a la API de OpenWeatherMap
response = requests.get(url, params=params)

# Verificamos si la petición fue exitosa
if response.status_code == 200:
    # Obtenemos la información del clima en formato JSON
    clima_info = response.json()

    # Imprimimos la temperatura actual y la descripción del clima
    temperatura_actual = clima_info['main']['temp']
    descripcion_clima = clima_info['weather'][0]['description']
    print(f"La temperatura actual en {ciudad} es de {temperatura_actual} grados Celsius, y el clima es {descripcion_clima}.")
else:
    print("No se pudo obtener la información del clima")

