peso = float(input('Peso: '))
estatura = float(input('Estatura: '))


def imc(peso, estatura):
    estatura_final = estatura * estatura
    return peso / estatura_final


print(f"El IMC es de: ", round(imc(peso, estatura)))
