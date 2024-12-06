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
    