from Persona import Persona

persona = Persona("Juan", "Perez", "01/01/1990")
print(persona)
print("Edad:", persona.calculoEdad())

persona2 = Persona(None, None, None)
persona2.setNombre("Pedro")
persona2.setApellido("Gomez")
persona2.setFechaNacimiento("02/02/1991")
print(persona2)
print("Edad:", persona2.calculoEdad())

persona3 = Persona("Maria", "Gomez", "03/03/1992")
print(persona3)
print("Edad:", persona3.calculoEdad())