import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Mi Aplicación Qt6")
window.resize(400, 300)
window.show()
sys.exit(app.exec())

