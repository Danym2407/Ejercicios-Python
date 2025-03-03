import sympy as sp

# Definir la variable
x = sp.Symbol('x')

# Definir la ecuación
ecuacion = sp.Eq(x**2 - 5*x + 6, 0)

# Resolver la ecuación
solucion = sp.solve(ecuacion, x)

# Mostrar el resultado
print("Solución de la ecuación:", solucion)
