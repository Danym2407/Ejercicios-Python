import sqlite3
import networkx as nx
import matplotlib.pyplot as plt
import itertools
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Definir nodos
nodos = {
    "La Comarca": {"país": "Tierra Media", "aeropuerto": "Bilbo Bolsón", "tipo": "Ordinaria"},
    "Rivendel": {"país": "Tierra Media", "aeropuerto": "Altos Elfos", "tipo": "Importante"},
    "Rohan": {"país": "Tierra Media", "aeropuerto": "Caballo Verde", "tipo": "Ordinaria"},
    "Reino del Bosque": {"país": "Tierra Media", "aeropuerto": "Elfos Silvanos", "tipo": "Ordinaria"},
    "Erebor": {"país": "Tierra Media", "aeropuerto": "Durin", "tipo": "Ordinaria"},
    "Gondor": {"país": "Tierra Media", "aeropuerto": "Isildur", "tipo": "Capital"},
    "Moria": {"país": "Tierra Media", "aeropuerto": "Khazad Dum", "tipo": "Ordinaria"},
    "Isengard": {"país": "Tierra Media", "aeropuerto": "Mago Blanco", "tipo": "Ordinaria"},
    "Mordor": {"país": "Tierra Media", "aeropuerto": "Ojo de Sauron", "tipo": "Importante"},
    "Narnia": {"país": "Narnia", "aeropuerto": "León Real", "tipo": "Capital"},
    "Telmar": {"país": "Narnia", "aeropuerto": "Príncipe Caspian", "tipo": "Importante"},
    "Charn": {"país": "Narnia", "aeropuerto": "Bruja Blanca", "tipo": "Importante"},
    "Ciudad Esmeralda": {"país": "Oz", "aeropuerto": "Mago de Oz", "tipo": "Capital"},
    "Winkie": {"país": "Oz", "aeropuerto": "Bruja del Oeste", "tipo": "Importante"},
    "Munchkin": {"país": "Oz", "aeropuerto": "Dorita", "tipo": "Ordinaria"},
}

