import csv

ruta_relativa = 'T3/data/datos_empleados.csv'

with open(ruta_relativa,'r',encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

