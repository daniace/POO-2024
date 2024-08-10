class Cartelera:
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__listado_series = []

    def agg_series(self, estrenos):
        self.__listado_series.append(estrenos)

    def imprimir_listado_series(self):
        print("-- CATEGORIA:", self.__titulo, " --\n")
        for estrenos in self.__listado_series:
            estrenos.imprimo_serie()
