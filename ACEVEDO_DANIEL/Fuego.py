from Pokemon import Pokemon
import random


class Fuego(Pokemon):
    def __init__(self, nombre):
        super().__init__(nombre)

    def atacar(self, objetivo):
        probabilidad_critico = random.randint(0.0, 1.0)
        if (objetivo.__class__.__name__ == "Hierba" and probabilidad_critico >= 0.7):
            objetivo.vida -= self.ataque * 0.5
            print(f"{self.nombre} ataco a {objetivo.nombre} con un daño critico de {self.ataque * 0.5}")
            print(f"{objetivo.nomnbre} le queda {objetivo.vida} de vida restante")
        else:
            if objetivo.defensa > self.ataque:
                print(f"{objetivo.nombre} se defendio del ataque de {self.ataque} puntos de daño")
            else:
                objetivo.vida -= self.ataque
                print(f"{self.nombre} ataco a {objetivo.nombre} con un daño de {self.ataque}")
                print(f"{objetivo.nomnbre} le queda {objetivo.vida} de vida restante")

        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} murio")


    def defender(self, atacante):
        if self.defensa > atacante.ataque:
            print(f"{self.nombre} se defendio del ataque de {atacante.ataque} puntos de daño")
        else:
            self.vida -= atacante.ataque
            print(f"{self.nombre} recibio el ataque de {atacante.nombre} con {atacante.ataque} daño")
            print(f"Vida restante: {self.vida}")

        if self.vida <= 0:
            print(f"{self.nombre} murio")