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

        self.el_boton_esta_chequeado = False

        self.setWindowTitle("Mi aplicación")

        button = QPushButton("Apretame!")
        button.setCheckable(True)
        button.clicked.connect(self.el_boton_fue_alternado)
        button.setChecked(self.el_boton_esta_chequeado)

        self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(600, 450))

        # Ponemos el widget central de la ventana
        self.setCentralWidget(button)

    def el_boton_fue_alternado(self, checked):
        self.el_boton_esta_chequeado = checked

        print(self.el_boton_esta_chequeado)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()