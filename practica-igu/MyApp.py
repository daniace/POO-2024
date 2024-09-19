from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Solo se necesita una instancia de QApplication por aplicación
# sys.argv es una lista de argumentos de la línea de comandos
# Si no sabes como usar sys.argv, QApplication([]) también funciona
app = QApplication(sys.argv)

# Creamos una instancia de QWidget, que va a ser nuestra ventana
window = QMainWindow()
window.show() # IMPORTANTE, las ventanas están ocultas por defecto

# Ejecutamos el bucle de eventos de la aplicación
app.exec()

# Tu aplicación no va a cerrarse hasta que el bucle de eventos termine