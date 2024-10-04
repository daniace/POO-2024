from Publicacion import Publicacion


class Revista(Publicacion):
    def __init__(self, isbn, titulo, anio_publicacion, revista_numero):
        super().__init__(isbn, titulo, anio_publicacion)
        self.__revista_numero = revista_numero


    def presta(self):
        print(f"Se prestó la Revista: {self._titulo} N°{self.__revista_numero}")
        self._prestado = True

    
    def devuelve(self):
        print(f"Se devolvió la Revista: {self._titulo} N°{self.__revista_numero}")
        self._prestado = False

    def estaPrestado(self):
        if self._prestado:
            print(f"La Revista: {self._titulo} esta prestado.")
            return True
        else:
            print(f"La Revista: {self._titulo} no esta prestado.")
            return False


    def imprimir(self):
        print(" --- REVISTA --- ")
        super().imprimir()
        print(f"N°{self.__revista_numero}")
        print("-----------------")