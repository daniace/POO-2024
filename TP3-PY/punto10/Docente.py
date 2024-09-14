from Personal import Personal


class Docente(Personal):
    def __init__(self, nombre, apellido, antiguedad, sector, categoria):
        super().__init__(nombre, apellido, antiguedad, sector)
        categorias = ["Simple", "Semiexclusivo", "Exclusivo"]
        self._categoria = categorias[categoria]
