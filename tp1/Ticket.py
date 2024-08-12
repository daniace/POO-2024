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
