from Familia import Familia


class Comuna:
    def __init__(self):
        self.__familias = []

    def agregar_familia(self, familia: Familia):
        self.__familias.append(familia)

    def cantidad_familias(self):
        cantidad = len(self.__familias)
        return cantidad

    def cantidad_personas_comuna(self):
        cantidad = 0
        for familia in self.__familias:
            cantidad += familia.cantidad_personas()
        return cantidad

    def promedio_edad_comuna(self):
        suma = 0
        for familia in self.__familias:
            suma += familia.promedio_edad()
        promedio = suma / len(self.__familias)
        return round(promedio, 2)

    def cantidad_trabajadores_comuna(self):
        cantidad = 0
        for familia in self.__familias:
            cantidad += familia.cantidad_trabajadores()
        return cantidad

    def imprimir(self):
        i = 1
        print("--- COMUNA ---")
        for familia in self.__familias:
            print("-- Familia:", i, "--")
            i += 1
            familia.imprimir()
