""" 
Código realizado por Daniela Méndez Ramírez

Ejemplo: Árboles Binarios en Python
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Clase con la que manejaremos al árbol
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    # Métodos de recorrido dentro de la clase
    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=" ")

# Prueba del árbol
arbol = ArbolBinario()
valores = [10, 5, 15, 3, 7, 12, 18]

for v in valores:
    arbol.insertar(v)

print("Recorrido inorden:")
arbol.inorden(arbol.raiz)  # Salida esperada: 3 5 7 10 12 15 18
