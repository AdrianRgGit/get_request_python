import requests
import time
from datetime import datetime

# URL de la información del dispositivo
url_device = "http://10.0.0.164:4011/api/device/THBR00000000e03d465f"
# URL de los datos enviados del dispositivo
url_data = "http://10.0.0.164:4011/api/current/1138584423/THBR00000000e03d465f"

# Función para obtener la fecha y hora actual
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# GET para obtener la información del dispositivo
response_device = requests.get(url_device)

# Info del dispositivo. Esta petición sólo la hacemos una vez.
if response_device.status_code == 200:
    # Guardamos los datos en un archivo TXT
    with open("info_dispositivo.txt", "a") as file:
        file.write(response_device.text + "\n")
    print(f"{get_current_time()} - Información del dispositivo guardada en 'info_dispositivo.txt'.")
else:
    print(f"{get_current_time()} - Error en la petición de info del dispositivo: {response_device.status_code}")

while True:
    try:
        # GET para obtener los datos del dispositivo
        response_data = requests.get(url_data)

        # Datos del dispositivo
        if response_data.status_code == 200:
            # Guardamos los datos en un archivo TXT
            with open("data.txt", "a") as file:
                file.write(response_data.text + "\n")
            print(f"{get_current_time()} - Datos guardados en 'data.txt'.")
        else:
            print(f"{get_current_time()} - Error en la petición de datos del dispositivo: {response_data.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"{get_current_time()} - Error en la petición: {e}")

    # Esperar 60 segundos antes de hacer la siguiente petición. El programa del sensor tarda lo mismo en enviar.
    time.sleep(60)
