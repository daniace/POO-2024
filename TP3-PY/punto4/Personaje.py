from abc import ABC, abstractmethod
import random


class Personaje(ABC):
    def __init__(self):
        self._vida = 100
        self._nivelAtaque = self._genero_atributo()
        self._nivelDefensa = self._genero_atributo()

    def get_vida(self):
        return self._vida

    def _genero_atributo(self):
        return random.randint(1,100)

    def atacar(self) -> int:
        return self._nivelAtaque

    @abstractmethod
    def defender(self, ataque):
        pass

    def imprimir(self):
        print("--------------------------")
        print(f"{self.__class__.__name__}")
        print(f" - Vida: ❤ {self._vida}")
        print(f" - Ataque: ⚔ {self._nivelAtaque}")
        print(f" - Defensa: 🛡 {self._nivelDefensa}")
