class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.color})"


class PilaAutos:
    def __init__(self):
        self.items = []  # Lista para almacenar los autos
    
    def apilar(self, auto):
        """Agrega un auto a la pila."""
        self.items.append(auto)

    def desapilar(self):
        """Elimina y devuelve el último auto agregado."""
        if not self.estavacia():
            return self.items.pop()
        return None  # Si la pila está vacía, retorna None

    def estavacia(self):
        """Devuelve True si la pila está vacía, False si no."""
        return len(self.items) == 0

    def cima(self):
        """Devuelve el auto en la cima sin eliminarlo."""
        if not self.estavacia():
            return self.items[-1]
        return None


# 🔹 Creación de objetos Auto
ferrari = Auto("Ferrari", "488 Spider", "Rojo")
jeep = Auto("Jeep", "Wrangler", "Negro")
vocho = Auto("Volkswagen", "Sedán", "Azul")

# 🔹 Creación de la pila de autos
pila_autos = PilaAutos()

# 🔹 Apilamos los autos
pila_autos.apilar(ferrari)
pila_autos.apilar(jeep)
pila_autos.apilar(vocho)

# 🔹 Operaciones con la pila de autos
print("Auto desapilado:", pila_autos.desapilar())  # Salida: Volkswagen Sedán (Azul)
print("Auto en la cima:", pila_autos.cima())       # Salida: Jeep Wrangler (Negro)
print("¿Está vacía la pila?", pila_autos.estavacia())  # Salida: False
