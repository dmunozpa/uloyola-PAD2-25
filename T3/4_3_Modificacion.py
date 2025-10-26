import json

fichero_path = "T3/data/fichero.json"

with open(fichero_path, "r",encoding='utf-8') as f:
    datos_alumna = json.load(f)
    
    # Modificación acceso de primer nivel
    datos_alumna["nombre"] = "Maria"
    datos_alumna["edad"] = "29"
    
    # Modificación acceso de listas
    lista = datos_alumna["habilidades"]
    lista.append("Java")
    datos_alumna["habilidades"] = lista
    
    # Modificación acceso de segundo nivel
    datos_alumna["configuracion"]["tema"] = "claro"
    
    # Valores Nuevos
    datos_alumna["modificado"] = True
    datos_alumna["original"] = fichero_path

fichero_path = "T3/data/fichero_modificado.json"

with open(fichero_path, "w",encoding='utf-8') as f:
    json.dump(datos_alumna,f,indent=4)



