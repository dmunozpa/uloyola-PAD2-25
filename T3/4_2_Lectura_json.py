import json

fichero_path = "T3/data/fichero.json"

with open(fichero_path, "r",encoding='utf-8') as f:
    
    datos_alumna = json.load(f)
    
    # Acceso a elementos primer nivel
    print(datos_alumna["nombre"])
    print(datos_alumna["edad"])
    
    # Acceso a listas
    lista_habilidades = datos_alumna["habilidades"]
    for habilidad in lista_habilidades:
        print(habilidad)

    # Acceso a elementos segundo nivel
    configuracion_tema = datos_alumna["configuracion"]["tema"]
    print(configuracion_tema)
    
