####################
## EJERICIO 2
## Desarrollar un juego donde la computadora 
## elija un número aleatorio y el jugador debe adivinarlo dentro de un número limitado de intentos.  
####################
import random


def adivina_el_nunero():
    '''
    Función principal para adivinar el número.
    '''
    # Variables
    min_number = 1
    max_number = 100
    max_intentos = 10

    # Genera un numero aleatorio entre un minimo y un máximo.
    numero_secreto = random.randint(min_number, max_number)

    print(f"Bienvenido a Adivina el Número")
    print(f"Estoy pensando un número entre {min_number} y {max_number}.")

    for intento in range(1, max_intentos + 1):
        
        print(f"Este es el intento [{intento}], y dispones como máximo de [{max_intentos}]")
        
        # TODO: Usa la variable numero_entrada. como entero por teclado, usando un texto descriptivo
        
        # TODO: Comprueba que el numero de entrada es menor que numero secreto
            print("Prueba un número más alto. ")
        # TODO: Comprueba que el numero de entrada es mayor que numero secreto
            print("Prueba un número más bajo. ")
        else:
            # TODO: Muestra mensaje ganado
            break
    else:
        print(f"Lo siento, no tienes más intentos disponibles. El número secreto era: {numero_secreto}.")

if __name__ == "__main__":
    adivina_el_nunero()