cant_num = int(input('¿Cuántos números deseas evaluar?: '))

for i in range (0, cant_num):
    num = float(input(f'Ingresa el numero {i + 1} a evaluar:'))
    num += num

print('Promedio es igual: ', (num/cant_num))
    
    
