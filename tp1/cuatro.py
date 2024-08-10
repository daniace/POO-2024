from Tienda import Tienda
from Curso import Curso

curso1 = Curso("Pytorch para Deep Learning", 12.99, 74.99, 4.6, "2,907", "PITON")
curso1.agregar_instructores("Andrei Neagoie")
curso1.agregar_instructores("Daniel Bourke")
curso1.etiqueta = "BestSeller"

curso2 = Curso("Machine learning A-Z: AI Python & R + ChatGPT", 14.99, 84.99, 4.5, "184,477", "Humano")
curso2.agregar_instructores("Krillin  Eremeko")
curso2.agregar_instructores("Hadelin DePaul")
curso2.etiqueta = "BestSeller"

curso3 = Curso("Deep Learning: Advanced Computer vision", 14.99, 79.99, 4.6, "6,157", "Ojo")
curso3.agregar_instructores("Lazy Programming Inc")

curso4 = Curso("Applied Generative AI and Natural Language Processing", 12.99, 54.99, 4.7, 88, "Carteles")
curso4.agregar_instructores("Bert Bollnick")
curso4.etiqueta = "Hot & New"

tiendita = Tienda()
tiendita.agregar_curso(curso1)
tiendita.agregar_curso(curso2)
tiendita.agregar_curso(curso3)
tiendita.agregar_curso(curso4)
tiendita.imprimir_curso()
