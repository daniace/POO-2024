from TarifaProveedor import TarifaProveedor


class Movistar(TarifaProveedor):
    def __init__(self, nombre, sms, minutos, gigas):
        super().__init__(nombre, sms, minutos, gigas)
        self._nombre = nombre

    def calcularSMS(self):
        return super().calcularSMS() * 1.1

    def calcularMinutosDeLlamada(self):
        return super().calcularMinutosDeLlamada() * 1.2

    def calcularConsumoGB(self):
        return super().calcularConsumoGB() * 1.3

    def calcular(self):
        return self.calcularSMS() + self.calcularMinutosDeLlamada() + self.calcularConsumoGB()
