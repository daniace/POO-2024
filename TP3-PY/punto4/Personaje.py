from abc import ABC, abstractmethod
from random import randint


class Personaje(ABC):
    def __init__(self, vida, nivelAtaque, nivelDefensa):
        self._vida = vida
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa

    def atacar(self) -> int:
        dano = randint(1, 100)
        return dano

    @abstractmethod
    def defender(self, ataque):
        pass
