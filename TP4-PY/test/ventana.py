from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MI VENTANITA UWU")
        button = QPushButton("Apretame")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
