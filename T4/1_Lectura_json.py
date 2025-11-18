import pandas as pd

# Datos del ejemplo​
data = {
  "CiudadOrigen": [
    "Madrid",
    "Madrid",
    "Barcelona",
    "Sevilla",
    "Valencia",
    "Madrid"
  ],
  "CiudadDestino": [
    "Barcelona",
    "Valencia",
    "Madrid",
    "Madrid",
    "Barcelona",
    "Sevilla"
  ],
  "Fecha": [
    "2024-01-05",
    "2024-01-07",
    "2024-01-08",
    "2024-01-10",
    "2024-01-12",
    "2024-01-14"
  ],
  "Medio": [
    "Tren",
    "Bus",
    "Avión",
    "Avión",
    "Tren",
    "Tren"
  ],
  "Distancia_km": [
    620,
    360,
    620,
    530,
    350,
    530
  ],
  "Precio": [
    55,
    28,
    95,
    80,
    45,
    None
  ]
}

#Convertir a DataFrame​
df = pd.DataFrame(data)
df.info()

df["Nueva Columna"] = df["Precio"]/ df["Distancia_km"]

df["Medio"] = df["Medio"].replace("Bus", "Autobús")

df[df["Nueva Columna"] > 50]

df_viajes_madrid = df[df["CiudadOrigen"] == "Madrid"]
df_viajes_madrid.to_csv("viajes_madrid.csv", index=False)

df[df["CiudadOrigen"] == "Madrid"].to_csv("viajes_madrid.csv", index=False)

print(df.head())