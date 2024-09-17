import random


class Entrenador:
    def __init__(self, nombre, nivel, pokemon):
        self.__nombre = nombre
        self.__nivel_entrenador = nivel
        self.__pokemon_principal = pokemon
        self.__pokedex = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nivel_entrenador(self):
        return self.__nivel_entrenador

    @property
    def pokemon_principal(self):
        return self.__pokemon_principal

    @property
    def pokedex(self):
        return self.__pokedex

    @nivel_entrenador.setter
    def nivel_entrenador(self, nivel):
        self.__nivel_entrenador = nivel

    @pokemon_principal.setter
    def pokemon_principal(self, pokemon):
        self.__pokemon_principal = pokemon

    @pokedex.setter
    def pokedex(self, pokemon):
        self.__pokedex.append(pokemon)

    def atrapar_pokemon(self, pokemon):
        lista = [True, False]
        captura = random.choice(lista)
        if self.nivel_entrenador > pokemon.salvajismo:
            for i in range(random.randint(1,3)):
                pokemon.vida -= pokemon.vida * 0.1
                if pokemon.vida > 0 and captura:
                    print(
                        f"{pokemon._nombre} tipo {pokemon.__class__.__name__} capturado!\n"
                    )
                    self.pokedex = pokemon
                elif pokemon.vida <= 0:
                    print(f"{pokemon.vida} murio")

            print(f"{pokemon._nombre} se escapo y no logro ser capturado\n")

    def imprimir_pokedex(self):
        contador = 1
        for pokemon in self.pokedex:
            print(f"Pokemon {contador}: {pokemon.imprimir_pokemon()}")
            contador += 1

    def imprimir_entrenador(self):
        print("===============================================================")
        print(f"Entrenador: {self.nombre} \nNivel: {self.nivel_entrenador} \n")
        print("==================POKEDEX===================")
        print(f"Pokedex: {self.imprimir_pokedex()} \n")
