from abc import ABC, abstractmethod
import random


class Pokemon(ABC):
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._vida: int = 100
        self._ataque = self.genero_atributo()
        self._defensa = self.genero_atributo()
        self._velocidad = self.genero_atributo()
        self._debilidad = self.genero_atributo()
        self._salvajismo = self.genero_atributo()

    @property
    def vida(self):
        return self._vida

    @property
    def ataque(self):
        return self._ataque

    @property
    def defensa(self):
        return self._defensa

    @property
    def velocidad(self):
        return self._velocidad

    @property
    def debilidad(self):
        return self._debilidad

    @property
    def salvajismo(self):
        return self._salvajismo

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    @ataque.setter
    def ataque(self, valor):
        self._ataque = valor

    @defensa.setter
    def defensa(self, valor):
        self._defensa = valor

    @velocidad.setter
    def velocidad(self, valor):
        self._velocidad = valor

    @debilidad.setter
    def debilidad(self, valor):
        self._debilidad = valor

    @salvajismo.setter
    def salvajismo(self, valor):
        self._salvajismo = valor

    def genero_atributo(self):
        return random.randint(0, 100)

    def imprimir_pokemon(self):
        print(
            f"Nombre: {self._nombre} \n Ataque: {self._ataque} \n Defensa: {self._defensa} \n Velocidad: {self._velocidad} \n Salvajismo: {self._salvajismo} \n"
        )

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def defender(self, atacante):
        pass
