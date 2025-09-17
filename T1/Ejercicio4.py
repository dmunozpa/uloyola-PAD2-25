####################
## EJERICIO 4
## Escribe un programa que simule el lanzamiento de dos dados y calcule la suma de los valores obtenidos.
####################
import random
from typing import Tuple

def lanza_dos_dados()-> Tuple[int, int]:
    """
    Lanza dos dados de seis caras y devuelve sus resultados.

    Returns:
        Tuple [int, int]: Una tupla que contiene los valores obtenidos 
        al lanzar el primer y el segundo dado. 
        Cada valor está en el rango de 1 a 6 (inclusive).
    """
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    return dado1,dado2

def main():
 
    dado1, dado2 = lanza_dos_dados()
    print(f"La suma de los datos es:",dado1+dado2)
    
if __name__ == "__main__":
    main()