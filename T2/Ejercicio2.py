import random

# Clase base Persona
class Persona:
    def __init__(self, nombre="", salario=0.0, edad=0):
        self.nombre = nombre
        self.identificador = random.randint(1000, 9999)
        self.salario = salario
        self.edad = edad

    def __str__(self):
        return f"ID: {self.identificador} | Nombre: {self.nombre} | Edad: {self.edad} | Salario: {self.salario}€"

# Subclase Directivo
class Directivo(Persona):
    def __init__(self, nombre="", salario=0.0, edad=0, cargo=""):
        super().__init__(nombre, salario, edad)
        self.cargo = cargo

    def __str__(self):
        return f"{super().__str__()} | Cargo: {self.cargo}"

# Subclase Entrenador
class Entrenador(Persona):
    def __init__(self, nombre="", salario=0.0, edad=0, experiencia=""):
        super().__init__(nombre, salario, edad)
        self.experiencia = experiencia

    def __str__(self):
        return f"{super().__str__()} | Experiencia: {self.experiencia}"

# Subclase Jugador
class Jugador(Persona):
    def __init__(self, nombre="", salario=0.0, edad=0, posicion=""):
        super().__init__(nombre, salario, edad)
        self.posicion = posicion

    def __str__(self):
        return f"{super().__str__()} | Posición: {self.posicion}"

# Clase Entidad Deportiva
class Entidad_Deportiva:
    def __init__(self, nombre="", presupuesto_disponible=0.0):
        self.nombre = nombre
        self.lista_empleados = []
        self.presupuesto_disponible = presupuesto_disponible

    def AñadirEmpleado(self, persona):
        if persona in self.lista_empleados:
            print(f"{persona.nombre} ya está en la entidad.")
        else:
            if self.presupuesto_disponible >= persona.salario:
                self.lista_empleados.append(persona)
                self.presupuesto_disponible -= persona.salario
                print(f"{persona.nombre} añadido correctamente. Presupuesto restante: {self.presupuesto_disponible}€")
            else:
                print(f"No hay presupuesto suficiente para añadir a {persona.nombre}.")

    def DespedirEmpleado(self, persona):
        if persona in self.lista_empleados:
            self.lista_empleados.remove(persona)
            self.presupuesto_disponible += persona.salario
            print(f"{persona.nombre} despedido correctamente. Presupuesto disponible: {self.presupuesto_disponible}€")
        else:
            print(f"{persona.nombre} no está en la entidad.")

    def MostrarPlantilla(self):
        print(f"\nPlantilla de {self.nombre}:")
        for empleado in self.lista_empleados:
            print(empleado)

# ------------------- Ejemplo de uso -------------------

# Crear empleados
d1 = Directivo("Ana", 5000, 45, "Presidente")
e1 = Entrenador("Luis", 3000, 50, "10 años en fútbol profesional")
j1 = Jugador("Carlos", 2000, 25, "Delantero")
j2 = Jugador("Miguel", 1800, 22, "Portero")

# Crear entidad deportiva
equipo = Entidad_Deportiva("Club Deportivo Python", 15000)

# Añadir empleados
equipo.AñadirEmpleado(d1)
equipo.AñadirEmpleado(e1)
equipo.AñadirEmpleado(j1)
equipo.AñadirEmpleado(j2)

# Mostrar plantilla
equipo.MostrarPlantilla()

# Despedir un empleado
equipo.DespedirEmpleado(j1)

# Mostrar plantilla después del despido
equipo.MostrarPlantilla()
