import csv

ruta_fichero_empleado = "T3/data/datos_empleados.csv"
ruta_fichero_empleado_filtrado = "T3/data/datos_empleados_filtrado.csv"


lista_profesiones = ['Especialista en IA', 'Ingeniero de Datos']
lista_perfiles = []

with open(ruta_fichero_empleado,"r",encoding="utf-8") as f:
    
    reader = csv.reader(f, delimiter=',')

    for empleado in reader:
        profesion = empleado[4]
        if profesion in lista_profesiones:
            lista_perfiles.append(empleado)
            
            
with open(ruta_fichero_empleado_filtrado,"w",encoding="utf-8",newline="\n") as f:
    
    escritor_csv = csv.writer(f)   
    escritor_csv.writerows(lista_perfiles)

    
