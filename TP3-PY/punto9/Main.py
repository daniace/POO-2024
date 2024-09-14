from Claro import Claro
from Movistar import Movistar
from Personal import Personal


def main():
    movistar = Movistar("Movistar", 10, 20, 30)
    claro = Claro("Claro", 10, 20, 30)
    personal = Personal("Personal", 10, 20, 30)
    print(movistar.calcular())
    print(claro.calcular())
    print(personal.calcular())


main()
