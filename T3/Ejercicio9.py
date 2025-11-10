import json
import csv

ruta_fichero_usuarios = "T3/data/usuarios.json"
fichero_csv = "T3/data/usuarios_estadisticas.csv"

cabecera = ["Pais","N_usuarios","Total_Edad"]

pais = "España"
n_usuarios = 0
total_edad = 0

# 1. Leer el archivo JSON completo
with open(ruta_fichero_usuarios, "r", encoding="utf-8") as f:
    usuarios = json.load(f)
    
    for usuario in usuarios:
        if usuario["pais"] == pais:
            n_usuarios = n_usuarios + 1
            total_edad = total_edad + usuario["edad"]
       
contenido = [pais,n_usuarios,total_edad]

fichero_total = []
fichero_total.append(cabecera)
fichero_total.append(contenido)

with open(fichero_csv, "w", encoding="utf-8") as f:
    csv_writer = csv.writer(f,delimiter=",",lineterminator="\n")
    csv_writer.writerows(fichero_total)