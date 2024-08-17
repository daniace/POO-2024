from Persona import Persona
from Familia import Familia
from Comuna import Comuna

persona1 = Persona("Juan", "Perez", 25, "M")
persona1.set_estudia(True)
persona1.set_trabaja(True)

persona2 = Persona("Maria", "Gomez", 22, "F")
persona2.set_estudia(True)
persona2.set_trabaja(False)

persona3 = Persona("Pedro", "Gonzalez", 30, "M")
persona3.set_estudia(False)
persona3.set_trabaja(True)

familia1 = Familia()
familia1.agregar_persona(persona1)
familia1.agregar_persona(persona2)
familia1.agregar_persona(persona3)

persona4 = Persona("Ana", "Garcia", 20, "F")
persona4.set_estudia(True)
persona4.set_trabaja(False)

persona5 = Persona("Carlos", "Lopez", 40, "M")
persona5.set_estudia(False)
persona5.set_trabaja(True)

familia2 = Familia()
familia2.agregar_persona(persona4)
familia2.agregar_persona(persona5)

persona6 = Persona("Lucia", "Martinez", 15, "F")
persona6.set_estudia(True)
persona6.set_trabaja(False)

persona7 = Persona("Jorge", "Rodriguez", 17, "M")
persona7.set_estudia(False)
persona7.set_trabaja(True)

persona8 = Persona("Laura", "Diaz", 16, "F")
persona8.set_estudia(True)
persona8.set_trabaja(True)

familia3 = Familia()
familia3.agregar_persona(persona6)
familia3.agregar_persona(persona7)
familia3.agregar_persona(persona8)

comuna = Comuna()
comuna.agregar_familia(familia1)
comuna.agregar_familia(familia2)
comuna.agregar_familia(familia3)
comuna.imprimir()
print("Cantidad de Familias en la comuna:", comuna.cantidad_familias())
print("Cantidad de Personas en la comuna:", comuna.cantidad_personas_comuna())
print("Promedio de edad en la comuna:", comuna.promedio_edad_comuna())
print("Cantidad de Trabajadores en la comuna:", comuna.cantidad_trabajadores_comuna())

familia3.pueden_trabajar_manejar()