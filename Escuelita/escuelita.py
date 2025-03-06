"""
Realizar un programa en Python para guardar, actualizar, borrar y mostrar los alumnos de una escuelita.
"""

# Primer paso importar la libreria sqlite3 para manejar bdd en sql 
import sqlite3

# Creamos la conexion para abrir la bdd
conn = sqlite3.connect("escuelita.db")
cursor = conn.cursor() # Cursor para ejecutar SQL

# Crear una tabla en SQLite
cursor.execute('''
               CREATE TABLE IF NOT EXISTS alumnos(
                matricula INTEGER PRIMARY KEY AUTOINCREMENT
                ,nombre VARCHAR(100) NOT NULL
                ,apellido_paterno VARCHAR(100) NOT NULL
                ,apellido_materno VARCHAR(100)
                ,fecha_nacimiento DATE
                ,sexo CHAR);
                ''')


cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS materias(
                clave CHAR(5) PRIMARY KEY
                ,nombre VARCHAR(100)
                ,creditos	 INT DEFAULT 10); ''')


cursor.execute(''' 
                CREATE TABLE calificaciones(
                alumno INT
                ,materia CHAR(5)
                ,calificacion FLOAT 
                ,fecha DATE  
                ,PRIMARY KEY (alumno, materia)
                ,FOREIGN KEY (alumno) REFERENCES alumnos(matricula)
                ,FOREIGN KEY (materia) REFERENCES materias(clave));''')








