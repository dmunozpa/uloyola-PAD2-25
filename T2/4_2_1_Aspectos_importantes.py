import random

class Persona:
    
    def __init__ (self, nombre: str, id:str, edad: int):
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.__codigoSecreto = random.randint(1,100) # Asignamos un valor aleatorio por defecto
        
    def cambiaCodigo(self,nuevoCodigo:str):
        self.__codigoSecreto = nuevoCodigo
        
    def muestraCodigo(self):
        print(f"Codigo: {self.__codigoSecreto}")


objetoPersonaManuel = Persona("Manuel","12345678Z",22)

variable = objetoPersonaManuel

variable.edad = 55

print(f"Edad de Objeto Manuel: {objetoPersonaManuel.edad}")

print(f"Edad de Objeto Variable: {variable.edad}")

