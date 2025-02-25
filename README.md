# Aplicación para obtener y guardar información de un dispositivo

Esta aplicación se encarga de obtener información de un dispositivo y sus datos periódicamente desde una URL específica. La información se guarda en dos archivos de texto:

- `info_dispositivo.txt`: Guarda la información del dispositivo, que se obtiene solo una vez al iniciar el programa.
- `data.txt`: Guarda los datos enviados por el dispositivo cada 60 segundos.

## Requisitos

- Python 3.x
- Librería `requests` instalada. Si no la tienes, instálala ejecutando:

```bash
pip install requests
```

## Descripción del funcionamiento

1. **Obtención de información del dispositivo**: El programa realiza una solicitud `GET` a la URL `http://10.0.0.164:4011/api/device/THBR00000000e03d465f` para obtener la información básica del dispositivo. Si la solicitud es exitosa, los datos se guardan en el archivo `info_dispositivo.txt`.

2. **Obtención de datos periódicos**: Luego, el programa realiza una solicitud `GET` a la URL `http://10.0.0.164:4011/api/current/1138584423/THBR00000000e03d465f` para obtener los datos enviados por el dispositivo. Esta operación se repite cada 60 segundos, y los datos se guardan en el archivo `data.txt`.

3. **Manejo de errores**: Si alguna solicitud falla, el programa mostrará un mensaje de error y continuará ejecutándose.

## Cómo ejecutar

1. Clona o descarga el repositorio de la aplicación.
2. Instala las dependencias necesarias.
3. Ejecuta el script:

```bash
python nombre_del_script.py
```

## Archivos generados

- `info_dispositivo.txt`: Contiene la información del dispositivo obtenida en la primera solicitud.
- `data.txt`: Contiene los datos periódicos enviados por el dispositivo.

## Notas

- El script realiza una pausa de 60 segundos entre cada solicitud de datos, lo que se ajusta al tiempo de espera del dispositivo.
- El script continuará ejecutándose indefinidamente hasta que se interrumpa manualmente.
