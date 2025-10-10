
#Variables 
"""
No cuenta con un comando para declarar variables.
Normalmente el valor se le asigna.
"""
x = 5
y = "Hola"
print(x, y)


#La variable toma el último valor asignado.
x = "Cambio de valor"
print(x)


#Si queremos podemos especificar el tipo de valor usando str(), int(), float(), etc.
x = int(6.4) #Solo se almacena la parte entera
print(x)


#Podemos comentar nuestro código utilizando # al inicio de cada línea. 
#Alternativamente, podemos utilizar “ ” ” o ‘ ’ ’ para comentar un bloque de varias líneas de código.
"""
Así podemos comentar
"""

"""También podemos usar comillas simples triples
para comentar varias líneas"""


#Si queremos conocer el tipo de una variable, podemos usar el comando: print(type(variable)).
print(type(x), type(y))


#Python usa la sangría para indicar bloques de código.
#Puede usarse un  espacio o cuatro.

if 5 > 2:
    print("5 es mayor que 2") #Sangría de 4 espacios


if 3 < 5:
 print("3 es menor que 5") #sangría de 1 espacio


#Las cadenas de texto pueden asignarse con comillas simples o dobles.
#Simples: 
x = 'Hola'
print(x)

#Dobles: 
x = "Hola con comillas dobles"
print(x)

#Python es distingue entre mayúsculas y minúsculas.
X = "esto es diferente a x "
x = "es otra variable para python"

print(X + x)
 
"""
Nombres de las variables:
Pueden empezar solo con valores alfanuméricos y guion bajo (A-Z,  0-9, _ ).
"""

#No puede ser una palabra “clave” de Python, por ejemplo: print.
#Pueden ser largos o cortos.

"""
Estándares en nombre de variable con varias palabras:
Camel: primera letra en minúscula y las otras en mayúscula (myVariableName).
Pascal: cada palabra inicia en mayúscula (MyVariableName).
Snake: cada palabra separada por guion bajo (my_variable_name).

"""

# Se pueden asignar múltiples valores usando una línea de código:
x, y, z = "hola", "como", "estas"
print(x, y, z)

x = y = z = "hola"
print(x, y, z)

#Variables globales y locales:
#Global: se ubican en el código general y su valor puede ser usando dentro de una función.
#Local: su valor es utilizado solo dentro del bloque de código al que corresponde. Por ejemplo, dentro de una función. 


x = "increible" #variable global

def mi_primera_funcion():
    x = "fantástico" #variable local
    print("Python es " + x)

mi_primera_funcion()

print("Python es " + x)   

#Se puede transformar su valor en global si se utiliza el comando “global”
print('Se puede transformar su valor en global si se utiliza el comando “global”') 
x = "increible" #variable global

def mifuncion():
  global x  #variable local que la convertimos en global
  x = "fantástico"
  print("Python es " + x)

mifuncion()

print("Python es " + x)   


#Listas: Los elementos de la lista están ordenados, se pueden modificar y permiten valores duplicados.
#Ejemplo: 
thislist = ["manzana", "platano", "cereza"]
print(thislist)

#Modificar lista: 
thislist.insert(2,"naranja") #inserta en la posición 2. Recordemos que empieza la posición en 0
print(thislist)

thislist.append("fresas") #agrega al final de la lista
print(thislist)

thislist.remove("fresas") #elimina el elemento indicado
print(thislist)

thislist.clear() #elimina todo el contenido de la lista
print(thislist)

#Tuple: Es una colección ordenada (el orden no cambiará) e inmutable. Permite miembros duplicados.
#Ejemplo: 
mytuple = ("manzana", "platano", "cereza")
print(mytuple)

#Condicionales y bucles
#If: evalúa si una condición se cumple (==, !=, <, <=, >, >=)
#Ejemplo: 
if 3 == 3:
 print("hola") #Noten que debe haber sangría y se cumple la condición

#Elif: Si las condiciones anteriores no se cumplían, prueba esta condición.
if 3 == 4:
  print("hola")
elif 5 > 2:
  print("5 es mayor que 2")


#Else: Hacer una acción si no se cumplen las condiciones anteriores.
if 3==5:
  print("hola")
else:
    print("3 no es igual a 5")


#While: En un bucle podemos ejecutar un conjunto de instrucciones mientras una condición sea verdadera.
i = 0 #Necesitamos inicializar la variable
while i < 5:
    print(i)
    i += 1

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break #Break: puede detener el bucle aunque la condición no se cumpla.

#For: El bucle se utiliza para iterar sobre una secuencia. 

for x in "banana": #Se inicia la variable x y toma cada valor de la cadena
  print(x)

for x in range(6): #range normalmente inicia en 0 y va hasta el número indicado -1. 
  print(x)

for x in range(1, 6): #range normalmente inicia en 0 y va hasta el número indicado -1. Si queremos que inicie en otro número, se indica entre paréntesis.
  if x == 1:
   print(f"Este for inicia en {x}")
  else:
   print(x)

for x in range(1, 6, 2): #Si queremos que incremente de a 2 en 2, se indica el tercer valor.
  if x == 1:
   print(f"Este for inicia en {x} y aumenta de a 2 en 2")
  else:
   print(x)


#Podemos usar for para recorrer listas
thislist = ["manzana", "platano", "cereza"]
for x in thislist:
  print(x)

#Funcniones
#Una función es un bloque de código que solo se ejecuta cuando se invoca.

#Ejemplo:
def prueba():
  print("Hello desde una funcion")

prueba() #Llamamos a la función para que se ejecute


#Se pueden pasar datos, conocidos como parámetros, a una función.
def suma_basica(a, b)->int:
    resultado = a + b
    return resultado #Una función puede devolver datos como resultado.

print(suma_basica(8,9)) 


#Dentro de una función:
#Try: intentar ejecutar código que podría dar error.
#Except: captura el error si ocurre dentro del try
#Return: en una función sirve para devolver un valor al lugar donde se llamó la función.

def suma_con_excepcion(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: ambos argumentos deben ser números."

print(suma_con_excepcion(8, 9))  # Resultado correcto
print(suma_con_excepcion(8, "a"))  # Error: ambos argumentos deben ser números.

"""
Además de TypeError se puede usar:
    except Exception as e:  # Captura cualquier tipo de error
        return f"Error: {e}"
"""
def suma_con_excepcion_2(a, b):
    try:
        resultado = a + b
        return resultado
    except Exception as e:  # Captura cualquier tipo de error y proporciona información detallada sobre el tipo de error.
        return f"Error: {e}"

print(suma_con_excepcion_2(8, 9))  # Resultado correcto
print(suma_con_excepcion_2(8, "a"))  


#Ingresar datos por el usuario
variable = input("pon tu nombre: ")
print(f"Tu nombre es: {variable}")