import sys
import shutil
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt


class FileMoverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Mover Archivos')
        self.setGeometry(100, 100, 400, 200)

        # Crear layout principal
        layout = QVBoxLayout()

        # Etiquetas para mostrar el archivo seleccionado y la ubicación de destino
        self.file_label = QLabel('Archivo seleccionado: Ninguno', self)
        self.destination_label = QLabel('Ubicación de destino: Ninguna', self)

        # Botón para seleccionar archivo
        self.select_file_button = QPushButton('Seleccionar Archivo', self)
        self.select_file_button.clicked.connect(self.select_file)

        # Botón para seleccionar la ubicación de destino
        self.select_destination_button = QPushButton('Seleccionar Destino', self)
        self.select_destination_button.clicked.connect(self.select_destination)

        # Botón para mover el archivo
        self.move_file_button = QPushButton('Mover Archivo', self)
        self.move_file_button.clicked.connect(self.move_file)

        # Añadir widgets al layout
        layout.addWidget(self.file_label)
        layout.addWidget(self.select_file_button)
        layout.addWidget(self.destination_label)
        layout.addWidget(self.select_destination_button)
        layout.addWidget(self.move_file_button)

        # Configurar layout en la ventana
        self.setLayout(layout)

        # Variables para almacenar las rutas
        self.file_path = None
        self.destination_path = None

    def select_file(self):
        # Abrir el diálogo para seleccionar un archivo
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            # Obtener la ruta del archivo seleccionado
            self.file_path = file_dialog.selectedFiles()[0]
            self.file_label.setText(f'Archivo seleccionado: {self.file_path}')

    def select_destination(self):
        # Abrir el diálogo para seleccionar la carpeta de destino
        destination_dialog = QFileDialog(self)
        destination_dialog.setFileMode(QFileDialog.FileMode.Directory)
        if destination_dialog.exec():
            # Obtener la ruta de la carpeta de destino
            self.destination_path = destination_dialog.selectedFiles()[0]
            self.destination_label.setText(f'Ubicación de destino: {self.destination_path}')

    def move_file(self):
        # Comprobar si el archivo y la ubicación de destino han sido seleccionados
        if not self.file_path or not self.destination_path:
            QMessageBox.warning(self, 'Advertencia', 'Seleccione un archivo y una ubicación de destino.')
            return

        try:
            # Copiar el archivo a la ubicación de destino
            shutil.copy(self.file_path, self.destination_path)
            QMessageBox.information(self, 'Éxito', 'Archivo movido exitosamente.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al mover el archivo: {str(e)}')


def main():
    app = QApplication(sys.argv)
    window = FileMoverApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
