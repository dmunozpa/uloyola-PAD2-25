
class Persona:
    
    def __init__ (self, nombre: str, id:str, edad: int):
        self.nombre = nombre
        self.id = id
        self.edad = edad

objetoPersonaManuel = Persona("Manuel","12345678Z",22)

objetoPersonaMyriam = Persona("Myriam","29942526E",35)

objetoPersonaMyriam.edad = 36

objetoPersonaMyriam.id = "28820574Z"




# Accediendo a los atributos en una lista
listObjetos = [objetoPersonaManuel, objetoPersonaMyriam]

for persona in listObjetos:
    print(f"Nombre: {persona.nombre}")
    print(f"Id: {persona.id}")
    print(f"Edad: {persona.edad}")

