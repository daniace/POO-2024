from TarifaProveedor import TarifaProveedor


class Claro(TarifaProveedor):
    def __init__(self, nombre, sms, minutos, gigas):
        super().__init__(nombre, sms, minutos, gigas)
        self._nombre = nombre

    def calcularSMS(self):
        return super().calcularSMS() * 1.2

    def calcularMinutosDeLlamada(self):
        return super().calcularMinutosDeLlamada() * 1.2

    def calcularConsumoGB(self):
        return super().calcularConsumoGB() * 1.2

    def calcular(self):
        return self.calcularSMS() + self.calcularMinutosDeLlamada() + self.calcularConsumoGB()
