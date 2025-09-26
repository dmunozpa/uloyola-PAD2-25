
class Persona:
    
    def __init__ (self, nombre: str, id:str, edad: int, codigo: str):
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.__codigoSecreto = codigo


objetoPersonaManuel = Persona("Manuel","12345678Z",22,"123")

# Recibimos un error, dado que el atributo no es accesible fuera de la clase.
valorCodigo = objetoPersonaManuel.__codigoSecreto

print(f"El codigo secreto es: {valorCodigo}")


