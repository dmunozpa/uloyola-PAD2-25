class Terminal:
    def __init__(self, numeroTelefono: str) -> None:
        
        # Condiciones de lista Validos
        listaValidos = ["9","6","7"]
        
        # Condicion de 9 digits
        if len(numeroTelefono) == 9 and numeroTelefono[0] in listaValidos:
            self.numeroTelefono = numeroTelefono
        else:
            print("Telefono no valido")
        self.tiempoLlamadaTotal = 0
        
    def realizarLlamada(self, telefonoLlamado: "Terminal", duracion:int):
        
        self.tiempoLlamadaTotal += duracion
        telefonoLlamado.tiempoLlamadaTotal +=  duracion
        
        print(f"El {self.numeroTelefono} llamó a {telefonoLlamado.numeroTelefono} durante {duracion} segundos")

    def __str__(self) -> str:
        return f"Terminal: {self.numeroTelefono} - Tiempo hablado: {self.tiempoLlamadaTotal} seg "

class Movil(Terminal):
    
    def __init__(self, numeroTelefono: str, tarifa:float) -> None:
        super().__init__(numeroTelefono)
        self.tarifa = tarifa
        self.costeTotal = tarifa * self.tiempoLlamadaTotal
        
    
    def realizarLlamada(self, telefonoLlamado: Terminal, duracion: int):
        super().realizarLlamada(telefonoLlamado, duracion)
        
        tiempoMinutos = duracion / 60
        costeLlamada = tiempoMinutos * self.tarifa
        
        self.costeTotal += costeLlamada
    
    def __str__(self) -> str:
        return f"{super().__str__()} | Tarfia: {self.tarifa} €/min | Coste Total: {self.costeTotal}"

# ------------------- Ejemplo de uso -------------------

miTerminal = Terminal("652875987")
tuTerminal = Terminal("745875444")
suTerminal = Terminal("954524187")

miTerminal.realizarLlamada(tuTerminal,60)
miTerminal.realizarLlamada(suTerminal,120)

print(miTerminal)
print(tuTerminal)
print(suTerminal)

# ------- 


miMovil = Movil("652875987",0.10) 
tuMovil = Movil("745875444",0.20) 
suMovil = Movil("954524187",0.50) 

miMovil.realizarLlamada(tuMovil,60) 
miMovil.realizarLlamada(suMovil,120) 

print(miMovil) 
print(tuMovil) 
print(suMovil) 
