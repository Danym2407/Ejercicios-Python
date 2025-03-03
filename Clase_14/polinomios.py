import sympy as sp

# Definir las variables
x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5')

# Definir las ecuaciones
eq1 = sp.Eq(5*x1 + 4*x2 - x3 + 2*x4 - 9*x5, 29)
eq2 = sp.Eq(4*x1 + 3*x2 - 5*x3 - 5*x4 + 4*x5, -65)
eq3 = sp.Eq(6*x1 - 6*x2 - 3*x3 - 9*x4 + 4*x5, -113)
eq4 = sp.Eq(-8*x1 + 8*x2 + 5*x3 - 3*x4 - 6*x5, 35)
eq5 = sp.Eq(-3*x1 - 7*x2 + 2*x3 - 5*x4 + 4*x5, -50)

# Resolver el sistema de ecuaciones
solucion = sp.solve((eq1, eq2, eq3, eq4, eq5), (x1, x2, x3, x4, x5))

# Mostrar la solución
print("Solución del sistema:")
for var, val in solucion.items():
    print(f"{var} = {val}")
