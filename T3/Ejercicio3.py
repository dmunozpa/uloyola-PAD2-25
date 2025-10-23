from datetime import datetime

class Usuario:
    def __init__(self, nombre:str):
        self.nombre = nombre


def abre_fichero(usuario):
    """
    Registra en 'log.txt' una línea con el formato:
    AAAA-MM-DD HH:MM:SS LOGIN nombre_usuario
    """
    # Obtener la fecha y hora actuales en el formato solicitado
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Construir la línea de log
    linea_log = f"{fecha_hora} LOGIN {usuario.nombre}\n"
    
    # Abrir el fichero en modo 'append' para no sobrescribir los registros anteriores
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(linea_log)
    
    print(f"Registro añadido al log: {linea_log.strip()}")


usuario1 = Usuario("usuario1")
usuario2 = Usuario("usuario2")

abre_fichero(usuario1)
abre_fichero(usuario2)
