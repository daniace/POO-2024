import datetime
import random


class Persona:
    def __init__(self, nombre, genero, email, fechaNacimiento):
        self.__nombre = nombre
        self.__genero = genero
        self.__email = email
        self.__contrasenia = (self.genero_constrasenia())
        self.__fechaNacimiento = datetime.date(year=int(fechaNacimiento.split("/")[2]), month=int(fechaNacimiento.split("/")[1]), day=int(fechaNacimiento.split("/")[0]))

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    
    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

    def genero_constrasenia(self):
        return "pas"+str(random.randint(1000, 9999))
        

    def __str__(self):
        return f"Nombre: {self.__nombre}, Genero: {self.__genero}, Email: {self.__email}, Constraseña: {self.__contrasenia}, Fecha de Nacimiento: {self.__fechaNacimiento}"
    
    def imprimir(self):
        print(self.__str__())