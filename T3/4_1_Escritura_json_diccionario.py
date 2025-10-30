import json

profesores = [
    ("Antonio Duran", "Ingeniero Informatico", "amduran@uloyola.es"),
    ("Manuel Ceballos", "Matematico", "mceballos@uloyola.es"),
    ("David Becerra", "Fisico", "dbecerra@uloyola.es")
    ]

datos = []
fichero_path = "T3/data/profesores1.json"

# Construimos el diccionario
for nombre, estudios, email in profesores:
    datos.append({"nombre": nombre, "estudios": estudios, "email": email})

with open(fichero_path, "w") as f:
    json.dump(datos,f,indent=4)
