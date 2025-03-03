import re

def limpiar_texto(texto):
    """
    Elimina secuencias innecesarias de espacios, tabulaciones y saltos de línea.
    """
    return re.sub(r"\s+", " ", texto).strip()

def extraer_horarios(nombre_archivo="horarios.txt"):
    """
    Extrae materias y horarios respetando la estructura del archivo.
    """
    materias = []
    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    # Divide el contenido en bloques de materias usando los separadores "*****"
    bloques = re.split(r"\*{5,}", contenido)

    for bloque in bloques:
        bloque = limpiar_texto(bloque)  # Elimina espacios y saltos de línea innecesarios
        
        # Extrae el nombre de la materia (la primera coincidencia con "LAB.")
        materia_match = re.search(r"(LAB(?:ORATORIO)?\.? DE [A-ZÁÉÍÓÚÑ\s]+)", bloque)
        if not materia_match:
            continue  # Si no encuentra materia, salta al siguiente bloque
        
        materia = materia_match.group(0).strip()
        
        # Encuentra todos los días y horarios dentro del bloque
        horarios = re.findall(r"(Lunes|Martes|Miércoles|Jueves|Viernes|Sábado|Domingo)\s+(\d{1,2}\s*-\s*\d{1,2})\s*Hrs\.?", bloque)

        for dia, horario in horarios:
            materias.append((materia, dia, f"{horario} Hrs."))

    return materias

def guardar_horarios(materias, nombre_archivo="materias.txt"):
    """
    Guarda la lista de materias formateadas en un archivo de texto.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("# Definimos las materias y sus horarios\n")
        archivo.write("materias = [\n")
        for materia in materias:
            archivo.write(f"    {materia},\n")
        archivo.write("]\n")

# Extrae los horarios
materias = extraer_horarios()

# Guarda el resultado en materias.txt
guardar_horarios(materias)

print("¡Horarios extraídos correctamente y guardados en materias.txt!")
