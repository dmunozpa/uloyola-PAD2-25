import json

profesores = [
    ("Antonio Duran", "Ingeniero Informatico", "amduran@uloyola.es"),
    ("Manuel Ceballos", "Matematico", "mceballos@uloyola.es"),
    ("David Becerra", "Fisico", "dbecerra@uloyola.es")
]

fichero_path = "profesores.json"

with open(fichero_path, "w",encoding="utf-8") as f:
    json.dump(profesores, f)
