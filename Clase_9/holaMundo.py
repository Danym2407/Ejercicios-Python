# Agregamos la librería
import tkinter as tk

# Creamos la instancia
root = tk.Tk()

# Escribimos nuestro mensaje
message = tk.Label(root, text="Hello, World!")
message2 = tk.Label(root, text="Hola Daniela")
message.pack()
message2.pack()

# Mantenemos la pestaña desplegandose
root.mainloop()