from abc import ABC

class Cuenta(ABC):
    def __init__(self, saldo, duenio, numero_cuenta):
        self._saldo = saldo
        self._duenio = duenio
        self._numero_cuenta = numero_cuenta
    
    def get_saldo(self):
        return self._saldo

    def imprimir(self):
        print(f"Dueño: {self._duenio}")
        print(f"Saldo: ${self._saldo}")
        print(f"Numero de cuenta: N°{self._numero_cuenta}")