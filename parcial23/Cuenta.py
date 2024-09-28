from abc import ABC
from Pagar import Pagar

class Cuenta(Pagar, ABC):
    def __init__(self, saldo, duenio, numero_cuenta):
        self._saldo = saldo
        self._duenio = duenio
        self._numero_cuenta = numero_cuenta
    
    def get_saldo(self):
        return self._saldo
    
    def pagar_debito(self, monto):
        if self._saldo > monto:
            self._saldo -= monto
            print(f"Pago de debito de ${monto} realizado con exito! \n")
        else:
            print(f"Saldo insuficiente ${round(self._saldo,2)}\n")
            pass

    def pagar_credito(self, monto, cuotas):
        pass

    def imprimir(self):
        print(f"Dueño: {self._duenio}")
        print(f"Saldo: ${self._saldo}")
        print(f"Numero de cuenta: N°{self._numero_cuenta}")