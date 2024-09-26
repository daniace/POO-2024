from Personal import Personal
import random

class Docente(Personal):
    def __init__(self, nombre, apellido, antiguedad, sector, categoria):
        super().__init__(nombre, apellido, antiguedad, sector)
        self.__categoria = categoria

    def get_categoria(self):
        return self.__categoria
    
    def calcular_horas_semanales(self):
        match self.__categoria:
            case "Simple":
                horas = 10
                horas_extras = random.randint(0,10)
                if random.randint(0,100) < 95:
                    horas += horas_extras
                    super().set_horas_semanales(horas)
                super().set_horas_semanales(horas)
            case "Semiexclusivo":
                horas = 20
                horas_extras = random.randint(0,10)
                if random.randint(0,100) < 75:
                    horas += horas_extras
                    super().set_horas_semanales(horas)
                super().set_horas_semanales(horas)
            case "Exclusiva":
                horas = 40
                horas_extras = random.randint(0,10)
                if random.randint(0,100) < 60:
                    horas += horas_extras
                    super().set_horas_semanales(horas)
                super().set_horas_semanales(horas)

    def imprimir(self):
        super().imprimir()
        print(f"Categoría: {self.__categoria}")
