import json
import pandas as pd

ruta_archivo_json = 'T4/data/usuarios.json'

with open(ruta_archivo_json,encoding="utf-8") as archivo_json:
    datos_json = json.load(archivo_json)

df = pd.DataFrame(datos_json)

# Creamos la columna nueva - Categoria
df["categoria"] = None

# Aplicamos el filtro, y actualizamos a "Mayor"
df.loc[(df["activo"] == True) & (df["edad"] > 40), "categoria"] = "Mayor"

print(df)