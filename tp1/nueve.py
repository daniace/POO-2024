import random

num = input("Ingresa un numero: ")

numerito = random.randint(1, 10)

if num == numerito:
    print("El numero", num, "es igual a", numerito)
else:
    print("El numero", num, "es distino a", numerito)

if int(num) < numerito:
    print("El numero", num, "es menor a a", numerito)
else:
    print("El numero", num, "es mayor a a", numerito)

if int(num) <= numerito:
    print("El numero", num, "es menor o igual a", numerito)
else:
    print("El numero", num, "es mayor o igual a", numerito)
