# Desarrollar dos ejemplos del uso de un dialog

# Un cuadro de diálogo que indique el siguiente mensaje “Está seguro que quiere
# dar de baja al usuario”, con los botones de aceptar y cancelar.

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Punto 1')
        self.setGeometry(100, 100, 300, 300)
        self.boton = QPushButton('Apretame', self)
        self.boton.move(100, 100)
        self.boton.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle('Dialog')
        dialog.setFixedSize(300, 100)
        dialog.setModal(True)

        respuesta = QMessageBox.question(self, 'Mensaje', 'Está seguro que quiere dar de baja al usuario', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        if respuesta == QMessageBox.StandardButton.Yes:
            print('Usuario dado de baja')
        else:
            print('Operación cancelada')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




