import random

class Reloj():
    def __init__(self):
        self.__personal = []

    def agregar_personal(self, personal):
        self.__personal.append(personal)

    def horitas(self):
        for personal in self.__personal:
            personal.calcular_horas_semanales()

    def calcular_horas_mensuales(self):
        for personal in self.__personal:
            horas_mensuales = personal.get_horas_semanales() * 4
            return horas_mensuales

    def imprimir_informe(self):
        for personal in self.__personal:
            personal.imprimir()
            print(f"Horas mensuales: {self.calcular_horas_mensuales()} \n")