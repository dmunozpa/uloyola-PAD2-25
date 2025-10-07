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
        return f"Terminal: {self.numeroTelefono} - Tiempo hablado: {self.tiempoLlamada} seg"

# ------------------- Clase Movil -------------------

class Movil(Terminal):
    def __init__(self, numeroTelefono: str, tarifa: float) -> None:
        """Constructor de Movil: hereda de Terminal e incluye tarifa y coste total."""
        super().__init__(numeroTelefono)
        self.tarifa = tarifa  
        self.costeTotal = 0.0

    def realizarLlamada(self, destino: "Terminal", duracion: int) -> None:
        """Sobrescribe el método para incluir el cálculo del coste."""
        super().realizarLlamada(destino, duracion)

        # Convertimos segundos a minutos
        minutos = duracion / 60
        coste = minutos * self.tarifa
        
        self.costeTotal += coste
        
        print(f"Realiza la llamada: {self.numeroTelefono} tiene un coste de {coste:0.2f} €")

    def __str__(self) -> str:
        return f"{super().__str__()} | Tarifa: {self.tarifa} €/min | Coste total: {self.costeTotal:0.2f} €"

### EJEMPLO DE USO ############

miMovil = Movil("652875987",0.10)
tuMovil = Movil("745875444",0.20)
suMovil = Movil("954524187",0.50)

miMovil.realizarLlamada(tuMovil,60)
miMovil.realizarLlamada(suMovil,120)

print(miMovil)
print(tuMovil)
print(suMovil)
