import random

class Persona:
    
    def __init__(self,nombre:str,salario:float,edad:int):
        #TODO: Realiza el constructor de la clase
    
    def __str__(self) -> str:
        #TODO: Realiza el método __str__(Self) de la clase
        pass

class Directivo(Persona):
    
    def __init__(self, nombre: str, salario: float, edad: int, cargo: str):
        #TODO: Realiza el constructor de la clase

    def __str__(self) -> str:
        #TODO: Realiza el método __str__(Self) de la clase

class Entrenador(Persona):
    
    def __init__(self, nombre: str, salario: float, edad: int, experiencia:int):
        #TODO: Realiza el constructor de la clase
    
    def __str__(self) -> str:
        #TODO: Realiza el método __str__(Self) de la clase

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
        # TODO: Realizar el constructor
        pass
        
    def __str__(self) -> str:
        return f"Entidad: {self.nombre} - Presupuesto: {self.presupuesto_disponible} €"
    
    def anadirEmpleado(self,persona: Persona)-> None:

        if persona not in self.lista_empleados:
            if self.presupuesto_disponible >= persona.salario:
                
                # TODO: Añade a la lista empleados a persona.
                # TODO: Actualiza el presupuesto disponible con el salario de la persona
                
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

######################
######################

uLoyolaFC = Entidad_deportiva("ULoyola",100)

uLoyolaFC.mostrarPlantilla()

pepe_castro = Directivo("Pepe Castro",1000,45,"Presidente")
obj_almeyda = Entrenador("Almeyda",400,50,7)
obj_navas = Jugador("Jesus Navas",2000,46,"Lateral")

uLoyolaFC.anadirEmpleado(pepe_castro)
uLoyolaFC.anadirEmpleado(obj_almeyda)
uLoyolaFC.anadirEmpleado(obj_navas)

uLoyolaFC.mostrarPlantilla()