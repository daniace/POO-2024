from Persona import Persona


class Familia:
    def __init__(self):
        self.__personas = []

    def agregar_persona(self, persona: Persona):
        self.__personas.append(persona)

    def cantidad_personas(self):
        cantidad = len(self.__personas)
        return cantidad

    def promedio_edad(self):
        suma = 0
        for persona in self.__personas:
            suma += persona.get_edad()
        promedio = suma / len(self.__personas)
        return promedio

    def cantidad_trabajadores(self):
        cantidad = 0
        for persona in self.__personas:
            if persona.get_trabaja():
                cantidad += 1
        return cantidad

    def pueden_trabajar_manejar(self):
        for persona in self.__personas:
            persona.puede_trabajar()
            persona.puede_manejar()

    def imprimir(self):
        for persona in self.__personas:
            print(persona)
