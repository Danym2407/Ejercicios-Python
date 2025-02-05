
# Funcion de filtrado en diccionario, esto
# nos permite almacenar solo aquellas letras,
#cuya aparicion sea mayor a 5 veces

def filtrar(diccionario):
    return {k: v for k, v in diccionario.items() if v > 5} # Ciclo para recorrer

datos = {"a": 3, "b": 7, "c": 9, "d": 2} # Diccionario que se enviara
print(filtrar(datos))



