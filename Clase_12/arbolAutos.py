""" 
Código realizado por Daniela Méndez Ramírez

Ejemplo: Árbol Binario con Autos en Python
"""

class Auto:
    """Clase que representa un auto con marca, modelo y año."""
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __lt__(self, otro):
        """Permite comparar autos por año (para insertar en el árbol)."""
        return self.año < otro.año

    def __str__(self):
        """Devuelve una representación en texto del auto."""
        return f"{self.marca} {self.modelo} ({self.año})"


class Nodo:
    """Nodo del árbol que almacena un auto."""
    def __init__(self, auto):
        self.auto = auto
        self.izquierda = None
        self.derecha = None


class ArbolBinarioAutos:
    """Árbol binario de búsqueda que organiza autos por año."""
    def __init__(self):
        self.raiz = None

    def insertar(self, auto):
        """Inserta un auto en el árbol según su año."""
        if self.raiz is None:
            self.raiz = Nodo(auto)
        else:
            self._insertar_recursivo(self.raiz, auto)

    def _insertar_recursivo(self, nodo, auto):
        if auto < nodo.auto:  # Comparación por año gracias a __lt__
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(auto)
            else:
                self._insertar_recursivo(nodo.izquierda, auto)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(auto)
            else:
                self._insertar_recursivo(nodo.derecha, auto)

    def inorden(self, nodo):
        """Recorre el árbol en inorden (autos ordenados por año)."""
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.auto)  # Usa __str__ para imprimir el auto
            self.inorden(nodo.derecha)


# Prueba del árbol con autos
arbol_autos = ArbolBinarioAutos()
autos = [
    Auto("Toyota", "Corolla", 2015),
    Auto("Ford", "Mustang", 2020),
    Auto("Honda", "Civic", 2018),
    Auto("Chevrolet", "Camaro", 2017),
    Auto("Tesla", "Model 3", 2022),
    Auto("BMW", "Serie 3", 2016),
]

# Insertamos los autos en el árbol
for auto in autos:
    arbol_autos.insertar(auto)

# Recorrido inorden (debería imprimir autos ordenados por año)
print("\n");
print("Autos ordenados por año:")
arbol_autos.inorden(arbol_autos.raiz)
print("\n");
