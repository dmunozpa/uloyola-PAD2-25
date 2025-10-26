
ruta_relativa = "data/don_quijote_cap1.txt"
ruta_absoluta = "C:/Users/dmuno/Desktop/uloyola/PAD2-25/uloyola-PAD2-25/T3/data/don_quijote_cap1.txt"

def cuenta_palabras(contenido: str)->int:
    
    lista_palabras = contenido.split()
    total = len(lista_palabras)
    
    return total
    

with open(ruta_relativa,"r",encoding="utf-8") as f:
    contenido = f.read()
    total = cuenta_palabras(contenido)
    
    print(f"El fichero '{f.name}' tiene {total} palabras.")
    
    