
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWidgets

# Aquí importas la clase generada del archivo .ui
from Presentacion import Ui_MainWindow  # Asegúrate de que el nombre sea correcto

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz gráfica en este QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()  # Crea una instancia de tu ventana principal
    mainWindow.show()  # Muestra la ventana
    sys.exit(app.exec())  # Ejecuta el ciclo de eventos


