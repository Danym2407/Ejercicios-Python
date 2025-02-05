# San Valentin Program
import os
import re

if os.path.exists("Personitas.txt"):
    os.remove("Personitas.txt")
    
    
f = open("Personitas.txt", "x")

f.write("""
        Amigos:{
                Iris Yulit Jasso Cortes {cualidades: divertida, amable, mi mejor amiga} 
                Joshua Abdiel Barragan Guardado {cualidades: honesta, un amor, directa, en general eres mi mejor amigo}
                Rodrigo Cruz Bartolo {cualidades: divertida, chistosa, y super adoro hablar contigo}
            }
        Crushes:{
                Lorenzo Grebe {cualidades: eres una persona amable, educado, alto, bonito, ojos bonitos, soliamos estudiar juntos, sonrisa hermosa, coqueto, te sientas adelante en el salon}
                Secreto {cualidades: listo, buena onda, lees mucho, eres divertido, usas frases chistosas, me gusta hablar contigo, desyunas muy rapido y me tienes que esperar mientras yo desayuno}
        }
        """)

f.close()


f = open("Personitas.txt", "r")
personitasCartita = f.read()
f.close()
#print(personitasCartita)


# We create the frinds letter

if os.path.exists("Platilla_Amigos.txt"):
    os.remove("Platilla_Amigos.txt")
    
f = open("Platilla_Amigos.txt", "x")
    
f.write("""
        
        Feliz San Valentin nombre,
        Esta carta la escribo con todo mi cariño,
        esperando te encuentres bien, a continuación
        te voy a decir algunas de las razones por las
        que te quiero demasiado y por qué eres importante
        para mi:
        
        Eres una persona cualidades.
        
        Pero no solo son ese tipo de cosas las que te hacen especial
        para mi, lo que realmente aprecio de nuestra amistad, es que es 
        verdadera, que puedo contar contigo en las buenas y en las malas,
        que no vas a temer decirme la verdad, pero tambien estar 
        ahi cuando lo necesite. 
        
        Te quiero muchooooo.
        
        Dany.
        
        
        """)
f.close()

f = open("Platilla_Amigos.txt", "r")
cartita_amiguitos = f.read()
#print(cartita_amiguitos)


# We create our crush letter

if os.path.exists("cartitaCrush.txt"):
    os.remove("cartitaCrush.txt")
    
    
f = open("cartitaCrush.txt", "w")
f.write(""" 
        Feliz San Valentin, nombre
        Probablemente te preguntes por qué te estoy escribiendo una carta,
        lo mismo me pregunto yo, sin embargo, una tarea me ha llevado a esto,
        si bien creo que en San Valentin puedes festejar las amistades, 
        también creo que es para sentirse enamorado y disfrutar de este sentimiento.
        
        Y he aqui mi carta, probablemente a estas alturas ya sepas que siento 
        algo por ti. Tendré que ser honesta y admitir que no es un simple crush,
        al menos no del todo.
        
        Eres una persona a la que he conocido poco, pero en ese breve tiempo, 
        me hiciste pasarmela increíble, la verdad te me haces un niño espectacular
        y de alguna manera lograste meterte en mi mente, debido a ciertas cosas que
        he notado de ti, como que eres: cualidades.
        
        En fin puede que algunas sean un poco torpes y superficiales, pero en realidad
        son validas para mi, son de esas pequeñas razones que me hacen sentir que quiero
        conocerte más. 
        
        Entonces dejando esta carta a tu alcance, te pregunto si estas interesado en
        conocer alguna de tus posibles futuras razones para encontrar tus razones que te 
        hagan sentir de la misma manera que yo por ti.
        
        Así que feliz 14 de Febrero, espero podamos vernos pronto.
        
        Dany.
   
        """)

f.close()

f = open("cartitaCrush.txt", "r")
cartitaCrush = f.read()
f.close()

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

    
    
            

# print(amigos)
# print(crushes)



if not os.path.exists("Amigos"):
    os.makedirs("Amigos")
    
if not os.path.exists("Crushes"):
    os.makedirs("Crushes")
    
    
# Desglosamos el glosario de Amigos
for nombre, cualidades in amigos.items():
    arch_personalizado = os.path.join("Amigos", f"{nombre}.txt")
    
    if os.path.exists(arch_personalizado):
        os.remove(arch_personalizado)
    
    with open(arch_personalizado, "w") as f:
        carta = cartita_amiguitos.replace("Crushes", nombre).replace("cualidades", cualidades)
        f.write(carta)
        f.close()
        
# Desglosamos el glosario de Crushes
for nombre, cualidades in crushes.items():
    arch_personalizado = os.path.join("Crushes", f"{nombre}.txt")
    
    if os.path.exists(arch_personalizado):
        os.remove(arch_personalizado)
    
    with open(arch_personalizado, "w") as f:
        carta = cartitaCrush.replace("nombre", nombre).replace("cualidades", cualidades)
        f.write(carta)
        f.close()

