class Puesto:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"Puesto: {self.__nombre}"
