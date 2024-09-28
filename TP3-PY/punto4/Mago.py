from Personaje import Personaje
import random


class Mago(Personaje):
    def __init__(self):
        super().__init__()
        self.__regeneracion_magica = random.randint(1,20) # El mago tiene 25% de probabilidad de regenerarse la vida al momento de un ataque
        self.__efecto_veneno = random.randint(1,20) # El mago tiene un 15% de probabilidad de lanzar un ataque venenoso

    def defender(self, ataque):
        print(f"{self.__class__.__name__} recibio un ataque de ⚔ {ataque} puntos de daño.")
        if random.randint(1,100) < 25:
            danio = max(0, ataque - self._nivelDefensa + self.__regeneracion_magica)
            print(f"Se defendio con sus 🛡 {self._nivelDefensa} puntos de defensa.")
            print(f"Y se regenero la vida con 🌟 {self.__regeneracion_magica} puntos de regeneracion.")
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
    
    def atacar(self) -> int:
        if random.randint(1,100) < 15:
            print(f"{self.__class__.__name__} arrojo un ataque venenoso! ✨")
            return self._nivelAtaque + self.__efecto_veneno
        else:
            return self._nivelAtaque

    def imprimir(self):
        super().imprimir()
        print(f" - Regeneracion Magica: 🌟 {self.__regeneracion_magica}")
        print(f" - Efecto Venenoso ✨ {self.__efecto_veneno}")