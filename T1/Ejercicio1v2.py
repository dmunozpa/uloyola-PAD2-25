####################
## EJERICIO 1
## Suma de números pares: Escriba un programa que sume todos los números pares del 1 al 100. 
## Usando 3 opciones posibles
## OPCION 1 - Modulo
## OPCION 2 - Sumando de 2 en 2
## OPCION 3 - Usando el for in range
####################

############
# OPCION 1 #
############
def calculo_n_par_forma1():
    '''
    Calculo de N pares del 1 al 100 usando módulo.
    '''
    numero = 1
    resultado = 0
    n_iteraciones = 0
    
    while numero <= 100:      # Condición desde 1 al 100.
        n_iteraciones = n_iteraciones + 1
        if numero % 2 == 0:           # Condición de Par.
            resultado = resultado + numero        # Suma de los valores que son pares. (que cumple la condicion de arriba)
            
        numero = numero + 1           # incrementa en 1 el valor de numero.

    print("La suma de los número pares del 1 al 100 es:", resultado, " con N iteraciones: ",n_iteraciones)

############
# OPCION 2 #
############
def calculo_n_par_forma2():
    '''
    Cálculo de N pares del 1 al 100 sumando de 2 en 2.
    '''
    numero = 1
    resultado = 0
    n_iteraciones = 0

    while numero <= 100:
        n_iteraciones = n_iteraciones + 1
        resultado = resultado + numero
        numero = numero + 2

    print("La suma de los número pares del 1 al 100 es:", resultado, " con N iteraciones: ",n_iteraciones)


############
# OPCION 3 #
############
def calculo_n_par_forma3():
    '''
    Cálculo de N pares del 1 al 100 usando el iterador for in range
    '''
    numero = 1
    resultado = 0
    n_iteraciones = 0
    numero_salida = 101 

    for numero in range(1, numero_salida, 2):
        #print(" Valores de numero",numero)
        n_iteraciones = n_iteraciones + 1
        resultado += numero

    print("La suma de los número pares del 1 al 100 es:", resultado, " con N iteraciones: ",n_iteraciones)


def main():
    calculo_n_par_forma1()
    calculo_n_par_forma2()
    calculo_n_par_forma3()
    

if __name__ ==  "__main__":
    main()