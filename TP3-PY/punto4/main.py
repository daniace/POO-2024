from Mago import Mago
from Guerrero import Guerrero
import random


mago = Mago()
guerrero = Guerrero()

print("-------------PELEA-------------")
mago.imprimir()
guerrero.imprimir()
print("-------------------------------")

primer_ataque = [ "mago", "guerrero"]

match random.choice(primer_ataque):
    case "guerrero":
        while mago.get_vida() and guerrero.get_vida() > 0:
            mago.defender(guerrero.atacar())
            if mago.get_vida() < 0:
                break
            guerrero.defender(mago.atacar())
            if guerrero.get_vida() < 0:
                break
    case "mago":
        while guerrero.get_vida() and mago.get_vida() > 0:
            guerrero.defender(mago.atacar())
            if guerrero.get_vida() < 0:
                break
            mago.defender(mago.atacar())
            if mago.get_vida() < 0:
                break
print("-------------------------------")