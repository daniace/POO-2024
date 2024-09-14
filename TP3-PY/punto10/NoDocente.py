from Personal import Personal


class NoDocente(Personal):
    def __init__(self, nombre, apellido, antiguedad, sector, jornada):
        super().__init__(nombre, apellido, antiguedad, sector)
        self._jornada = ["Completa", "Reducida"]
