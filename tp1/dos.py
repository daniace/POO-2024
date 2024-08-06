class Ticket:
    def __init__(self, nventa, fecha):
        self.nventa = nventa
        self.fecha = fecha
        self.total = 0
        self.listaMed = []

    def AggProd(self, medicamento):
        self.listaMed.append(medicamento)

    def impLista(self):
        for medicamento in self.listaMed:
            medicamento.impMed()
            self.total += medicamento.precio
        print(f"Total: {self.total}")


class Medicamento:
    def __init__(self, nombre, dosis, precio):
        self.nombre = nombre
        self.dosis = dosis
        self.precio = precio

    def impMed(self):
        print(f"Nombre: {self.nombre} " + f"Dosis: {self.dosis} " + f"Precio: {self.precio}\n")


pastilla = Medicamento("actron", 600, 4500)
pastilla2 = Medicamento("rivotril", 25, 700)
pastilla3 = Medicamento("paracetamol", 500, 3200)

factura = Ticket(132, "6/8/2024")
factura.AggProd(pastilla)
factura.AggProd(pastilla2)
factura.AggProd(pastilla3)
factura.impLista()
