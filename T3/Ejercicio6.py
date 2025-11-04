import csv

ruta_fichero_empleado = "T3/data/datos_empleados.csv"

conteo = {'Consultor': 0, 'Analista': 0, 'Ingeniero de Datos': 0}

with open(ruta_fichero_empleado,"r",encoding="utf-8") as f:
    
    reader = csv.reader(f, delimiter=',')

    for empleado in reader:
        profesion = empleado[4]
        if profesion in conteo:
            conteo[profesion] = conteo[profesion] + 1
            
print(conteo)
        
    
