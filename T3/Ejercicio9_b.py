import json
import csv

ruta_fichero_usuarios = "T3/data/usuarios.json"
fichero_json = "T3/data/usuarios_estadisticas.json"

json_salida = {"Pais":"España","N_usuarios":0,"Total_edad":0}

# 1. Leer el archivo JSON completo
with open(ruta_fichero_usuarios, "r", encoding="utf-8") as f:
    usuarios = json.load(f)
    
    for usuario in usuarios:
        if usuario["pais"] == json_salida["Pais"]:
            json_salida["N_usuarios"] = json_salida["N_usuarios"] + 1
            json_salida["Total_edad"] = json_salida["Total_edad"] + usuario["edad"]
      
with open(fichero_json, "w", encoding="utf-8") as f:
    json.dump(json_salida,f,indent=4,ensure_ascii=False)