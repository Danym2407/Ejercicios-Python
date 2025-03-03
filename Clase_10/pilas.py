class Pilas:
    
    def __init__(self):
        # Declaramos nuestra lista para almacenar los elementos
        self.items = []
        
    def apilar(self, item):
        # Agregar un elemento a la pila
        self.items.append(item)
        
    def desapilar(self):
        # Elimar y mostrar el ultimo elemento guardado
        if not self.estavacia():
            return self.items.pop()
        return None # En el caso de que la lista este vacia

    def estavacia(self):
        # Devolver True en caso de que la pila este vacia y False si no
        return len(self.items) == 0
    
    def ultimoElemento(self):
        # Devolver el ultimo elemento sin necesidad de eliminarlo
        if not self.estavacia():
            return self.items[-1]
        return None


pila = Pilas()
pila.apilar(20)
pila.apilar(10)
pila.apilar(33)

print(pila.desapilar())
print(pila.ultimoElemento())
print(pila.desapilar())
print(pila.ultimoElemento())
print(pila.desapilar())
print(pila.estavacia())