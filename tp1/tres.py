class Cartelera:
    def __init__(self):
        self.listado_series = []

    def agg_series(self, estrenos):
        self.listado_series.append(estrenos)

    def imprimir_estrenos(self):
        for estrenos in self.listado_series:
            print(estrenos.nombre)
            print(estrenos.estreno)
            print(estrenos.imagen)


class Serie:
    def __init__(self, nombre, estreno, imagen):
        self.nombre = nombre
        self.estreno = estreno
        self.imagen = imagen


serie = Serie('Breaking Bad', 'Todos los martes', 'BB')
serie2 = Serie('The boys', 'Todos los lunes', 'TB')
serie3 = Serie('Rick and morty', 'Todos los miercoles', 'RM')
cartelera = Cartelera()
cartelera.agg_series(serie)
cartelera.agg_series(serie2)
cartelera.agg_series(serie3)
cartelera.imprimir_estrenos()
