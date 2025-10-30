import json
import pandas as pd

ruta_archivo_json = 'T4/data/ejemplo.json'

with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)



datos = pd.DataFrame(datos_json)

print(datos)