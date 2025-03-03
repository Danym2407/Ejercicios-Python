import sympy as sp

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función a derivar
f = x**3 + 2*x**2 + x + 5

# Calcular la derivada
dfdx = sp.diff(f, x)

# Mostrar el resultado
print(dfdx)  # Salida: 3*x**2 + 4*x + 1
