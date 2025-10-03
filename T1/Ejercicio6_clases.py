####################
## EJERICIO 6
# Simulación de cuenta bancaria
####################

# Definimos la cuenta como una clase
class Cuenta:
    
    def __init__(self, titular:str, saldo:float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,monto:float):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto}€ realizado. Nuevo saldo: {self.saldo} €")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self,monto:float):
        if monto > 0 and self.saldo - monto > 0:
            self.saldo -= monto
            print(f"Retirada de {monto}€ realizado. Nuevo saldo: {self.saldo} €")
        else:
            print("El monto a retirar es incorrecto.")
    
    def muestra_saldo(self)->float:
        return self.saldo
    
    ### OPCIONAL
    def __str__(self) -> str:
        return f"Titular: {self.titular} \nSaldo: {self.saldo}"
    

###############

miCuentaLoyola = Cuenta("David",5000)

miCuentaLoyola.depositar(500)
print(f"La cuenta tiene {miCuentaLoyola.muestra_saldo()} € ")
miCuentaLoyola.retirar(700)
print(f"La cuenta tiene {miCuentaLoyola.muestra_saldo()} € ")


print(miCuentaLoyola)