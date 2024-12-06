import sys



from PyQt6.QtWidgets import QMainWindow, QApplication,QHeaderView
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6.uic import loadUi
from PyQt6 import QtCore
from PyQt6 import QtWidgets

from Veterinaria.DAO.conexion_sqlite import Conexion

from Veterinaria.Entidades.Entidades import PracticaMedica

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('Veterinaria/Vistas/Vista.ui', self)

 # Conectar los botones con las funciones
        self.btnFormInicio.clicked.connect(self.mostrar_inicio)
        self.btnFormAgregarPractica.clicked.connect(self.mostrar_agregar_practica)
        self.btnFormVerPractica.clicked.connect(self.mostrar_ver_practica)
        self.btnBuscarIdpractica.clicked.connect(self.BuscarPracticaMedica)

        # Navegar directamente a la página de inicio
        self.stackedWidget.setCurrentWidget(self.page_inicio)
        # Inicialmente, colapsar la barra lateral
        self.frame_lateral.setMinimumWidth(0)
        self.frame_lateral.setMaximumWidth(0)
        self.btn_menu.clicked.connect(self.moverMenu)

        self.base_datos= Conexion()
      

    def mostrar_inicio(self):
     self.stackedWidget.setCurrentWidget(self.page_inicio)  # Cambia al widget de inicio

    def mostrar_agregar_practica(self):
        self.stackedWidget.setCurrentWidget(self.page_agregarPractica)  # Cambia a la página de agregar práctica

    def mostrar_ver_practica(self):
        self.stackedWidget.setCurrentWidget(self.page_verPractica)   

        self.cargar_practicas()  # Llamar a la función para cargar la tabla con los datos de la base de datos




    def moverMenu(self):
   
        width = self.frame_lateral.width() # Obtener el ancho actual del frame_lateral

        normal = 0  # Acolapsada
        extender = 250  # expandida

        if self.frame_lateral.isVisible():  # Si la barra lateral está visible, la colapsamos
            self.animacion = QPropertyAnimation(self.frame_lateral, b"minimumWidth")
            self.animacion.setDuration(250)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(normal)  # Colapsa a 0
            self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutCubic)
            self.animacion.start()

            # Después de la animación, hacer la barra lateral invisible
            self.animacion.finished.connect(lambda: self.frame_lateral.setVisible(False))

        else:  # Si la barra lateral no está visible, la expandimos
            self.frame_lateral.setVisible(True)  # Hacer visible la barra lateral
            self.animacion = QPropertyAnimation(self.frame_lateral, b"minimumWidth")
            self.animacion.setDuration(250)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)  
            self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutCubic)
            self.animacion.start()

    def cargar_practicas(self):
        

        datos=self.base_datos.mostrar_PracticaMedica()
        i=len(datos)
        self.grdPractica.setRowCount(i)
        tablerow=0
        for row in datos:
            self.id=row[0]
            self.grdPractica.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.grdPractica.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            tablerow +=1
           
    def BuscarPracticaMedica(self):
        Practica= PracticaMedica()
        textoBuscar=self.txtIdPracticaFiltro.text()
        Practica.setId(textoBuscar)
        print("------------------------*********************************************averr que hay adentr de onj")
        print(Practica.getId())
    

        datos=self.base_datos.buscar_practicaMedica(Practica)
        i=len(datos)

        self.grdPractica.setHorizontalHeaderLabels(['ID', 'Descripción'])
        self.grdPractica.setRowCount(i)
        tablerow=0
        for row in datos:
            self.id=row[0]
            self.grdPractica.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.grdPractica.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))

            tablerow +=1
            self.grdPractica.viewport().update()  # Forzar actualización del widget




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())