class Curso:
    def __init__(self, nombre, precio, descuento, estrellas, valoraciones, imagen):
        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento
        self.__estrellas = estrellas
        self.__valoraciones = valoraciones
        self.__lista_instructores = []
        self.__etiqueta = None
        self.__imagen = imagen

    def agregar_instructores(self, instructor):
        self.__lista_instructores.append(instructor)

    @property
    def etiqueta(self):
        return self.__etiqueta

    @etiqueta.setter
    def etiqueta(self, valor):
        self.__etiqueta = valor

    def imprimo_curso(self):
        print("Nombre:", self.__nombre)
        print("Precio:", self.__precio)
        print("Descuento:", self.__descuento)
        print("Estrellas:", self.__estrellas)
        print("Valoraciones:", self.__valoraciones)
        cadena = "Instructor/es: "
        for instructor in self.__lista_instructores:
            cadena += instructor + " - "
        print(cadena)
        print("Etiqueta:", self.__etiqueta)
        print("Imagen:", self.__imagen, "\n")
