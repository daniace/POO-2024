from Serie import Serie
from Cartelera import Cartelera

serie1 = Serie("Breaking Bad", "Todos los Lunes", "https://en.wikipedia.org/wiki/Breaking_Bad")

serie2 = Serie("Rick and Morty", "Todos los Martes", "https://en.wikipedia.org/wiki/Rick_and_Morty")

serie3 = Serie("Los simpsons", "Todos los Miercoles", "https://en.wikipedia.org/wiki/Los_simpsons")

cartelera = Cartelera("Nuevos lanzamientos")
cartelera.agg_series(serie1)
cartelera.agg_series(serie2)
cartelera.agg_series(serie3)
cartelera.imprimir_listado_series()
