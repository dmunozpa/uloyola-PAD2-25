ruta_relativa = "data/don_quijote_cap1.txt"
ruta_absoluta = "C:/Users/dmuno/Desktop/EXAMEN/data/don_quijote_cap1.txt"

fichero_salida = "output.txt"

def extrae_lineas(n_lineas:int):
    
    with open(ruta_absoluta,"r",encoding='utf-8') as f:
        # Leemos el fichero linea a linea
        contenido = f.readlines()
    
    # Seleccionamos las primeras n lienas
    lista_contenido = contenido[:n_lineas]
    
    # Escribimos el fichero de salida.
    with open(fichero_salida,"w",encoding='utf-8') as w:
        w.writelines(lista_contenido)
           
n_lineas = int(input("¿Cuántas líneas extraigo del fichero? \n"))
extrae_lineas(n_lineas)