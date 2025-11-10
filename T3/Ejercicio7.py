import json

ruta_fichero_usuarios = "T3/data/usuarios.json"
ruta_fichero_usuarios_modificado = "T3/data/usuarios_modificado.json"

# 1. Leer el archivo JSON completo
with open(ruta_fichero_usuarios, "r", encoding="utf-8") as f:
    
    # 2. Leemos el contenido en la variable usuarios
    usuarios = json.load(f)
    
    # 3. Itreamos cada elemento del JSON en la variable Usuario
    for usuario in usuarios:

        # 4. Comprobamos si el usuario está activo.
        if usuario['activo'] is True:
                   
            # 5. Actualizamos la edad del usuario.
            usuario['edad'] = usuario['edad'] + 1
           
            # 6. Creamos la categoria con el valor correcto.
            if usuario['edad'] < 30:
                usuario['categoria'] = 'Joven'
            elif usuario['edad'] >= 60:
                usuario['catergoria'] = 'Senior'
            else:
                usuario['categoria'] = 'Adulto'
      
 
# 7. Escribir en un fichero JSON completo
with open(ruta_fichero_usuarios_modificado, "w", encoding="utf-8") as f:
    json.dump(usuarios,f,indent=4,ensure_ascii=False)
    print("Fichero creado con éxito ! ")