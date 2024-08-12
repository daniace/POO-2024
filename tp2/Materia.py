class Materia:
    def __init__(self):
        self.__nombre = None
        self.__codigo = None

    @classmethod
    def inicio_con_materia_y_codigo(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    