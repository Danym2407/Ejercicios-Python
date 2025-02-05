# Agregamos la librería
import tkinter as tk

# Creamos la instancia
root = tk.Tk()

# Cambiamos el nombre de la ventana
root.title('Pruebita Daniela')
# Definimos el tamanio de la pantalla
root.geometry('600x400+750+150')
# Deshabilitamos ajustar el tamanio de la ventana
root.resizable(False, False)
root.attributes('-alpha', 0.5)
root.attributes('-topmost', 1)
root.iconbitmap('./assets/pythontutorial.ico')
root.mainloop()

"""
# Escribimos nuestro mensaje
message = tk.Label(root, text="Hello, World!")
message2 = tk.Label(root, text="Hola Daniela")
message.pack()
message2.pack()

# Mantenemos la pestaña desplegandose


"""
