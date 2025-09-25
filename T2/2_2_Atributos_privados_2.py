
class Persona:
    
    def __init__ (self, nombre: str, id:str, edad: int, codigo: str):
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.__codigoSecreto = codigo
    
    def cambiaCodigo(self,nuevoCodigo:str):
        self.__codigoSecreto = nuevoCodigo
        
    def muestraCodigo(self):
        print(f"Codigo: {self.__codigoSecreto}")


objetoPersonaManuel = Persona("Manuel","12345678Z",22,"123")

#Mostramos el valor del atributo privado
objetoPersonaManuel.muestraCodigo()

#Cambiamos el valor de atributo privado
objetoPersonaManuel.cambiaCodigo("456")

#Mostramos el valor del atributo privado
objetoPersonaManuel.muestraCodigo()






