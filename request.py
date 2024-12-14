# pip install requests
# pip show requests

import requests

def data_get(url):
    try:
        # Realizar la petición GET
        respuesta = requests.get(url)

        # Verificar si la petición fue exitosa (código 200)
        if respuesta.status_code == 200:
            print("Respuesta recibida con éxito:")
            print(respuesta.json())  # Imprimir el contenido en formato JSON
        else:
            print(f"Error en la petición. Código de estado: {respuesta.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error: {e}")

# URL de ejemplo (API pública de prueba)
url = "https://secure.epayco.co/validation/v1/reference/b99af202985342207951976b"

# Llamar a la función
data_get(url)
