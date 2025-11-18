import pandas as pd

df = pd.read_csv(
    "T4/data/viajes_output.csv",
    sep=",",        # Separador ("," por defecto)
    encoding="utf-8",  # Codificación
    header=0,       # Fila que contiene los nombres de las columnas
)

print(df)
df["Nueva Columna"] = df["Precio"]/ df["Distancia_km"]

df_nuevo = df[df['Precio']>50]

print(df_nuevo)
