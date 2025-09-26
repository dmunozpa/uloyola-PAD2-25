class Persona:
    
    def __init__(self,nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self)->str:
        return f"Hola me llamo :{self.nombre} y tengo {self.edad} años."

class Alumno(Persona):
    
    def __init__(self, nombre: str, edad: int, carrera:str):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def presentarse(self) -> str:
        return f"Soy el alumno :{self.nombre} y estudio :{self.carrera}"
    

class Profesor(Persona):

    def __init__(self, nombre: str, edad: int, materia:str):
        super().__init__(nombre, edad)
        self.materia = materia
        self.listaAlumnos = []
    
    def presentarse(self) -> str:
        return f"Soy el profesor :{self.nombre} e imparto :{self.materia}"
    
    def anadirAlumno(self,alumno: Alumno):
        self.listaAlumnos.append(alumno)
    
    def totalAlumnos(self) ->int:
        return len(self.listaAlumnos)

objetoProfDani = Profesor("Daniel",42,"PAD2")
objetoAlumnoPepe = Alumno("Pepe",24,"DAN")
objetoAlumnoMaria = Alumno("Maria",23,"DAN")

objetoProfDani.anadirAlumno(objetoAlumnoPepe)
objetoProfDani.anadirAlumno(objetoAlumnoMaria)


print(f"El profesor: {objetoProfDani.nombre} tiene : {objetoProfDani.totalAlumnos()} alumnos")