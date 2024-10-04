from Libro import Libro
from Revista import Revista


libro1 = Libro("123456", "La Ruta Prohibida", 2007)
libro2 = Libro("112233", "Los Otros", 2016)
libro3 = Libro("456789", "La rosa del mundo", 1995)

revista1 = Revista("444555", "Año Cero", 2019, 344)
revista2 = Revista("002244", "National Geographic", 2003, 255)

libro1.imprimir()
libro2.imprimir()
libro3.imprimir()

revista1.imprimir()
revista2.imprimir()

libro2.presta()
if libro2.estaPrestado():
    print("El libro está prestado")

libro2.presta()
libro2.devuelve()

if libro2.estaPrestado():
    print("El libro está prestado")

libro3.presta()
libro2.imprimir()
libro3.imprimir()
