from Carta import Carta
from random import randint


class BronceEspecial(Carta):
    def __init__(self, nombre, equipo, pais, habilidad):
        super().__init__(nombre, equipo, pais)
        self.__habilidad = habilidad

    @property
    def habilidad(self):
        return self.__habilidad

    @habilidad.setter
    def habilidad(self, habilidad):
        self.__habilidad = habilidad

    def genero_atributo(self):
        return randint(49, 65) + 2

    def __str__(self):
        return super().__str__() + f"\nHabilidad: {self.habilidad}"
