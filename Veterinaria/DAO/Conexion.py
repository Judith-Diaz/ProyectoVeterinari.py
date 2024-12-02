import sqlite3;
class Conexion:
    def conectar(self):
      conexion = sqlite3.connect('DAO/BDProyectoPy.db')
      return conexion
    
def cargar_materias():
    try:
        cone = Conexion()
        conexion = cone.conectar()
        cur = conexion.cursor()
        sql = 'SELECT * FROM PracticaMedica;'
        cur.execute(sql)
        resultado = cur.fetchall()
        print(resultado)
        resultado2 = []
        for r in resultado:
            resultado2.append({'IdPracticaMe_pra': r[0], 'decripcion_pra': r[1]})
        return resultado2
    finally:
        conexion.close()

print(cargar_materias())