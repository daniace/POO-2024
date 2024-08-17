from Puesto import Puesto


class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int, sexo: str, puesto: Puesto):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__sexo = sexo
        self.__puesto = puesto

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def __str__(self):
        return f"{self.__nombre} {self.__apellido} {self.__edad} años, {self.__sexo} {self.__puesto}"
