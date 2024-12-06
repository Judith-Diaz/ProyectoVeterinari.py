import sqlite3
from Veterinaria.Entidades.Entidades import PracticaMedica
class Conexion():
    def __init__(self):
        self.conexion = sqlite3.connect('Veterinaria/DAO/BDProyectoPy.db')


        self.Practica= PracticaMedica()

    def mostrar_PracticaMedica(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT IdPracticaMe_pra, decripcion_pra FROM PracticaMedica")
        registros = cursor.fetchall()
        print(registros)  # Agrega esta línea para depurar
        return registros
    
    def buscar_practicaMedica(self, Practica):
         cursor = self.conexion.cursor()
         cursor.execute("SELECT IdPracticaMe_pra, decripcion_pra FROM PracticaMedica where IdPracticaMe_pra ="+Practica.getId+" or "+Practica.getDescripcion+" ")
         registros = cursor.fetchall()
         print(registros)  # Agrega esta línea para depurar
         return registros
    