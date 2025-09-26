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

#Mostramos el valor del atributo privado
objetoPersonaManuel.muestraCodigo()

        