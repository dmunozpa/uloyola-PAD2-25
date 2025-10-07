class Terminal:
    def __init__(self, numeroTelefono: str) -> None:
        """Constructor de la clase Terminal.
        Valida el número y establece el tiempo de llamada a 0 segundos.
        """
        permitidos = ["6", "7", "9"]
        if len(numeroTelefono) == 9 and numeroTelefono[0] in permitidos:
            self.numeroTelefono = numeroTelefono
            self.tiempoLlamada = 0 # Por defecto a cero.
        else:
            print("Error en el numero de teléfono")

    def realizarLlamada(self, destino: "Terminal", duracion: int) -> None:
        
        """Actualiza el tiempo de llamada entre dos terminales."""
        self.tiempoLlamada += duracion
        destino.tiempoLlamada += duracion

        print(f"El {self.numeroTelefono} llamó a {destino.numeroTelefono} durante {duracion} segundos.")

    def __str__(self) -> str:
        return f"Terminal: {self.numeroTelefono} - Tiempo hablado: {self.tiempoLlamada} "

# ------------------- Ejemplo de uso -------------------

miTerminal = Terminal("652875987")
tuTerminal = Terminal("745875444")
suTerminal = Terminal("954524187")

miTerminal.realizarLlamada(tuTerminal,60)
miTerminal.realizarLlamada(suTerminal,120)

print(miTerminal)
print(tuTerminal)
print(suTerminal)
