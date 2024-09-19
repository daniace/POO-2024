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

        boton = QPushButton("Apretame!")

        # Ponemos el widget central de la ventana
        self.setCentralWidget(boton)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()