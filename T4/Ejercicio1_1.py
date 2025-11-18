import json
import pandas as pd

ruta_archivo_json = 'T4/data/usuarios.json'

with open(ruta_archivo_json,'r',encoding="utf-8") as archivo_json:
    datos_json = json.load(archivo_json)

df = pd.DataFrame(datos_json)

# Opcion simple
df_filtrado = df[df["activo"] == True]
df_filtrado = df_filtrado[df_filtrado["edad"]>40]

print(df_filtrado)

# Opcion Multiple
df_filtrado2 = df[(df["activo"] == True) & (df["edad"] > 40)]

print(df_filtrado2)
