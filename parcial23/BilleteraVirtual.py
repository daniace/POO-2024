from Cuenta import Cuenta
from Pagar import Pagar

class BilleteraVirtual(Cuenta, Pagar):
    def __init__(self, saldo, duenio, numero_cuenta, cvu):
        super().__init__(saldo, duenio, numero_cuenta)
        self.__cvu = cvu

    def pagar_debito(self, monto):
        if self._saldo > monto:
            self._saldo -= monto
            print(f"Pago de debito de ${monto} realizado con exito! \n")
        else:
            print(f"Saldo insuficiente ${self._saldo}\n")
            pass

    def pagar_credito(self, monto, cuotas):
        interes = cuotas * 0.08
        if self._saldo > monto:
            match cuotas:
                case 1:
                    self._saldo -= monto
                    print(f"Pago de credito de ${monto} realizado con exito! en 1 cuota \n")
                case 3:
                    self._saldo -= (monto / cuotas)
                    print(f"Pago de credito de ${monto} realizado con exito! en 3 cuotas \n")
                case 6 | 12:
                    self._saldo -= (monto / cuotas) + interes
                    print(f"Pago de credito de ${monto} realizado con exito! en {cuotas} cuotas con un interes de %{int(interes * 100)} \n")
        else:
            print(f"Saldo insuficiente ${self._saldo} \n")
            pass

    def imprimir(self):
        print("---BILLETERA VIRTUAL---")
        super().imprimir()
        print(f"CVU: {self.__cvu}")
        print("--------------------\n")


if __name__ == "__main__":
    billetera = BilleteraVirtual(10000, "Juan Perez", 123456, 987654)
    billetera.imprimir()
    billetera.pagar_debito(1000)
    billetera.imprimir()
    billetera.pagar_credito(1000, 12)
    billetera.imprimir()
    billetera.pagar_credito(1000, 3)
    billetera.imprimir()
    billetera.pagar_credito(1000, 1)
    billetera.imprimir()
    billetera.pagar_debito(10000) # Saldo insuficiente
    billetera.pagar_credito(10000, 12) # Saldo insuficiente
