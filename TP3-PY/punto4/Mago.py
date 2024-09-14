from Personaje import Personaje


class Mago(Personaje):

    def __init__(self, vida, nivelAtaque, nivelDefensa):
        super().__init__(vida, nivelAtaque, nivelDefensa)
        self.__vida = vida
        self.__nivelAtaque = nivelAtaque
        self.__nivelDefensa = nivelDefensa


    def defender(self, ataque):
        pass
