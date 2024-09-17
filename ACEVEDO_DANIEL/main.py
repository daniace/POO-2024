from Hierba import Hierba
from Fuego import Fuego
from Agua import Agua
from Entrenador import Entrenador
import random


nombres = [
    "Mango",
    "Palta",
    "Azul",
    "Rojito",
    "Enano",
    "Remolacha",
    "Aceituna",
    "Burro",
    "Papiro",
    "Muzzarella",
    "Jamon",
    "Lentejuela",
]
tipos_pokemones = [Hierba, Fuego, Agua]

entrenador = Entrenador(
    "Daniel", random.randint(1, 100), random.choice(tipos_pokemones)
)

# Se van a repetir nombres y tipos en la pokedex y las capturas porque hay pocos nombres y tipos

for i in range(1, 10):
    pokemon = random.choice(tipos_pokemones)(random.choice(nombres))

    entrenador.atrapar_pokemon(pokemon)

entrenador.imprimir_entrenador()
