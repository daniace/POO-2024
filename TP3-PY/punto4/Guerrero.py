from Personaje import Personaje
import random


class Guerrero(Personaje):
    def __init__(self):
        super().__init__()
        self.__escudo = random.randint(1,20) # El guerrero tiene un 30% de probabilidad de cubrirse del ataque con el escudo

    def defender(self, ataque):
        print(f"{self.__class__.__name__} recibio un ataque de ⚔ {ataque} puntos de daño.")
        if random.randint(1,100) < 30:
            danio = max(0, ataque - self._nivelDefensa + self.__escudo)
            print(f"Se defendio con sus 🛡 {self._nivelDefensa} puntos de defensa.")
            print(f"Y cubrio el ataque con su escudo disminuyendo 🛡 {self.__escudo} puntos.")
        else:
            danio = max(0, ataque - self._nivelDefensa)
            print(f"Se defendio con sus 🛡 {self._nivelDefensa} puntos de defensa.")
        self._vida -= danio
        if self._vida > 0:
            print(f" - Vida {self.__class__.__name__} restante ❤ {self._vida}")
        else:
            print(f" - {self.__class__.__name__} Murio 💀")
            pass
        return danio
    
    def imprimir(self):
        super().imprimir()
        print(f" - Escudo: 🛡 {self.__escudo}")
