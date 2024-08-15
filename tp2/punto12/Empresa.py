from Persona import Persona


class Empresa:
    def __init__(self, nombre: str, direccion: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__empleados = []

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_empleados(self):
        return self.__empleados

    def set_empleados(self, empleado: Persona):
        self.__empleados.append(empleado)

    def total_empleados(self):
        return len(self.__empleados)

    def imprimir_empleados(self):
        print("Empleados:")
        for empleado in self.__empleados:
            print(empleado)

    def __str__(self):
        return f"Empresa: {self.__nombre}, Direccion: {self.__direccion}"
