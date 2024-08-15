class Alumno:
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__dni = 0
    
    @classmethod
    def iniciar_con_nombre_apellido(cls, nombre, apellido):
        alumno = cls.__new__(cls)
        alumno.__nombre = nombre
        alumno.__apellido = apellido
        return alumno
    
    def getNombreYapellido(self):
        return f'{self.__nombre} {self.__apellido}'
    
    def getDni(self):
        return self.__dni
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def setDni(self, dni):
        self.__dni = dni