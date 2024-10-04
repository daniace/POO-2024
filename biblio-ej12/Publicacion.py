from Prestable import Prestable
from abc import ABC, abstractmethod


class Publicacion(Prestable, ABC):
    def __init__(self, isbn, titulo, anio_publicacion):
        self._isbn = isbn
        self._titulo = titulo
        self._anio_publicacion = anio_publicacion
        self._prestado = False



    @abstractmethod
    def presta(self):
        pass


    @abstractmethod
    def devuelve(self):
        pass


    @abstractmethod
    def estaPrestado(self):
        pass


    @abstractmethod
    def imprimir(self):
        print(f"ISBN:   {self._isbn}")
        print(f"Título: {self._titulo}")
        print(f"Año de Publicación: {self._anio_publicacion}")
        if self._prestado:
            print("Estado: Prestado")
        else:
            print("Estado: Disponible")