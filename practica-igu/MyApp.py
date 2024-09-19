import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

# Subclase QMainWindow para customizar la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        self.button = QPushButton("Apretame!")
        self.button.clicked.connect(self.el_boton_fue_clickeado)
        self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(600, 450))

        # Ponemos el widget central de la ventana
        self.setCentralWidget(self.button)

    def el_boton_fue_clickeado(self):
        self.button.setText("Ya me apretaste!")
        self.button.setEnabled(False)

        # Tambien cambia el titulo de la ventana
        self.setWindowTitle("Se me jijean los jijonazos")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()