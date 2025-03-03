import sympy as sp

# Definir la variable
x = sp.Symbol('x')

# Definir la ecuación exponencial
ecuacion = sp.Eq(2**x, 16)

# Resolver la ecuación
solucion = sp.solve(ecuacion, x)

# Mostrar el resultado
print("Solución de la ecuación exponencial:", solucion)
