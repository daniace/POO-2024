class CuentaCorriente:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Deposito de ${cantidad} realizado con éxito. Nuevo saldo: ${self.saldo}")
        else:
            print("Cantidad a depostiar invalida.")


    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado con éxito. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insuficiente o cantidad a retirar invalida.")
    

    def get_saldo(self):
        return self.saldo
    

# cuenta = CuentaCorriente("Juan Perez", 1000)

# print(f"Dueño de la cuenta: {cuenta.titular}")
# print(f"Saldo de la cuenta: ${cuenta.get_saldo()}")

# cuenta.depositar(500)
# cuenta.retirar(200)
# cuenta.retirar(2000)

# print(f"Saldo de la cuenta: ${cuenta.get_saldo()}")