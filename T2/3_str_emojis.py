
class Persona:
    
    def __init__ (self, nombre: str, id:str, edad: int, codigo: str):
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.__codigoSecreto = codigo
        
    def __str__(self)->str:
        return f"- Nombre: {self.nombre} \U0001F600 \n- Id: {self.id} \n- Edad:{self.edad} \N{kissing face}"
       

objetoPersonaManuel = Persona("Manuel","12345678Z",22,"123")
print(objetoPersonaManuel)

