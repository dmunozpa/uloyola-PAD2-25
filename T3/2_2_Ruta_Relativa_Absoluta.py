
ruta_relativa = "T3/data/don_quijote_cap1.txt"
ruta_absoluta = "C:/Users/dmuno/Desktop/uloyola/PAD2-25/uloyola-PAD2-25/T3/data/don_quijote_cap1.txt"

with open(ruta_relativa,"r",encoding="utf-8") as f:
    contenido = f.read()
print(contenido)
