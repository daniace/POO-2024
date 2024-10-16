from abc import ABC, abstractmethod


class Juego(ABC):
    def __init__(self) -> None:
        self.__id_juego = int
        self.__importe = float
    
    # Calcular el precio del juego
    @abstractmethod
    def getPrecio(self):
        pass

class JuegoDigital(Juego):
    def __init__(self) -> None:
        super().__init__()
        self.__plataforma = str
    
    def getPrecio(self):
        pass


class JuegoFisico(Juego):
    def __init__(self) -> None:
        super().__init__()
        self.__precio_traslado = float

    def getPrecio(self):
        pass

