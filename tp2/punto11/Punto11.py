from Persona import Persona
from Empresa import Empresa


def main():
    persona1 = Persona("Juan", "Perez", 20, "M")
    persona2 = Persona("Maria", "Gomez", 15, "F")
    persona3 = Persona("Carlos", "Lopez", 16, "M")
    persona4 = Persona("Ana", "Diaz", 17, "F")
    persona5 = Persona("Pedro", "Rodriguez", 18, "M")
    empresa = Empresa("Teclas Inc", "Lomas turbas 6969")
    empresa.set_empleados(persona1)
    empresa.set_empleados(persona2)
    empresa.set_empleados(persona3)
    empresa.set_empleados(persona4)
    empresa.set_empleados(persona5)
    print(empresa)
    print("Cantidad de empleados:", empresa.total_empleados())
    empresa.imprimir_empleados()


main()
