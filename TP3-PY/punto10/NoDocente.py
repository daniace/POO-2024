from Personal import Personal
import random

class NoDocente(Personal):
    def __init__(self, nombre, apellido, antiguedad, sector, jornada):
        super().__init__(nombre, apellido, antiguedad, sector)
        self.__jornada = jornada

    def get_jornada(self):
        return self.__jornada
    
    def calcular_horas_semanales(self):
        match self.__jornada:
            case "Completa":
                horas = 30
                horas_extras = random.randint(0,10)
                if random.randint(0,100) < 80:
                    horas += horas_extras
                    super().set_horas_semanales(horas)
                super().set_horas_semanales(horas)
            case "Reducida":
                horas = 20
                horas_extras = random.randint(0,10)
                if random.randint(0,100) < 80:
                    horas += horas_extras
                    super().set_horas_semanales(horas)
                super().set_horas_semanales(horas)

    def imprimir(self):
        super().imprimir()
        print(f"Jornada: {self.__jornada}")