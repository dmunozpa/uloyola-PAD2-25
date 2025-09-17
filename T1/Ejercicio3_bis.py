####################
## EJERICIO 3
## Desarrolle una calculadora de índice de masa corporal (IMC)
# que tome el peso y la altura de una persona y calcule su IMC. 
####################
## 
## Ref -- https://www.calculatorsoup.com/calculators/health/bmi-calculator.php
##


def calculate_imc(peso_kg:float, altura_m:float)->float:
    """
    Función que calcula el Índice de Masa Corporal
    Args:
        peso_kg (float): Peso en Kg
        altura_m (int): Altura en metros
    Returns:
        float: Devuelve el resultado en forma de float
    """
    imc = 0.0
    try:
        # TODO: Usa la variable imc, con la resultado de la fórmula = peso (kg) / (altura_m (m) * altura (m))
        imc = peso_kg / (altura_m * altura_m)
    except ZeroDivisionError:
        print("La áltura no puede ser cero. Introduce número válido")
    
    return imc
    

def main():

    print("Bienvenido a la calculadora del IMC!")
    
    try:
        # TODO: Usa la variable peso_kg. como float por teclado, usando un texto descriptivo
        # TODO: Usa la variable altura_m. como float por teclado, usando un texto descriptivo
        peso_kg = float(input("Dame tu peso en Kg, con dos decimales"))
        altura_m = float(input("Dame tu altura en Metros, con dos decimales"))
        bmi = calculate_imc(peso_kg, altura_m)

        print(f"Tu IMC es: {bmi:.2f}")
        
    
    except ValueError:
        return print("Valores deben de ser decimales con 2 dígitos. Introduce un valor válido")

if __name__ == "__main__":
    main()


## Adultos
## Menor que 18.5 está bajo de peso
## Entre 18.5 y 24.9 estas en tu índice correcto
## Entre 25 y 29.9 estas en sobre pero
## Más de 30 estás muy por encima 