# Definir aristas
aristas = [
    {"origen": "La Comarca", "destino": "Rivendel", "tipo": "N", "distancia": 500.00, "tiempo": 1.5, "costo": 1550.00},
    {"origen": "Rivendel", "destino": "La Comarca", "tipo": "N", "distancia": 500.00, "tiempo": 1.5, "costo": 1850.00},
    {"origen": "Rivendel", "destino": "Reino del Bosque", "tipo": "N", "distancia": 950.00, "tiempo": 2.4, "costo": 2400.00},
    {"origen": "Rivendel", "destino": "Rohan", "tipo": "N", "distancia": 550.00, "tiempo": 1.6, "costo": 1975.00},
    {"origen": "Rivendel", "destino": "Telmar", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 3750.00},
    {"origen": "Rohan", "destino": "Rivendel", "tipo": "N", "distancia": 550.00, "tiempo": 1.6, "costo": 1675.00},
    {"origen": "Rohan", "destino": "Isengard", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1300.00},
    {"origen": "Rohan", "destino": "Gondor", "tipo": "N", "distancia": 600.00, "tiempo": 1.7, "costo": 1550.00},
    {"origen": "Gondor", "destino": "Rohan", "tipo": "N", "distancia": 600.00, "tiempo": 1.7, "costo": 2350.00},
    {"origen": "Gondor", "destino": "Erebor", "tipo": "N", "distancia": 1250.00, "tiempo": 3.0, "costo": 4225.00},
    {"origen": "Gondor", "destino": "Mordor", "tipo": "N", "distancia": 450.00, "tiempo": 3.4, "costo": 3125.00},
    {"origen": "Gondor", "destino": "Narnia", "tipo": "I", "distancia": 550.00, "tiempo": 4.1, "costo": 1975.00},
    {"origen": "Gondor", "destino": "Ciudad Esmeralda", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 4250.00},
    {"origen": "Mordor", "destino": "Isengard", "tipo": "N", "distancia": 550.00, "tiempo": 1.6, "costo": 1375.00},
    {"origen": "Mordor", "destino": "Winkie", "tipo": "I", "distancia": 600.00, "tiempo": 3.2, "costo": 1500.00},
    {"origen": "Isengard", "destino": "Rohan", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1300.00},
    {"origen": "Isengard", "destino": "Moria", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1100.00},
    {"origen": "Moria", "destino": "Isengard", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1300.00},
    {"origen": "Moria", "destino": "Erebor", "tipo": "N", "distancia": 900.00, "tiempo": 2.3, "costo": 2225.00},
    {"origen": "Erebor", "destino": "Moria", "tipo": "N", "distancia": 900.00, "tiempo": 2.3, "costo": 2000.00},
    {"origen": "Erebor", "destino": "Gondor", "tipo": "N", "distancia": 1250.00, "tiempo": 3.0, "costo": 3525.00},
    {"origen": "Reino del Bosque", "destino": "Erebor", "tipo": "N", "distancia": 500.00, "tiempo": 4.5, "costo": 2450.00},
    {"origen": "Reino del Bosque", "destino": "Rivendel", "tipo": "N", "distancia": 950.00, "tiempo": 2.4, "costo": 2100.00},
    {"origen": "Narnia", "destino": "Telmar", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1800.00},
    {"origen": "Narnia", "destino": "Charn", "tipo": "N", "distancia": 450.00, "tiempo": 3.4, "costo": 3125.00},
    {"origen": "Narnia", "destino": "Gondor", "tipo": "I", "distancia": 550.00, "tiempo": 4.1, "costo": 2875.00},
    {"origen": "Narnia", "destino": "Ciudad Esmeralda", "tipo": "I", "distancia": 1300.00, "tiempo": 5.6, "costo": 4750.00},
    {"origen": "Telmar", "destino": "Narnia", "tipo": "N", "distancia": 400.00, "tiempo": 1.3, "costo": 1500.00},
    {"origen": "Telmar", "destino": "Rivendel", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 3750.00},
    {"origen": "Charn", "destino": "Narnia", "tipo": "N", "distancia": 450.00, "tiempo": 3.4, "costo": 1225.00},
    {"origen": "Charn", "destino": "Winkie", "tipo": "I", "distancia": 700.00, "tiempo": 3.4, "costo": 875.00},
    {"origen": "Ciudad Esmeralda", "destino": "Munchkin", "tipo": "N", "distancia": 200.00, "tiempo": 3.4, "costo": 875.00},
    {"origen": "Ciudad Esmeralda", "destino": "Winkie", "tipo": "N", "distancia": 300.00, "tiempo": 3.1, "costo": 2250.00},
    {"origen": "Ciudad Esmeralda", "destino": "Gondor", "tipo": "I", "distancia": 1100.00, "tiempo": 5.2, "costo": 4250.00},
    {"origen": "Ciudad Esmeralda", "destino": "Narnia", "tipo": "I", "distancia": 1300.00, "tiempo": 5.6, "costo": 4750.00},
    {"origen": "Winkie", "destino": "Mordor", "tipo": "I", "distancia": 600.00, "tiempo": 3.2, "costo": 750.00},
    {"origen": "Winkie", "destino": "Charn", "tipo": "I", "distancia": 700.00, "tiempo": 3.4, "costo": 875.00},
]

# Crear el grafo dirigido y agregar nodos y aristas
grafo = nx.DiGraph()

for ciudad, atributos in nodos.items():
    grafo.add_node(ciudad, **atributos)

for ruta in aristas:
    origen, destino = ruta["origen"], ruta["destino"]
    grafo.add_edge(origen, destino, **ruta)

# Marcar aristas bidireccionales internamente
for origen, destino in list(grafo.edges()):
    if grafo.has_edge(destino, origen):
        grafo[origen][destino]["flecha"] = "doble"
        grafo[destino][origen]["flecha"] = "doble"

# Configuración de colores y tamaños de nodos
colores_nodos = {'Capital': 'gold', 'Importante': 'skyblue', 'Ordinaria': 'lightgreen'}
tamaños_nodos = {'Capital': 1000, 'Importante': 700, 'Ordinaria': 500}
pos = nx.spring_layout(grafo, seed=42)

# Dibujar nodos y etiquetas
for tipo, color in colores_nodos.items():
    nodos_tipo = [nodo for nodo, datos in grafo.nodes(data=True) if datos['tipo'] == tipo]
    nx.draw_networkx_nodes(grafo, pos, nodelist=nodos_tipo,
                           node_color=color,
                           node_size=[tamaños_nodos[tipo]] * len(nodos_tipo),
                           alpha=0.8)
nx.draw_networkx_labels(grafo, pos, font_size=10, font_color='black')

