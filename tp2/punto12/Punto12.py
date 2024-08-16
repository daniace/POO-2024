from Persona import Persona
from Empresa import Empresa
from Puesto import Puesto

administrativo = Puesto("Administrativo")
gerente = Puesto("Gerente")
tesorero = Puesto("Tesorero")


def main():
    persona1 = Persona("Juan", "Perez", 20, "M", administrativo)
    persona2 = Persona("Maria", "Gomez", 15, "F", administrativo)
    persona3 = Persona("Carlos", "Lopez", 16, "M", administrativo)
    persona4 = Persona("Ana", "Diaz", 17, "F", gerente)
    persona5 = Persona("Pedro", "Rodriguez", 18, "M", tesorero)
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
