import csv

ruta_fichero_empleado = "T3/data/datos_empleados.csv"

conteo = {'Consultor': 0, 'Analista': 0, 'Ingeniero de Datos': 0}

with open(ruta_fichero_empleado,"r",encoding="utf-8") as f:
    
    #TODO: Apertura del fichero modo csv, con delimitador ','

    #TODO: Recorrer el fichero modo lista.
        #TODO: Optiene la profesion
        #TODO: Comprueba que la profesión esta en el diciionario conteos:
            #TODO:Incrementa el valor del diccionario.
            
print(conteo)
        
    
