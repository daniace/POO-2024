from Ticket import Ticket
from Medicamento import Medicamento

pastilla = Medicamento("actron", 600, 4500)
pastilla2 = Medicamento("rivotril", 25, 700)
pastilla3 = Medicamento("paracetamol", 500, 3200)

factura = Ticket(132, "6/8/2024")
factura.AggProd(pastilla)
factura.AggProd(pastilla2)
factura.AggProd(pastilla3)
factura.impLista()