# Dibujar aristas con validación de dirección:
# Si existe la arista inversa se dibuja una sola flecha bidireccional,
# de lo contrario se dibuja la flecha simple en la dirección registrada.
dibujadas = set()
for origen, destino, datos in grafo.edges(data=True):
    # Si ya se dibujó la conexión (en cualquiera de los sentidos), la saltamos
    if (origen, destino) in dibujadas or (destino, origen) in dibujadas:
        continue

    if datos.get("flecha") == "doble" and grafo.has_edge(destino, origen):
        # Dibujar solo una flecha bidireccional
        nx.draw_networkx_edges(grafo, pos, edgelist=[(origen, destino)],
                               arrowstyle='<->', arrowsize=20,
                               connectionstyle='arc3,rad=0.1', edge_color='gray', alpha=0.6)
        dibujadas.add((origen, destino))
        dibujadas.add((destino, origen))
    else:
        # Dibujar la flecha según la dirección única
        nx.draw_networkx_edges(grafo, pos, edgelist=[(origen, destino)],
                               arrowstyle='-|>', arrowsize=20,
                               connectionstyle='arc3,rad=0.1', edge_color='gray', alpha=0.6)
        dibujadas.add((origen, destino))

plt.title("Mapa de Rutas entre Ciudades de Mundos Fantásticos", fontsize=14)
plt.axis('off')
plt.show()

def conectar_bd():
    conn = sqlite3.connect("vuelos.db")
    cursor = conn.cursor()
    
    # Crear las tablas si no existen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ap_paterno TEXT NOT NULL,
        ap_materno TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL,
        nacionalidad TEXT NOT NULL,
        raza TEXT NOT NULL,
        telefono TEXT NOT NULL,
        correo TEXT NOT NULL
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vuelos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        origen TEXT NOT NULL,
        destino TEXT NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
    )''')
    
    conn.commit()
    return conn, cursor

def insertar_usuario(cursor, conn, nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo):
    cursor.execute('''
    INSERT INTO Usuarios (nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo))
    conn.commit()
    return cursor.lastrowid  # Devuelve el ID del usuario insertado

def insertar_vuelo(cursor, conn, usuario_id, origen, destino, fecha):
    cursor.execute('''
    INSERT INTO Vuelos (usuario_id, origen, destino, fecha)
    VALUES (?, ?, ?, ?)''', (usuario_id, origen, destino, fecha))
    conn.commit()

def solicitar_datos_usuario():
    nombre = input("Ingrese su nombre: ")
    ap_paterno = input("Ingrese su apellido paterno: ")
    ap_materno = input("Ingrese su apellido materno: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
    nacionalidad = input("Ingrese su nacionalidad: ")
    raza = input("Ingrese su raza: ")
    telefono = input("Ingrese su teléfono: ")
    correo = input("Ingrese su correo electrónico: ")
    return nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo

def solicitar_datos_vuelo():
    origen = input("Ingrese la ciudad de origen: ")
    destino = input("Ingrese la ciudad de destino: ")
    fecha = input("Ingrese la fecha del vuelo (YYYY-MM-DD): ")
    return origen, destino, fecha

def mostrar_rutas_optimizada(grafo, origen, destino, max_rutas=3, criterio="distancia"):
    try:
        rutas_generator = nx.shortest_simple_paths(grafo, source=origen, target=destino, weight=criterio)
    except nx.NetworkXNoPath:
        print(f"No existen rutas entre {origen} y {destino}.")
        return
    
    rutas = list(itertools.islice(rutas_generator, max_rutas))
    
    if not rutas:
        print(f"No se encontraron rutas entre {origen} y {destino}.")
        return

    print(f"\nSe encontraron {len(rutas)} rutas entre {origen} y {destino} (ordenadas por {criterio}):\n")
    
    for i, ruta in enumerate(rutas, start=1):
        total_distancia = 0
        total_tiempo = 0
        total_costo = 0
        
        for j in range(len(ruta) - 1):
            datos = grafo[ruta[j]][ruta[j+1]]
            total_distancia += datos.get("distancia", 0)
            total_tiempo += datos.get("tiempo", 0)
            total_costo += datos.get("costo", 0)
        
        print(f"Ruta {i}: {ruta}")
        print(f"   Distancia total: {total_distancia}")
        print(f"   Tiempo total: {total_tiempo}")
        print(f"   Costo total: {total_costo}\n")

if __name__ == "__main__":
    conn, cursor = conectar_bd()
    
    nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo = solicitar_datos_usuario()
    usuario_id = insertar_usuario(cursor, conn, nombre, ap_paterno, ap_materno, fecha_nacimiento, nacionalidad, raza, telefono, correo)
    
    origen, destino, fecha = solicitar_datos_vuelo()
    insertar_vuelo(cursor, conn, usuario_id, origen, destino, fecha)
    
    print("Datos guardados correctamente en la base de datos.")
    mostrar_rutas_optimizada(grafo, origen, destino, max_rutas=3, criterio="distancia")
    mostrar_rutas_optimizada(grafo, origen, destino, max_rutas=3, criterio="tiempo")
    mostrar_rutas_optimizada(grafo, origen, destino, max_rutas=3, criterio="costo")
    
    conn.close()
