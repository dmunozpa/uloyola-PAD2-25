####################
## EJERICIO 1
## Suma de números pares: Escriba un programa que sume todos los números pares del 1 al 100. 
####################
def calculo_n_pares():
    
    resultado = 0
    numero = 2
    
    while numero <= 100:
        resultado += numero
        numero += 2 

    print("La suma de los número pares del 1 al 100 es:", resultado) 


def main():
    calculo_n_pares()
    

if __name__ ==  "__main__":
    main()