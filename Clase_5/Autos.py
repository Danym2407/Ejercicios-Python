class Auto:
    
    def __init__(self, marca, modelo, posicion=0): 
        self.marca = marca
        self.modelo = modelo
        self.posicion = posicion
        
    def avanzar(self, x=1):
        self.posicion += x
    
    def imprimir(self):
        print(self.marca, self.modelo, '|', self.posicion, 'Km')
        
# Creamos miVocho que es el primer objeto    
# Su instancia en es
miVocho = Auto('VW', 'Sedan')
miVocho.avanzar(100)
miVocho.imprimir()

# Creamos un nuevo objeto
miFerrari = Auto('Ferrari', 'Clasico', 500)
miFerrari.imprimir()

# Creamos nuestro 3er objeto
miCoche = miVocho
miCoche.imprimir()

miCoche.avanzar(200)
miCoche.imprimir()
miVocho.imprimir()

miCoche = None
miCoche = Auto('Nissan', 'Tsuru')
miCoche.imprimir()
