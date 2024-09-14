import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from custom_dialog import CustomDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi App")

        button = QPushButton("Está seguro que quiere dar de baja al usuario?")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        if dlg.exec():
            print("OK")
        else:
            print("CANCEL")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()