import sympy as sp

# Definir la variable y la función
x = sp.Symbol('x')
f = x**3 + 2*x**2 - 3*x + 5

# Calcular la primera derivada
primera_derivada = sp.diff(f, x)

# Calcular la segunda derivada
segunda_derivada = sp.diff(primera_derivada, x)

# Mostrar los resultados
print("Primera derivada:", primera_derivada)
print("Segunda derivada:", segunda_derivada)
