import sys
from random import choice
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

window_titles = [
    "Mi aplicación",
    "Sigue siendo mi aplicación",
    "No me canso de decir que es mi aplicación",
    "Que paso, ya no es mi aplicación?",
    "Ya no es mi aplicación",
    "Es tu aplicación ahora",
    "Es de quien la quiera",
    "No es de nadie",
    "Es de todos",
    "Es de la humanidad",
    "Algo malo ocurrió",
]

# Subclase QMainWindow para customizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_veces_clickeada = 0

        self.setWindowTitle("Mi aplicación")

        self.button = QPushButton("Apretame!")
        self.button.clicked.connect(self.el_boton_fue_clickeado)

        self.windowTitleChanged.connect(
            self.el_titulo_de_la_ventana_cambio
        )

        self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(600, 450))

        # Ponemos el widget central de la ventana
        self.setCentralWidget(self.button)

    def el_boton_fue_clickeado(self):
        print("Clickeado!")
        nuevo_titulo = choice(window_titles)
        print("Poniendo el titulo: %s" % nuevo_titulo)
        self.setWindowTitle(nuevo_titulo)

    def el_titulo_de_la_ventana_cambio(self, titulo):
        print("El titulo de la ventana cambio a: %s" % titulo)

        if titulo == "Algo malo ocurrió":
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()