import tkinter as tk

# Función para guardar los datos en un archivo de texto
def guardar_datos():
    nombre = entrada_nombre.get()
    apellido_paterno = entrada_apellido_paterno.get()
    apellido_materno = entrada_apellido_materno.get()
    fecha_nacimiento = entrada_fecha_nacimiento.get()
    sexo = var_sexo.get()

    # Guardar en el archivo de texto
    with open("datos_persona.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Apellido Paterno: {apellido_paterno}\n")
        archivo.write(f"Apellido Materno: {apellido_materno}\n")
        archivo.write(f"Fecha de Nacimiento: {fecha_nacimiento}\n")
        archivo.write(f"Sexo: {sexo}\n")
        archivo.write("-" * 30 + "\n")  # Separador para facilitar lectura

    # Limpiar el formulario después de guardar
    entrada_nombre.delete(0, tk.END)
    entrada_apellido_paterno.delete(0, tk.END)
    entrada_apellido_materno.delete(0, tk.END)
    entrada_fecha_nacimiento.delete(0, tk.END)
    var_sexo.set(None)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Datos Personales")
ventana.configure(bg="#FFF0F5")  # Color de fondo rosado claro

# Crear las etiquetas y campos de entrada
etiqueta_nombre = tk.Label(ventana, text="Nombre:", font=("Arial", 12), bg="#FFF0F5")
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_nombre = tk.Entry(ventana, font=("Arial", 12), bg="#FFE4E1")
entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

etiqueta_apellido_paterno = tk.Label(ventana, text="Apellido Paterno:", font=("Arial", 12), bg="#FFF0F5")
etiqueta_apellido_paterno.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entrada_apellido_paterno = tk.Entry(ventana, font=("Arial", 12), bg="#FFE4E1")
entrada_apellido_paterno.grid(row=1, column=1, padx=10, pady=5)

etiqueta_apellido_materno = tk.Label(ventana, text="Apellido Materno:", font=("Arial", 12), bg="#FFF0F5")
etiqueta_apellido_materno.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entrada_apellido_materno = tk.Entry(ventana, font=("Arial", 12), bg="#FFE4E1")
entrada_apellido_materno.grid(row=2, column=1, padx=10, pady=5)

etiqueta_fecha_nacimiento = tk.Label(ventana, text="Fecha de Nacimiento (DD/MM/AAAA):", font=("Arial", 12), bg="#FFF0F5")
etiqueta_fecha_nacimiento.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entrada_fecha_nacimiento = tk.Entry(ventana, font=("Arial", 12), bg="#FFE4E1")
entrada_fecha_nacimiento.grid(row=3, column=1, padx=10, pady=5)

etiqueta_sexo = tk.Label(ventana, text="Sexo:", font=("Arial", 12), bg="#FFF0F5")
etiqueta_sexo.grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Opción de género: radio buttons
var_sexo = tk.StringVar()
radio_masculino = tk.Radiobutton(ventana, text="Masculino", variable=var_sexo, value="Masculino", font=("Arial", 12), bg="#FFF0F5")
radio_masculino.grid(row=4, column=1, padx=10, pady=5, sticky="w")
radio_femenino = tk.Radiobutton(ventana, text="Femenino", variable=var_sexo, value="Femenino", font=("Arial", 12), bg="#FFF0F5")
radio_femenino.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Botón para guardar los datos
boton_guardar = tk.Button(ventana, text="Guardar Datos", font=("Arial", 12), bg="#FFB6C1", fg="#000000", command=guardar_datos)
boton_guardar.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar la ventana
ventana.mainloop()
