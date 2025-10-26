
ruta_absoluta = "C:/Users/dmuno/Desktop/EXAMEN/data/don_quijote_cap1.txt"


ruta_relativa = "T3/data/don_quijote_cap1.txt"
texto = "The End."

with open(ruta_relativa,"a",encoding="utf-8") as f:
    f.write(texto)

