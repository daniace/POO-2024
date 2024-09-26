from Docente import Docente
from NoDocente import NoDocente
from Reloj import Reloj
import random

categorias_docentes = ["Simple", "Semiexclusivo", "Exclusiva"]
jornadas_no_docentes = ["Completa", "Reducida"]
tipo_personal = ["Docente", "NoDocente"]
reloj = Reloj()

for i in range(1,11):
    match random.choice(tipo_personal):
        case "Docente":
            docente = Docente(f"Docente {i}", f"Apellido {i}", random.randint(1,10), f"Sector {i}", random.choice(categorias_docentes))
            reloj.agregar_personal(docente)
        case "NoDocente":
            noDocente = NoDocente(f"NoDocente {i}", f"Apellido {i}", random.randint(1,10), f"Sector {i}", random.choice(jornadas_no_docentes))
            reloj.agregar_personal(noDocente)

reloj.imprimir_informe()

