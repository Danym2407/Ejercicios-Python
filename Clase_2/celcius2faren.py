def cel2faren(c):
    return (((9/5)*c) + 32)

def faren2cel(f):
    return (((5/9)*c) - 32)
print('Menu')
print('a. De Celcius a Farenheit')
print('b. De Farenheit a Celcius')

op = (input('Que deseas convertir?\n'))


if(op == 'a'):
    cel = float(input('Ingresa los grados Celsius: '))
    print('De grados Celsius a Farenheit tu resultado es: ', cel2faren(cel))
else:
    faren = float(input('Ingresa los grados Faren: '))
    print('De grados Farenheit a Celsius tu resultado es: ', faren2cel(faren))
    
    

a



