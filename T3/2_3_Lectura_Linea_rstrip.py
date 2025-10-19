ruta_relativa = "data/don_quijote_cap1.txt"
ruta_absoluta = "C:/Users/dmuno/Desktop/EXAMEN/data/don_quijote_cap1.txt"

with open(ruta_absoluta,"r",encoding="utf-8") as f:
    for linea in f:
        print(linea.rstrip())
