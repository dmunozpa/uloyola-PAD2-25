import csv

datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Ana', 25, 'Madrid'],
    ['Luis', 30, 'Barcelona'],
]

with open('ejemplo1.csv', mode='w', newline="\n") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    # Escribe cada fila de la lista de listas
    escritor_csv.writerows(datos)

