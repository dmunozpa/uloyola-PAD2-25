####################
## EJERCICIO 6
# Simulación de cuenta bancaria con Clases
####################

class CuentaBancaria:
    
    def __init__(self, titular: str, saldo_inicial: float):
        """
        Constructor de la cuenta bancaria.
        Args:
            titular (str): Nombre del titular de la cuenta.
            saldo_inicial (float): Saldo inicial de la cuenta.
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto: float):
        """Método para depositar dinero en la cuenta."""
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto}€ realizado. Nuevo saldo: {self.saldo} €")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto: float):
        """Método para retirar dinero de la cuenta."""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto}€ realizado. Nuevo saldo: {self.saldo} €")
        else:
            print("Saldo insuficiente o monto inválido.")

    def obtener_saldo(self) -> float:
        """Devuelve el saldo actual."""
        return self.saldo


# Ejemplo de uso con menú interactivo
if __name__ == "__main__":

    cuenta = CuentaBancaria("Gladis Gonzales", 10000.00)

    print("-" * 60)
    print("- Bienvenido a Banco Loyola - ")
    print("-" * 60)
    print(f"Saldo actual de {cuenta.titular}: {cuenta.obtener_saldo()} €")
    print("-" * 60)

    accion = input("¿Desea realizar un:\n 1. Depósito\n 2. Retiro\n 3. Salir\n")

    if accion not in ["1", "2", "3"]:
        print("Opción no válida.")

    if accion == "3":
        print("Gracias por usar el Banco ULoyola.")

    while accion != "3":
        if accion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif accion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        else:
            print("Opción no válida.")

        accion = input("¿Desea realizar otro:\n 1. Depósito\n 2. Retiro\n 3. Salir\n")
        if accion not in ["1", "2", "3"]:
            print("Opción no válida.")
        if accion == "3":
            print("Gracias por usar el Banco ULoyola.")
