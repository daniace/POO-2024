from Carta import Carta
from random import randint


class Especial(Carta):
    def __init__(self, nombre, equipo, pais, habilidad: list[str]):
        super().__init__(nombre, equipo, pais)
        self.__habilidad: list[str] = habilidad

    @property
    def habilidad(self):
        return self.__habilidad

    @habilidad.setter
    def habilidad(self, habilidad):
        self.__habilidad.append(habilidad)

    def genero_atributo(self):
        if (randint(89, 99) + 1.02) >= 99:
            return 99
        else:
            return randint(89, 99) + 1.02

    def imprimo_habilidades(self):
        contador = 1
        for habilidad in self.__habilidad:
            print(f"Habilidad {contador}: {habilidad}")
            contador += 1

    def __str__(self):
        return super().__str__() + f"\nHabilidad: {self.imprimo_habilidades()}"
