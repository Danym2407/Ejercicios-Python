# Practicamos usar los widgets

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry('600x400+750+150')


tk.Label(root, text='Classic Label').pack()
# Se ve un poco mas obscuro
ttk.Label(root, text='Themed Label').pack()

# Ajustamos el Label
tk.Label(root, text='Texto con fuente', font=('Arial', 16, 'bold'), fg='blue', bg='lightgray').pack()

# Alineamos el texto
tk.Label(root, text='Alineado a la derecha', anchor='ne', justify='right', width=30).pack()


img = tk.PhotoImage(file='10t.jpg')  # Usa PNG o GIF
tk.Label(root, image=img).pack()



root.mainloop()
