from abc import ABC


class Personal(ABC):
    def __init__(self, nombre, apellido, antiguedad, sector):
        self._nombre = nombre
        self._apellido = apellido
        self._antiguedad = antiguedad
        self._sector = sector
        self._horasSemanales = 0

    @property
    def horasSemanales(self):
        return self._horasSemanales

    @horasSemanales.setter
    def horasSemanales(self, horas):
        self._horasSemanales = horas
