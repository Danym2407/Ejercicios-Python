import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('vuelos.db')
cursor = conn.cursor()

# Agregar la columna 'ruta' a la tabla 'Vuelos'
cursor.execute("ALTER TABLE Vuelos ADD COLUMN ruta TEXT NOT NULL")
conn.commit()

# Verificar si la columna se agregó correctamente
cursor.execute("PRAGMA table_info(Vuelos)")
columnas = cursor.fetchall()
print("Columnas en la tabla Vuelos:", columnas)

# Cerrar la conexión
conn.close()