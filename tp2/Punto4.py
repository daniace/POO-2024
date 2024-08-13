from Materia import Materia
from Profesor import Profesor

poo = Materia("POO", "IF153")
algebra = Materia("Algebra", 183)
introduccion = Materia.inicio("Introduccion a la programacion")
introduccion.codigo = "IF0300"
algoritmica = Materia("Algoritmica", "500")

profesores = []

profesor1 = Profesor("Pedro", "Hernandez")
profesor1.agregar_materia(poo)
profesor1.agregar_materia(algebra)
profesores.append(profesor1)
profesor2 = Profesor("Juan", "Perez")
profesor2.agregar_materia(introduccion)
profesor2.agregar_materia(algoritmica)
profesores.append(profesor2)
profesor3 = Profesor("Maria", "Gomez")
profesores.append(profesor3)

for pro in profesores:
    print(f"{"Profesor: "}{pro.nombre}{", "}{pro.apellido}")
    print("Materias:")
    for mat in pro.materia:
        print(mat.imprimir())
