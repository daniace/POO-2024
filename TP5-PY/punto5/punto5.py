from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


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

    @abstractmethod
    def produce_sabor_vainilla(self) -> None:
        pass

    @abstractmethod
    def produce_sabor_coco(self) -> None:
        pass

    @abstractmethod
    def produce_sabor_chocolate(self) -> None:
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
        self._torta.add("500g de masa :v")

    def produce_relleno(self) -> None:
        self._torta.add("250g de naruto XD")

    def produce_sabor_vainilla(self) -> None:
        self._torta.add("Sabor Vainilla")

    def produce_sabor_coco(self) -> None:
        self._torta.add("Sabor Coco")

    def produce_sabor_chocolate(self) -> None:
        self._torta.add("Sabor Chocolate")


class Torta():
    def __init__(self) -> None:
        self.ingredientes = []

    def add(self, ingrediente: Any) -> None:
        self.ingredientes.append(ingrediente)

    def lista_ingredientes(self) -> None:
        print(f"Ingredientes de la Torta: {', '.join(self.ingredientes)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderTorta:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderTorta) -> None:
        self._builder = builder

    def build_vainilla(self) -> None:
        self.builder.produce_masa()
        self.builder.produce_relleno()
        self.builder.produce_sabor_vainilla()

    def build_coco(self) -> None:
        self.builder.produce_masa()
        self.builder.produce_relleno()
        self.builder.produce_sabor_coco()

    def build_chocolate(self) -> None:
        self.builder.produce_masa()
        self.builder.produce_relleno()
        self.builder.produce_sabor_chocolate()


director = Director()
builder = ConcreteBuilderTorta()
director.builder = builder

print("Torta de Vainilla: ")
director.build_vainilla()
builder.torta.lista_ingredientes()

print("\n")

print("Torta de Coco: ")
director.build_coco()
builder.torta.lista_ingredientes()

print("\n")

print("Torta de Chocolate: ")
director.build_chocolate()
builder.torta.lista_ingredientes()
