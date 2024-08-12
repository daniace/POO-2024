class Profesor:
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__materia = []
    
    @classmethod
    def inicio_con_profesor_y_apellido(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def materia(self):
        return self.__materia
    
    @materia.setter
    def materia(self, materia):
        self.__materia = materia

    def agregar_materia(self, materia):
        self.__materia.append(materia)
    