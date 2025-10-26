import csv

datos_dic = [
    {'Nombre': 'Carlos', 'Edad': 35, 'Ciudad': 'Valencia'},
    {'Nombre': 'Elena', 'Edad': 28, 'Ciudad': 'Bilbao'},
]

# Nombres de los campos que servirán como encabezados
encabezado = ['Nombre', 'Edad', 'Ciudad']

with open('ejemplo2.csv', mode='w', newline='\n') as archivo_csv:
    # Crea el objeto DictWriter con el nombre de los campos
    escritor_dict = csv.DictWriter(archivo_csv, fieldnames=encabezado)
    
    # Escribe el encabezado
    escritor_dict.writeheader()
    
    # Escribe cada fila de datos del diccionario
    escritor_dict.writerows(datos_dic)


