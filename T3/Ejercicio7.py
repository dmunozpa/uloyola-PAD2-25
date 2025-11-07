import json

ruta_fichero_usuarios = "T3/data/usuarios.json"
ruta_fichero_usuarios_modificado = "T3/data/usuarios_modificado.json"

# 1. Leer el archivo JSON completo
with open(ruta_fichero_usuarios, "r", encoding="utf-8") as f:
    usuarios = json.load(f)

# 2. Modificar los datos
for usuario in usuarios:
    # Incrementar edad si está activo
    if usuario["activo"]:
        usuario["edad"] += 1
        
        # Añadir categoría según la edad
        edad = usuario["edad"]
        if edad < 30:
            usuario["categoria"] = "joven"
        elif edad < 60:
            usuario["categoria"] = "adulto"
        else:
            usuario["categoria"] = "senior"

# 3. Guardar los cambios en un nuevo archivo
with open(ruta_fichero_usuarios_modificado, "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4)

print(f"Archivo '{ruta_fichero_usuarios}' generado correctamente.")
        
    
