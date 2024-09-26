from abc import ABC


class Personal(ABC):
    def __init__(self, nombre, apellido, antiguedad, sector):
        self._nombre = nombre
        self._apellido = apellido
        self._antiguedad = antiguedad
        self._sector = sector
        self._horasSemanales = 0

    def get_horas_semanales(self):
        return self._horasSemanales
    
    def set_horas_semanales(self, horas):
        self._horasSemanales = horas

    def imprimir(self):
        print(f"Nombre: {self._nombre}")
        print(f"Apellido: {self._apellido}")
        print(f"Antigüedad: {self._antiguedad}")
        print(f"Sector: {self._sector}")
        print(f"Horas semanales: {self._horasSemanales}")
