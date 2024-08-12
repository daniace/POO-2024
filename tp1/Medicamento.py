class Medicamento:
    def __init__(self, nombre, dosis, precio):
        self.nombre = nombre
        self.dosis = dosis
        self.precio = precio

    def impMed(self):
        print(f"Nombre: {self.nombre} " + f"Dosis: {self.dosis} " + f"Precio: {self.precio}\n")