import csv

ruta_fichero_empleado = "T3/data/datos_empleados.csv"
anio_a_buscar= '1980'

with open(ruta_fichero_empleado,"r",encoding="utf-8") as f:
    
    reader = csv.reader(f, delimiter=',')

    for empleado in reader:
        if anio_a_buscar in empleado[3]:
            print(empleado[2],empleado[0],empleado[1])
        
    
