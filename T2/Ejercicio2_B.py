import random

class Persona:
    
    def __init__(self,nombre:str,salario:float,edad:int):
        self.nombre = nombre
        self.id = random.randint(1,1000)
        self.salario = salario
        self.edad = edad
    
    def __str__(self) -> str:
        return f"ID: {self.id} - Nombre: {self.nombre} - Edad: {self.edad} - Salario: {self.salario}"

class Directivo(Persona):
    
    def __init__(self, nombre: str, salario: float, edad: int, cargo: str):
        super().__init__(nombre, salario, edad)
        self.cargo = cargo

    def __str__(self) -> str:
        return f"Directivo: {super().__str__()} - Cargo: {self.cargo}"

class Entrenador(Persona):
    
    def __init__(self, nombre: str, salario: float, edad: int, experiencia:int):
        super().__init__(nombre, salario, edad)
        self.experiencia = experiencia
    
    def __str__(self) -> str:
        return f"Entrenador: {super().__str__()} - Experiencia: {self.experiencia}"

class Jugador(Persona):
    
    def __init__(self, nombre: str, salario: float, edad: int, posicion:str):
        super().__init__(nombre, salario, edad)
        self.posicion = posicion
    
    def __str__(self) -> str:
        return f"Jugador: {super().__str__()} - Posicion: {self.posicion}"

######################
######################

class Entidad_deportiva:
    
    def __init__(self, nombre:str, presupuesto_disponible: float):
        self.nombre = nombre
        self.lista_empleados = []
        self.presupuesto_disponible = presupuesto_disponible
        
    def __str__(self) -> str:
        return f"Entidad: {self.nombre} - Presupuesto: {self.presupuesto_disponible} €"
    
    def anadirEmpleado(self,persona: Persona)-> None:

        if persona not in self.lista_empleados:
            if self.presupuesto_disponible >= persona.salario:
                
                self.lista_empleados.append(persona)
                self.presupuesto_disponible -= persona.salario
                
                print(f"Añadido el empleado: {persona.nombre}")
                print(f"Salario actuaizado a : {self.presupuesto_disponible}")
            else:
                print(f"No hay presupuesto para añadir a: {persona.nombre}")
        else:
            print(f" La persona : {persona.nombre} ya está incluida en la entidad")

    def mostrarPlantilla(self):
        if len(self.lista_empleados) > 0:
           
            print(f"--- Lista de Empleados de {self.nombre}--- ")
            for emp in self.lista_empleados:
                print(emp)
        else:
            print("No hay empleados en la Entidad")
            
    def DespedirEmpleado(self, persona:Persona):
        if persona in self.lista_empleados:
            self.lista_empleados.remove(persona)
            self.presupuesto_disponible += persona.salario
            print(f"{persona.nombre} despedido correctamente. Presupuesto disponible: {self.presupuesto_disponible}€")
        else:
            print(f"{persona.nombre} no está en la entidad.")
            
    def EmpleadoMayorEdad(self) -> Persona:
        
        resultado = self.lista_empleados[0]
        
        for persona in self.lista_empleados:
            
            if resultado.edad > persona.edad:
                resultado = persona
                
        return resultado

######################
######################
### EJEMPLO DE USO ###
######################
######################

uLoyolaFC = Entidad_deportiva("ULoyola",1000)

uLoyolaFC.mostrarPlantilla()

pepe_castro = Directivo("Pepe Castro",1000,45,"Presidente")
obj_almeyda = Entrenador("Almeyda",400,50,7)
obj_navas = Jugador("Jesus Navas",2000,46,"Lateral")

uLoyolaFC.anadirEmpleado(pepe_castro)
uLoyolaFC.anadirEmpleado(obj_almeyda)
uLoyolaFC.anadirEmpleado(obj_navas)

uLoyolaFC.mostrarPlantilla()

print(f"El empleado con mayor edad es: {uLoyolaFC.EmpleadoMayorEdad()}")