####################
## EJERICIO 1
## Suma de números pares: Escriba un programa que sume todos los números pares del 1 al 100. 
## - Optimización con parámetros de entrada
####################
def funcion_con_parametros(n_inicio:int, n_fin:int)-> int: 
    """
    Función que calcula la suma de numero pares con párametros
    Args:
        n_inicio (int): Número de Inicio para la suma
        n_fin (int): Número de Fin para la suma
    Returns:
        int: Devuelve el resultado en forma de entero
    """
    return sum([number for number in range(n_inicio, n_fin, 2)])


def main():
    n_inicio = 1
    n_fin = 101
    print(f"La suma de los número pares del {n_inicio} al {n_fin} es: {funcion_con_parametros(n_inicio,n_fin)}")
    

if __name__ ==  "__main__":
    main()