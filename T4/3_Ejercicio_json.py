import pandas as pd

#Cargamos el archivo
df = pd.read_json("T4/data/productos.json")
print(df.head())

#Crea la nueva columna basada en el precio de compra
df["precio_venta"] = df["precio_compra"] + (df["precio_compra"]*0.2)

#Imprimes todo el dataframe
print(df)

#Guarda en un nuevo archivo json llamado “precio_venta.json” 
#Cuando guardemos archivos json, podemos integrar:
#orient="records" -> exporta las filas como una lista de objetos JSON
#indent=4 -> Para que agregue la sangría.
#orient e indent, ayudan a que sea más legible el archivo SJON creado.
df.to_json("T4\data\precio_venta.json", orient="records", indent=4, index=False)

#Muestro en pantalla solo aquellos productos que tengan una cantidad menor a 10.
#Paso 1: df.loc[ ] -> para seleccionar por etiqueta de las columnas.
#Paso 2: df["cantidad"] < 10 -> Realiza el filtro. ¡Hay que separar la condición con una , de la selección de columnas (paso 3)!
#Paso 3: ["id", "nombre", "cantidad"] -> indica cuales son las columnas que quiero que muestre.
print(df.loc[df["cantidad"] < 10, ["id", "nombre", "cantidad"]])

#Utilizo el mismo filtro de antes, pero para almacenar ese resultado en una nueva variable (objeto dataframe).
df_nuevo = df.loc[df["cantidad"] < 10, ["id", "nombre", "cantidad"]]

#La inspecciono
print(df_nuevo.info())

#Guardo este dataframe como un nuevo archivo json
df_nuevo.to_json("T4\data\pendiente_compra.json", orient="records", indent=4, index=False)



