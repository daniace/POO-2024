class Plantilla:
    def __init__(self, usuario, pais_favorito, equipo_favorito):
        self.__usuario = usuario
        self.__pais_favorito = pais_favorito
        self.__equipo_favorito = equipo_favorito
        self.__plantel = []

    @property
    def usuario(self):
        return self.__usuario

    @property
    def pais_favorito(self):
        return self.__pais_favorito

    @property
    def equipo_favorito(self):
        return self.__equipo_favorito

    @property
    def plantel(self):
        return self.__plantel

    @plantel.setter
    def plantel(self, plantel):
        self.__plantel = plantel

    def imprimir_plantel(self):
        for carta in self.__plantel:
            print(carta)

    def calcular_quimica_plantel(self):
        suma = 0
        for carta in self.__plantel:
            suma += carta.quimica
        return (suma / len(self.__plantel))

    def __str__(self):
        return (
            f"===================================\n"
            f"Usuario: {self.__usuario}\n"
            f"Pais favorito: {self.__pais_favorito}\n"
            f"Equipo favorito: {self.__equipo_favorito}\n"
            f"Plantel: {self.imprimir_plantel()}\n"
            f"Quimica Total: {self.calcular_quimica_plantel()}\n"
            f"===================================\n"
        )
