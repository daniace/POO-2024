import random

marca = True


def mayor_o_menor():
    while marca:
        valor1 = random.randint(1, 100)
        valor2 = random.randint(1, 100)

        if valor1 == valor2:
            pass
        elif valor1 > valor2:
            print("Gano el valor ", valor1)
        else:
            print("Perdio el valor ", valor1)
