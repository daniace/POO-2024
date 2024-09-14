from Carta import Carta
from random import randint


class Oro(Carta):
    def __init__(self, nombre, equipo, pais):
        super().__init__(nombre, equipo, pais)

    def genero_atributo(self):
        return randint(74,90) + 1.05