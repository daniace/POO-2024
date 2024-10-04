from Publicacion import Publicacion


class Libro(Publicacion):
    def __init__(self, isbn, titulo, anio_publicacion):
        super().__init__(isbn, titulo, anio_publicacion)


    def presta(self):
        print(f"Se prestó el Libro: {self._titulo}")
        self._prestado = True

    
    def devuelve(self):
        print(f"Se devolvió el Libro: {self._titulo}")
        self._prestado = False


    def estaPrestado(self):
        if self._prestado:
            print(f"El Libro: {self._titulo} esta prestado.")
            return True
        else:
            print(f"El Libro: {self._titulo} no esta prestado.")
            return False
        

    def imprimir(self):
        print(" ---- LIBRO ---- ")
        super().imprimir()
        print("-----------------")