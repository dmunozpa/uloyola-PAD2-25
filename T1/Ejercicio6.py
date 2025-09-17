####################
## EJERICIO 6
# Simulación de cuenta bancaria
####################

# Definimos la cuenta como un diccionario
cuenta = {
    "titular": "Gladis Gonzales",
    "saldo": 10000.00
}

# Funcion de depositar
def depositar(cuenta:dict, monto:float):
    """
    Método depositar.
    Args:
        cuenta (dict): Cuenta a depositar.
        monto (float): Cantidad a depositar.
    """

    if monto > 0:
        cuenta["saldo"] += monto
        print(f"Depósito de {monto}€ realizado. Nuevo saldo: {cuenta['saldo']} €")
    else:
        print("El monto a depositar debe ser positivo.")

# Funcion de retirar
def retirar(cuenta:dict, monto:float):
    """
    Método de retirar de la cuenta, una candidad dada.
    Args:
        cuenta (dict): Cuenta a retirar.
        monto (float): Cantidad a retirar.
    """
    
    if 0 < monto <= cuenta["saldo"]:
        cuenta["saldo"] -= monto
        print(f"Retiro de {monto}€ realizado. Nuevo saldo: {cuenta['saldo']} €")
    else:
        print("Saldo insuficiente o monto inválido.")

def obtener_saldo(cuenta:dict)->float:
    return cuenta["saldo"]


# Ejemplos de uso
if __name__ == "__main__":

    # Menú de opciones
    print("-" * 60)
    print("- Bienvenido a Banco Loyola - ")
    print("-" * 60)
    print(f"Saldo actual de: {cuenta['titular']}: {obtener_saldo(cuenta)} €")
    print("-" * 60)
    
    accion = input("¿Desea realizar un:\n 1. Depósito\n 2. Retiro\n 3. Salir\n")
    if accion not in ["1", "2", "3"]:
        print("Opción no válida.")

    if accion == "3":
        print("Gracias por usar el Banco ULoyola.")

    while accion != "3":
        if accion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            depositar(cuenta, monto)
        elif accion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            retirar(cuenta, monto)
        else:
            print("Opción no válida.")
        
        accion = input("¿Desea realizar otro:\n 1. Depósito\n 2. Retiro\n 3. Salir\n")
        if accion not in ["1", "2", "3"]:
            print("Opción no válida.")
        if accion == "3":
            print("Gracias por usar el el Banco ULoyola.")
