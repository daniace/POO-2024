from datetime import date, datetime


class Persona:
    def __init__(self, nombre, apellido, fechaNacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = date.today() if fechaNacimiento is None else datetime.strptime(fechaNacimiento, '%d/%m/%Y')

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def setFechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = datetime.strptime(fechaNacimiento, '%d/%m/%Y')

    def __str__(self):
        return f'{self.__nombre} {self.__apellido} {self.__fechaNacimiento.strftime('%d-%m-%Y')}'
    
    def calculoEdad(self):
        edad = datetime.now()
        edadfinal = int(edad.year) - int(self.__fechaNacimiento.year)
        return edadfinal