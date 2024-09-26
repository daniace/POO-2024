from abc import ABC, abstractmethod

class Pagar(ABC):

    @abstractmethod
    def pagar_debito(self, monto):
        pass

    @abstractmethod
    def pagar_credito(self, monto, cuotas):
        pass