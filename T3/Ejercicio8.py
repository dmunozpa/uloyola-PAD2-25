import json


ruta_fichero_usuarios = "T3/data/usuarios.json"

nuevo_usuario = {
    "id": 0,
    "nombre": "Manuel",
    "edad": 22,
    "pais": "España",
    "activo": False
  }


# 1. Leer el archivo JSON completo
with open(ruta_fichero_usuarios, "r", encoding="utf-8") as f:
    usuarios = json.load(f)

# 2.1 Obtenemos el ultimo ID del ultimo usuario
ultimo = usuarios[-1]   

# 2.2 Incremetamos el valor.
nuevo_usuario["id"] = ultimo["id"] + 1

# 2.3 Añadimos a la lista
usuarios.append(nuevo_usuario)

# 3. Sobreescribimos el fichero.
with open(ruta_fichero_usuarios, "w", encoding="utf-8") as f:
    json.dump(usuarios,f,indent=4,ensure_ascii=False)