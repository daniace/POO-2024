from abc import ABC, abstractmethod


class Carta(ABC):
    @abstractmethod
    def __init__(self, nombre, equipo, pais):
        self.__nombre = nombre
        self.__equipo = equipo
        self.__pais = pais
        self.__velocidad = self.genero_atributo()
        self.__tiro = self.genero_atributo()
        self.__regate = self.genero_atributo()
        self.__defensa = self.genero_atributo()
        self.__pase = self.genero_atributo()
        self.__fisico = self.genero_atributo()
        self.__quimica = any

    @property
    def nombre(self):
        return self.__nombre

    @property
    def equipo(self):
        return self.__equipo

    @property
    def pais(self):
        return self.__pais

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def tiro(self):
        return self.__tiro

    @property
    def regate(self):
        return self.__regate

    @property
    def defensa(self):
        return self.__defensa

    @property
    def pase(self):
        return self.__pase

    @property
    def fisico(self):
        return self.__fisico

    @property
    def quimica(self):
        return self.__quimica

    @velocidad.setter
    def velocidad(self, velocidad):
        self.__velocidad = velocidad

    @tiro.setter
    def tiro(self, tiro):
        self.__tiro = tiro

    @regate.setter
    def regate(self, regate):
        self.__regate = regate

    @defensa.setter
    def defensa(self, defensa):
        self.__defensa = defensa

    @pase.setter
    def pase(self, pase):
        self.__pase = pase

    @fisico.setter
    def fisico(self, fisico):
        self.__fisico = fisico

    @quimica.setter
    def quimica(self, quimica):
        self.__quimica = quimica

    @abstractmethod
    def genero_atributo(self):
        pass

    def calcular_quimica(self, pais_favorito, equipo_favorito):
        if self.__class__.__name__ == "Especial":
            self.__quimica = 100
        elif (self.__pais == pais_favorito) and (self.__equipo == equipo_favorito):
            self.__quimica = 100
        elif (self.__pais == pais_favorito) or (self.__equipo == equipo_favorito):
            self.__quimica = 80
        else:
            self.__quimica = 0

    def __str__(self):
        return (
            f"===================================\n"
            f"Carta: {self.__class__.__name__} \n"
            f"Nombre: {self.nombre} \n"
            f"Equipo: {self.equipo} \n"
            f"Pais: {self.pais} \n"
            f"Velocidad: {self.velocidad} \n"
            f"Tiro: {self.tiro} \n"
            f"Regate: {self.regate} \n"
            f"Defensa: {self.defensa} \n"
            f"Pase: {self.pase} \n"
            f"Fisico: {self.fisico} \n"
            f"Quimica: {self.quimica}\n"
            f"===================================\n"
        )
