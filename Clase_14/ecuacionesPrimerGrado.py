import sympy as sp

# Definir las variables simbólicas
x, y, z = sp.symbols('x y z')

# Definir las ecuaciones
eq1 = sp.Eq(2*x + 3*y + 4*z, 20)
eq2 = sp.Eq(3*x - 5*y - z, -10)
eq3 = sp.Eq(-x + 2*y - 3*z, -6)

# Resolver el sistema
solucion = sp.solve((eq1, eq2, eq3), (x, y, z))

# Mostrar el resultado
print(solucion)  # Devuelve un diccionario con los valores de x, y, z
