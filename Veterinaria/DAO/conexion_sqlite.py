import sqlite3
from Veterinaria.Entidades.Entidades import PracticaMedica
class Conexion():
    def __init__(self):
        self.conexion = sqlite3.connect('Veterinaria/DAO/BDProyectoPy.db')


        self.Entidades= PracticaMedica()

    def mostrar_PracticaMedica(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT IdPracticaMe_pra, decripcion_pra FROM PracticaMedica")
        registros = cursor.fetchall()
        print(registros)  # Agrega esta línea para depurar
        return registros
    
    def buscar_practicaMedica(self, Entidades.Id,Entidades.Descripcion):
         cursor = self.conexion.cursor()
         cursor.execute("SELECT IdPracticaMe_pra, decripcion_pra FROM PracticaMedica where IdPracticaMe_pra ="+Entidades.Id+" or "+Entidades.Descripcion+" ")
         registros = cursor.fetchall()
         print(registros)  # Agrega esta línea para depurar
         return registros
    