
ruta_relativa = "data/don_quijote_cap1.txt"
ruta_absoluta = "C:/Users/dmuno/Desktop/EXAMEN/data/don_quijote_cap1.txt"

def cuenta_palabras(contenido: str)->int:
    
    lista_palabras = contenido.split()
    total = len(lista_palabras)
    
    return total
    

with open(ruta_absoluta,"r",encoding="utf-8") as f:
    contenido = f.read()
    total = cuenta_palabras(contenido)
    
    print(f"El fichero '{f.name}' tiene {total} palabras.")
    
    