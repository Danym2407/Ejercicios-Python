import re

personitasCartita = """
    Amigos:{
            Iris Yulit Jasso Cortes {cualidades: divertida, amable, mi mejor amiga} 
            Joshua Abdiel Barragan Guardado {cualidades: honesto, un amor de persona, directo, mi mejor amigo}
            Rodrigo Cruz Bartolo {cualidades: divertido, me encanta hablar contigo, chistoso}
        }
    Crushes:{
            Lorenzo Grebe {cualidades: eres una persona amable, educado, alto, bonito, ojos bonitos, soliamos estudiar juntos, sonrisa hermosa, coqueto, te sientas adelante en el salon}
            Secreto {cualidades: listo, buena onda, lees mucho, eres divertido, usas frases chistosas, me gusta hablar contigo, desyunas muy rapido y me tienes que esperar mientras yo desayuno}
    }
"""


# Expresión regular ajustada para extraer las categorías (Amigos, Crushes) y su contenido
categorias = re.findall(r"(\w+):\s*{([^{}]+(?:\{[^}]*\}[^{}]*)*)}", personitasCartita)


# Habilitamos la variable para el diccionario
amigos = {}
crushes = {}


# Mostramos los bloques encontrados
for categoria, contenido in categorias:
    #print(f"Categoría: {categoria}")
    #print(f"Contenido:\n{contenido}\n")
    
    #Capturar el nombre
    nombres = re.findall(r"([\w\s]+?)\s*\{cualidades:", contenido)
    # Limpiar los saltos de línea y espacios adicionales de cada nombre
    nombres_limpios = [nombre.strip() for nombre in nombres]
    
    #print(nombres_limpios)
    
    
    #Capturar cualidades
    cualidades = re.findall(r"\{cualidades:\s*([^}]+)\}", contenido)
    #print(cualidades)
    
    # Creamos un diccionario
    if categoria == "Amigos":
        for i, nombre in enumerate(nombres_limpios):
            amigos[nombre] = cualidades[i]
    else:
        for i, nombre in enumerate(nombres_limpios):
            crushes[nombre] = cualidades[i]
            

print(amigos)
print(crushes)
    
            

