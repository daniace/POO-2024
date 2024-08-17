import random

def numeros_aleatorios():
    num1 = 0
    num2 = 0
    while num1 == num2:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    return num1, num2

jugar = True
perdidas = 0
ganadas = 0
while jugar:
    num1, num2 = numeros_aleatorios()
    seleccion = int(input("Elige numero 1 o 2: "))
    match seleccion:
        case 1: 
            if num1 > num2:
                print(f"Has ganado. {num1} > {num2}")
                ganadas += 1
            else:
                print(f"Has perdido. {num1} < {num2}")
                perdidas += 1
    
        case 2: 
            if num2 > num1:
                print(f"Has ganado. {num2} > {num1}")
                ganadas += 1
            else:
                print(f"Has perdido. {num2} < {num1}")
                perdidas += 1
    jugar = input("Desea seguir jugando? (s/n) ") == "s"
print(f"Juegos ganados: {ganadas}")
print(f"Juegos perdidos: {perdidas}")


