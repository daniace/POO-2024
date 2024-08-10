class Tienda:
    def __init__(self):
        self.listado_cursos = []

    def agregar_curso(self, curso):
        self.listado_cursos.append(curso)

    def imprimir_curso(self):
        for curso in self.listado_cursos:
            curso.imprimo_curso()
