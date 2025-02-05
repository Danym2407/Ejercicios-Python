# Solicitar la cantidad de números a evaluar
cant_num = int(input('¿Cuántos números deseas evaluar?: '))

# Inicializar una lista para almacenar los números
cal = []

# Iterar la cantidad de veces indicada por el usuario
for i in range(1, cant_num + 1):
    num = float(input(f'Ingresa el número {i} a evaluar: '))
    cal.append(num)  # Agregar el número a la lista

# Mostrar los números ingresados
print("Los números ingresados son:", cal)
