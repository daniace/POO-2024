import random

class Impuesto:
    def __init__(self, nombre, monto, periodo):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__cobrado = False
        self.__numero_comprobante = 0

    def get_monto(self):
        return self.__monto
    
    def get_cobrado(self):
        return self.__cobrado
    
    def get_periodo(self):
        return self.__periodo
    
    def get_numero_comprobante(self):
        return self.__numero_comprobante

    def validar_pago(self, monto, periodo):
        numero_comprobante = random.randint(1000, 9999)
        if monto == self.__monto and periodo == self.__periodo:
            print("Pago realizado!")
            print(f" - N°Comprobante: {numero_comprobante}\n")
            self.__numero_comprobante = numero_comprobante
            self.__cobrado = True
        else:
            print("Pago NO realizado.")
            print("Verifique")
            print(f" - Monto: ${monto}")
            print(f" - Periodo/Mes: {periodo}\n")
            self.__cobrado = False

    def imprimir(self):
        print(f"Impuesto: {self.__nombre}")
        print(f"Monto: ${self.__monto}")
        print(f"Periodo/Mes: {self.__periodo}\n")


if __name__ == "__main__":
    lista_impuestos = []
    for i in range (1,21):
        impuesto = Impuesto(f"Impuesto {i}", random.randint(1000, 5000), random.randint(1, 12))
        lista_impuestos.append(impuesto)
    
    random.shuffle(lista_impuestos)

    print("---Impuesto a pagar---\n")
    lista_impuestos[0].imprimir()
    print("----------------------")

    print("----Pago realizado----\n")
    lista_impuestos[0].validar_pago(lista_impuestos[0].get_monto(), lista_impuestos[0].get_periodo()) # Valido
    lista_impuestos[0].imprimir()
    print("----------------------")
    
    print("----Pago Rechazado----\n")
    lista_impuestos[0].validar_pago(random.randint(1000,5000), random.randint(1,12)) # No valido pero muy poco probable que sea valido
    lista_impuestos[0].imprimir()
    print("----------------------")