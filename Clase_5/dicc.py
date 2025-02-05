productos = {"manzana": 10, "plátano": 5, "naranja": 7}

def contar_palabras(frase):
    palabras = frase.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

print(contar_palabras("hola mundo hola"))
