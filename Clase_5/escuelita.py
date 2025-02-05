class Personita:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.materias = []
    
    def agregar_materia(self, materia):
        self.materias.append(materia)
    
    def mostrar_calificaciones(self):
        print(f"Calificaciones de {self.nombre}:")
        for materia in self.materias:
            print(f"{materia.nombre}: {materia.obtener_promedio():.2f} (Notas: {materia.listar_calificaciones()})")

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    
    def obtener_promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0.0
    
    def listar_calificaciones(self):
        return ", ".join(map(str, self.calificaciones))

# Ejemplo de uso
ejemplo = Personita("Daniela Mendez", 20)
materia1 = Materia("Matemáticas")
materia2 = Materia("Historia")

materia1.agregar_calificacion(90)
materia1.agregar_calificacion(85)
materia2.agregar_calificacion(78)
materia2.agregar_calificacion(82)

ejemplo.agregar_materia(materia1)
ejemplo.agregar_materia(materia2)

ejemplo.mostrar_calificaciones()