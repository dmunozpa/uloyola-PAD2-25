import pandas as pd

#Cargo directamente los datos como un dataframe usando pandas:
df = pd.read_csv("T4/data/alumnos.csv")

#Inspecciono los datos del dataframe:
print(df.info())

#Creo una nueva columna
df["Promedio"] = (df["Matematicas"] + df["Lengua"] + df["Ciencias"])/3
print(df.loc[:,["alumno", "Promedio"]])

#Mostrar en pantalla aquellos estudiantes que no aprobaron: Promedio < 5
print(df[df["Promedio"]<5])

#Crea una nueva columna llamada “Aprobado” y asigna 1 si aprobaron, 0 si no. 
df["Aprobado"] = (df["Promedio"] > 5).astype(int)

print(df)

#Almacena en un nuevo fichero “alumnos_promedio.csv” el dataframe.
df.to_csv("T4/data/alumnos_promedio.csv", index=False)
print("El nuevo fichero 'alumnos_promedio', fue creado con éxito.")