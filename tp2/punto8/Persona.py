class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int, sexo: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__sexo = sexo
        self.__estudia = None
        self.__trabaja = None

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_estudia(self):
        return self.__estudia

    def get_trabaja(self):
        return self.__trabaja

    def set_estudia(self, estudia: bool):
        self.__estudia = estudia

    def set_trabaja(self, trabaja: bool):
        if Persona.puede_trabajar(self):
            self.__trabaja = trabaja
        else:
            self.__trabaja = False

    def puede_trabajar(self):
        if self.__edad >= 16:
            print(f"{self.__nombre} Tiene edad suficiente para trabajar ({self.__edad} años)")
        else:
            print(f"{self.__nombre} Tiene edad insuficiente para trabajar ({self.__edad} años)")

    def puede_manejar(self):
        if self.__edad >= 17:
            print(f"{self.__nombre} Tiene edad suficiente para manejar ({self.__edad} años)")
        else:
            print(f"{self.__nombre} Tiene edad insuficiente para manejar ({self.__edad} años)")

    def __str__(self):
        return (f"{self.__nombre} {self.__apellido} {self.__edad} años, {self.__sexo}, trabaja: {self.__trabaja}, "
                f"estudia: {self.__estudia}")
