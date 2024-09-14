from BronceEspecial import BronceEspecial
from Especial import Especial
from Oro import Oro
from Plantilla import Plantilla
from random import choice, choices, shuffle, randint

habilidades_especiales = ["Ataque", "Pase", "Defensa"]
equipos = ["Arsenal", "Montevideo City Torque", "Inter Miami", "Manchester City"]
paises = ["Argentina", "Inglaterra", "Holanda", "Japon"]
usuarios = ["Wolfav", "Dimidio", "Dari", "Ocus", "Hachazo"]
nombres_cartas = ["Record Breaker", "Flashback", "Showdown", "Ones to Watch", "Headliners", "Future Stars", "Shapeshifters"]

plantilla1 = Plantilla(choice(usuarios), choice(paises), choice(equipos))
plantilla2 = Plantilla(choice(usuarios), choice(paises), choice(equipos))

cartas = []

for i in range(8):
    bronce = BronceEspecial(choice(nombres_cartas), choice(equipos), choice(paises), choice(habilidades_especiales))
    bronce.calcular_quimica(plantilla1.pais_favorito, plantilla1.equipo_favorito)
    cartas.append(bronce)

    oro = Oro(choice(nombres_cartas), choice(equipos), choice(paises))
    oro.calcular_quimica(plantilla1.pais_favorito, plantilla1.equipo_favorito)
    cartas.append(oro)

    especial = Especial(choice(nombres_cartas), choice(equipos), choice(paises), choices(habilidades_especiales, k=randint(1, 3)))
    especial.calcular_quimica(plantilla1.pais_favorito, plantilla1.equipo_favorito)
    cartas.append(especial)

shuffle(cartas)

plantilla1.plantel = cartas[0:11]
plantilla2.plantel = cartas[11:22]

print(plantilla1)
print(plantilla2)



