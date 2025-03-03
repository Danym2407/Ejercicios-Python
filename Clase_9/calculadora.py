import tkinter as tk
import math

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("Calculadora Científica")
raiz.configure(bg="#FFF0F5")  # Color de fondo rosado claro

# Campo de entrada para los cálculos
entrada = tk.Entry(
    raiz, 
    width=25, 
    font=("Arial", 18), 
    justify="right", 
    bg="#FFE4E1",  # Fondo rosado pastel
    fg="#000000", 
    bd=10, 
    relief=tk.FLAT
)
entrada.grid(row=0, column=0, columnspan=7, pady=10, padx=10)  # Cambié columnspan de 6 a 7

# Función para manejar las acciones de los botones
def al_hacer_click(valor_boton):
    try:
        if valor_boton == "=":  # Evaluar la expresión ingresada
            resultado = eval(
                entrada.get(), 
                {"math": math, "sqrt": math.sqrt, "log": math.log, "sin": math.sin, 
                 "cos": math.cos, "tan": math.tan, "pi": math.pi, "e": math.e}
            )
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        elif valor_boton == "AC":  # Limpiar el campo de entrada
            entrada.delete(0, tk.END)
        elif valor_boton == "Rad":  # Convertir a radianes
            entrada.insert(tk.END, "math.radians(")
        elif valor_boton == "Deg":  # Convertir a grados
            entrada.insert(tk.END, "math.degrees(")
        elif valor_boton in ["sin", "cos", "tan", "log", "sqrt", "exp"]:  # Funciones matemáticas
            entrada.insert(tk.END, f"math.{valor_boton}(")
        elif valor_boton == "x!":  # Calcular el factorial
            expresion = int(entrada.get())
            resultado = math.factorial(expresion)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        elif valor_boton == "Ans":  # Placeholder para último resultado
            pass  # Puedes agregar la funcionalidad aquí
        elif valor_boton == "x²":  # Elevar al cuadrado
            expresion = float(entrada.get())
            resultado = expresion ** 2
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        elif valor_boton == "π":  # Insertar el valor de pi
            entrada.insert(tk.END, str(math.pi))
        elif valor_boton == "e":  # Insertar el valor de e
            entrada.insert(tk.END, str(math.e))
        else:  # Insertar cualquier otro valor
            entrada.insert(tk.END, valor_boton)
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")  # Mostrar mensaje de error en caso de fallo

# Lista de botones con su disposición, agregando columna para operaciones básicas
botones = [
    ('Rad', 1, 0), ('Deg', 1, 1), ('x!', 1, 2), ('(', 1, 3), (')', 1, 4), ('%', 1, 5), ('+', 1, 6),
    ('Inv', 2, 0), ('sin', 2, 1), ('ln', 2, 2), ('7', 2, 3), ('8', 2, 4), ('9', 2, 5), ('-', 2, 6),
    ('π', 3, 0), ('cos', 3, 1), ('log', 3, 2), ('4', 3, 3), ('5', 3, 4), ('6', 3, 5), ('*', 3, 6),
    ('e', 4, 0), ('tan', 4, 1), ('√', 4, 2), ('1', 4, 3), ('2', 4, 4), ('3', 4, 5), ('/', 4, 6),
    ('AC', 5, 0), ('Ans', 5, 1), ('EXP', 5, 2), ('x²', 5, 3), ('0', 5, 4), ('=', 5, 5), (' ', 5, 6)
]

# Crear botones dinámicamente
for (texto, fila, columna) in botones:
    boton = tk.Button(
        raiz, 
        text=texto, 
        width=5, 
        height=2, 
        font=("Arial", 12),
        bg="#FFB6C1" if fila % 2 == 0 else "#FFC0CB",  # Alternar tonos rosados
        fg="#000000", 
        activebackground="#FF69B4", 
        bd=2,
        relief=tk.RAISED, 
        command=lambda t=texto: al_hacer_click(t)
    )
    boton.grid(row=fila, column=columna, padx=3, pady=3, sticky="nsew")

# Ajustar el tamaño de las columnas y filas
total_columnas = 7  # Actualizado a 7 columnas
for columna in range(total_columnas):
    raiz.grid_columnconfigure(columna, weight=1)
for fila in range(1, 6):
    raiz.grid_rowconfigure(fila, weight=1)

# Iniciar el bucle principal de la interfaz gráfica
raiz.mainloop()
