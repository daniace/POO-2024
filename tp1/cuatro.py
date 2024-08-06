class Tienda:
    def __init__(self):
        self.listado_curso = []

    def agregar_curso(self, curso):
        self.listado_curso.append(curso)

    def imprimir_curso(self):
        for curso in self.listado_curso:
            print(f"Nombre: {curso.nombre}")
            print(f"Precio: {curso.precio}")
            print(f"Estrellas: {curso.estrellas}")
            print(f"Autor: {curso.autor}")
            print(f"Imagen: {curso.imagen}")
            print("\n")


class Curso:
    def __init__(self, nombre, precio, estrellas, autor, imagen):
        self.nombre = nombre
        self.precio = precio
        self.estrellas = estrellas
        self.autor = autor
        self.imagen = imagen


curso1 = Curso("Pytorch para Deep Learning", 12.99, 4.6, "Andrei Negroni", "PITON")
curso2 = Curso("Machine learning A-Z: AI Python & R + ChatGPT", 14.99, 4.5, "Krilin Esposito", "Humano")
curso3 = Curso("Deep Learning: Advanced Computer vision", 14.99, 4.5, "Lazy Town", "ojo")
curso4 = Curso("Applied Generative AI and Natural Language Processing", 12.99, 4.7, "Bert Gollok", "Carteles")
tiendita = Tienda()
tiendita.agregar_curso(curso1)
tiendita.agregar_curso(curso2)
tiendita.agregar_curso(curso3)
tiendita.agregar_curso(curso4)
tiendita.imprimir_curso()
