
ruta_relativa = "data/don_quijote_cap1.txt"
ruta_absoluta = "C:/Users/dmuno/Desktop/EXAMEN/data/don_quijote_cap1.txt"

def busca_palabra(palabra:str, contenido: str)->int:
    
    lista_palabras = contenido.split()
    total = 0
    if palabra in lista_palabras:
        total = lista_palabras.count(palabra)
    
    return total
 

with open(ruta_absoluta,"r",encoding="utf-8") as f:
    contenido = f.read()
    
    palabra_a_buscar = str(input("¿Qué palabra busco? \n"))
    total = busca_palabra(palabra_a_buscar,contenido)
    
    print(f"En fichero '{f.name}' tiene {total} de {palabra_a_buscar}")
    