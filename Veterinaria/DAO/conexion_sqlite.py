import sqlite3
from Veterinaria.Entidades.Entidades import PracticaMedica
class Conexion():
    def __init__(self):
        self.conexion = sqlite3.connect('Veterinaria/DAO/BDProyectoPy.db')


   

    def mostrar_PracticaMedica(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT IdPracticaMe_pra, decripcion_pra FROM PracticaMedica")
        registros = cursor.fetchall()
        print(registros)  # Agrega esta línea para depurar
        return registros
    
    def buscar_practicaMedica(self, Practica):
    
         print("llego------------------------") 
         print(Practica.getId()) 
         cursor = self.conexion.cursor()
         consulta=()
         cursor.execute("SELECT IdPracticaMe_pra, decripcion_pra FROM PracticaMedica where IdPracticaMe_pra ="+Practica.getId()+"")
         registros = cursor.fetchall()
     
         print(registros)  # Agrega esta línea para depurar
         return registros
    
    def Agregar_MascotasBD(self, Mascota):
            cursor = self.conexion.cursor()
            cursor.execute("INSERT INTO Mascotas (DNIporietario_ma, raza_ma, Genero_ma, Peso_ma, FechaNacimiento_ma, Nombre_ma, Especie_ma, Observacion_ma) VALUES('"+Mascota.getDNIporietario_ma()+"', '"+ Mascota.getRaza_ma()+"', '"+Mascota.getGenero_ma()+"', "+Mascota.getPeso_ma()+", '"+Mascota.getFechaNacimiento_ma()+"', '"+Mascota.getNombre_ma()+"', '"+Mascota.getEspecie_ma()+"', '"+Mascota.getObservacion_ma()+"');")
            self.conexion.commit()
            print("Se agrego a ka bd la mascota")  # Agrega esta línea para depurar
          

    