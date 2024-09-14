from abc import ABC, abstractmethod


class TarifaProveedor(ABC):
    def __init__(self, nombre, sms, minutos, gigas):
        self._nombre = nombre
        self._sms = sms
        self._minutos = minutos
        self._gigas = gigas

    @property
    def nombre(self):
        return self._nombre

    def calcularSMS(self) -> float:
        totalSMS: int = self._sms * 1.0
        print(f"Para el proveedor {self._nombre} el total de {self._sms} SMS es: {totalSMS}")
        return totalSMS

    @abstractmethod
    def calcularMinutosDeLlamada(self) -> float:
        totalMinutos = self._minutos * 15.0
        print(f"Para el proveedor {self._nombre} el total de {self._minutos} minutos es: {totalMinutos}")
        return totalMinutos

    @abstractmethod
    def calcularConsumoGB(self) -> float:
        totalGigas = self._gigas * 20.0
        print(f"Para el proveedor {self._nombre} el total de {self._gigas} gigas es ${totalGigas}")
        return totalGigas

    @abstractmethod
    def calcular(self) -> float:
        return self.calcularSMS() + self.calcularMinutosDeLlamada() + self.calcularConsumoGB()
