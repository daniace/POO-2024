from abc import ABC, abstractmethod


class Prestable(ABC):

    @abstractmethod
    def presta(self):
        pass


    @abstractmethod
    def devuelve(self):
        pass


    @abstractmethod
    def estaPrestado(self):
        pass