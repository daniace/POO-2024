class Serie:
    def __init__(self, nombre, estreno, urlImg):
        self.__nombre = nombre
        self.__estreno = estreno
        self.__urlImg = urlImg

    def imprimo_serie(self):
        print("Serie:", self.__nombre)
        print("Estreno:", self.__estreno)
        print("Url Image:", self.__urlImg, "\n")
