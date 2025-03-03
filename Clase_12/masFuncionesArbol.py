""" 
Código realizado por Daniela Méndez Ramírez

Ejemplo: Árboles Binarios en Python con más funciones
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

    # 1. Determinar el nivel de un nodo
    def nivel_nodo(self, nodo, valor, nivel=0):
        if nodo is None:
            return -1  # El nodo no existe en el árbol
        if nodo.valor == valor:
            return nivel

        izquierda = self.nivel_nodo(nodo.izquierda, valor, nivel + 1)
        if izquierda != -1:
            return izquierda

        return self.nivel_nodo(nodo.derecha, valor, nivel + 1)

    # 2. Determinar la profundidad del árbol
    def profundidad(self, nodo=None):
        if nodo is None:
            return 0
        return 1 + max(self.profundidad(nodo.izquierda), self.profundidad(nodo.derecha))

    # 3. Determinar si un nodo es hoja
    def es_hoja(self, nodo):
        return nodo is not None and nodo.izquierda is None and nodo.derecha is None

    # 4. Imprimir todos los nodos hoja
    def imprimir_hojas(self, nodo):
        if nodo is not None:
            if self.es_hoja(nodo):
                print(nodo.valor, end=" ")
            self.imprimir_hojas(nodo.izquierda)
            self.imprimir_hojas(nodo.derecha)

    # 5. Encontrar el nodo con el máximo valor
    def encontrar_maximo(self, nodo):
        while nodo.derecha is not None:
            nodo = nodo.derecha
        return nodo.valor

# Prueba del árbol
arbol = ArbolBinario()
valores = [10, 5, 15, 3, 7, 12, 18]

for v in valores:
    arbol.insertar(v)

print("Recorrido inorden:")
arbol.inorden(arbol.raiz)  # Salida esperada: 3 5 7 10 12 15 18
print("\n")

# Probando las funciones
nodo_busqueda = 7
print(f"Nivel del nodo {nodo_busqueda}: {arbol.nivel_nodo(arbol.raiz, nodo_busqueda)}")  # Esperado: 2

print(f"Profundidad del árbol: {arbol.profundidad(arbol.raiz)}")  # Esperado: 3

print("Nodos hoja:", end=" ")
arbol.imprimir_hojas(arbol.raiz)  # Esperado: 3 7 12 18
print("\n")

print(f"Máximo valor en el árbol: {arbol.encontrar_maximo(arbol.raiz)}")  # Esperado: 18
