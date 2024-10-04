from CuentaBancaria import CuentaBancaria
from CuentaBilleteraVirtual import CuentaBilleteraVirtual
from Impuesto import Impuesto
import random

cuenta_bancaria = CuentaBancaria(
    random.randint(1000, 10000),
    "Wolfgang Amadeus Mozart",
    random.randint(1000, 10000),
    random.randint(100000, 10000000),
)
cuenta_virtual = CuentaBilleteraVirtual(
    random.randint(1000, 10000),
    "Peter Parker",
    random.randint(1000, 10000),
    random.randint(100000, 10000000),
)

cuenta_bancaria.imprimir()
cuenta_virtual.imprimir()

nombre_impuesto = [
    "Impueso a las ganancias",
    "Impuesto a los bienes personales",
    "Impuesto a la riqueza",
    "Impuesto a la renta financiera",
    "Impuesto a la herencia",
    "Impuesto a la transferencia de inmuebles",
    "Impuesto a la transferencia de automotores",
    "Impuesto a la transferencia de bienes personales",
    "Impuesto a la transferencia de bienes muebles y servicios",
    "Impuesto a la transferencia de combustibles",
    "Impuesto a la transferencia de energia electrica",
    "Impuesto a la transferencia de gas natural",
    "Impuesto a la transferencia de agua potable",
    "Impuesto a la transferencia de telefonía",
    "Impuesto a la transferencia de internet",
    "Impuesto a la transferencia de televisión por cable",
    "Impuesto a la transferencia de servicios de comunicaciones",
    "Impuesto a la transferencia de servicios de transporte",
    "Impuesto a la transferencia de servicios de turismo",
    "Impuesto a la transferencia de servicios de hoteleria",
    "Impuesto a la transferencia de servicios de gastronomia",
    "Impuesto al valor agregado",
    "Impuesto a las transacciones financieras",
    "Impuesto a la transferencia de servicios de salud",
    "Impuesto a la transferencia de servicios de educación",
    "Impuesto a la transferencia de servicios de seguridad",
    "Impuesto a la transferencia de servicios de justicia",
]

lista_impuestos = []
for i in range(1, 21):
    lista_impuestos.append(
        Impuesto(
            random.choice(nombre_impuesto),
            random.randint(500, 1500),
            random.randint(1, 12),
        )
    )

random.shuffle(lista_impuestos)

cuotas = (1, 3, 6, 12)

tipo_pago = ["debito", "credito"]
tipo_cuenta = ["cuenta_bancaria", "cuenta_virtual"]
tipo_cuentita = [cuenta_bancaria, cuenta_virtual]

"""
for impuesto in impuestos:
    match random.choice(tipo_cuenta):
        case "cuenta_bancaria":
            print("---CUENTA BANCARIA---\n")
            print("---Impuesto a pagar---\n")
            impuesto.imprimir()
            print("--------------------")
            match random.choice(tipo_pago):
                case "debito":
                    print("---Pago Debito---\n")
                    if cuenta_bancaria.get_saldo() > impuesto.get_monto():
                        cuenta_bancaria.pagar_debito(impuesto.get_monto())
                        impuesto.validar_pago(
                            impuesto.get_monto(), impuesto.get_periodo()
                        )
                        print("--------------------")
                    else:
                        print(f"Saldo insuficiente ${round(cuenta_bancaria.get_saldo(),2)}\n")
                case "credito":
                    if cuenta_bancaria.get_saldo() > impuesto.get_monto():
                        print("---Pago Credito---\n")
                        cuenta_bancaria.pagar_credito(
                            impuesto.get_monto(), random.choice(cuotas)
                        )
                        impuesto.validar_pago(
                            impuesto.get_monto(), impuesto.get_periodo()
                        )
                        print("--------------------")
                    else:
                        print(f"Saldo insuficiente ${round(cuenta_bancaria.get_saldo(),2)}\n")
        case "cuenta_virtual":
            print("---BILLETERA VIRUTAL---\n")
            print("---Impuesto a pagar---\n")
            impuesto.imprimir()
            print("--------------------")
            match random.choice(tipo_pago):
                case "debito":
                    if cuenta_virtual.get_saldo() > impuesto.get_monto():
                        print("---Pago Debito---\n")
                        cuenta_virtual.pagar_debito(impuesto.get_monto())
                        impuesto.validar_pago(
                            impuesto.get_monto(), impuesto.get_periodo()
                        )
                        print("--------------------")
                    else:
                        print(f"Saldo insuficiente ${round(cuenta_virtual.get_saldo(),2)}\n")
                case "credito":
                    if cuenta_virtual.get_saldo() > impuesto.get_monto():
                        print("---Pago Credito---\n")
                        cuenta_virtual.pagar_credito(
                            impuesto.get_monto(), random.choice(cuotas)
                        )
                        impuesto.validar_pago(
                            impuesto.get_monto(), impuesto.get_periodo()
                        )
                        print("--------------------")
                    else:
                        print(f"Saldo insuficiente ${round(cuenta_virtual.get_saldo(),2)}\n")
"""


def pagar_nazi(cuenta, pago, impuesto, cuotas):
    match pago:
        case "debito":
            impuesto.validar_pago(cuenta.pagar_debito(impuesto.get_monto()), random.randint(1,12))
        case "credito":
            impuesto.validar_pago(cuenta.pagar_credito(impuesto.get_monto(), cuotas), random.randint(1,12))

for impuesto in lista_impuestos:
    pagar_nazi(random.choice(tipo_cuentita), random.choice(tipo_pago), impuesto, random.choice(cuotas))


print("---IMPUESTOS PAGADOS---\n")
for impuesto in lista_impuestos:
    if impuesto.get_cobrado():
        impuesto.imprimir()
        print(f"Cobrado: {impuesto.get_cobrado()}")
        print(f"Numero de comprobante: {impuesto.get_numero_comprobante()}\n")
