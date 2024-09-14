from TarifaProveedor import TarifaProveedor


class Personal(TarifaProveedor):
    def __init__(self, nombre, sms, minutos, gigas):
        super().__init__(nombre, sms, minutos, gigas)
        self._nombre = nombre

    def calcularMinutosDeLlamada(self) -> float:
        return super().calcularMinutosDeLlamada() * 1.2

    def calcularConsumoGB(self) -> float:
        return super().calcularConsumoGB() * 1.5

    def calcular(self) -> float:
        return self.calcularSMS() + self.calcularMinutosDeLlamada() + self.calcularConsumoGB()
