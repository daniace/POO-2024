from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Match


class BuilderTorta(ABC):

    @property
    @abstractmethod
    def torta(self) -> None:
        pass

    @abstractmethod
    def torta(self) -> None:
        pass

    @abstractmethod
    def produce_masa(self) -> None:
        pass

    @abstractmethod
    def produce_relleno(self) -> None:
        pass


class ConcreteBuilderTorta(BuilderTorta):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._torta = Torta()

    @property
    def torta(self) -> Torta:
        torta = self._torta
        self.reset()
        return torta

    def produce_masa(self) -> None:
        print(" 1 - Vainilla \n"
              " 2 - Coco \n"
              " 3 - Chocolate \n")
        eleccion = int(input("Elige el sabor de la masa: "))
        match eleccion:
            case 1:
                self._torta.add("Masa de Vainilla")
                self._torta.setMasa("Vainilla")
            case 2:
                self._torta.add("Masa de Coco")
                self._torta.setMasa("Coco")
            case 3:
                self._torta.add("Masa de Chocolate")
                self._torta.setMasa("Chocolate")
            case _:
                print("Sabor no encontrado")

    def produce_relleno(self) -> None:
        print(" 1 - Dulce de leche \n"
              " 2 - Durazno con crema \n"
              " 3 - Frutos rojos \n")
        eleccion = int(input("Elige el relleno de la torta: "))
        match eleccion:
            case 1:
                self._torta.add("Relleno de Dulce de Leche")
                self._torta.setRelleno("Dulce de leche")
            case 2:
                self._torta.add("Relleno de Durazno con crema")
                self._torta.setRelleno("Durazno con crema")
            case 3:
                self._torta.add("Relleno de Frutos Rojos")
                self._torta.setRelleno("Frutos Rojos")
            case _:
                print("Anda a mirar naruto")


class Torta:
    def __init__(self) -> None:
        self.ingredientes = []
        self.__masa = str
        self.__relleno = str

    def setMasa(self, valor):
        self.__masa = valor

    def setRelleno(self, valor):
        self.__relleno = valor

    def add(self, ingrediente: Any) -> None:
        self.ingredientes.append(ingrediente)

    def lista_ingredientes(self) -> None:
        print(f"Ingredientes de la Torta: {', '.join(self.ingredientes)}", end="")
        print("\n")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderTorta:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderTorta) -> None:
        self._builder = builder

    def build_torta(self) -> None:
        self.builder.produce_masa()
        self.builder.produce_relleno()


director = Director()
builder = ConcreteBuilderTorta()
director.builder = builder

director.build_torta()
builder.torta.lista_ingredientes()

director.build_torta()
builder.torta.lista_ingredientes()

director.build_torta()
builder.torta.lista_ingredientes()

print("\n")
