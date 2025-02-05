# Quiero mandar un regalo a su noviaa, tienda con productos y precios fijos.
# Mostrar lo que la tienda tiene disponible, que deje elegir cuantos tiene

# Inventario inicial con precios y cantidad disponibles
tienda_regalos = {
    "Ositos": {"precio": 100, "stock": 10},
    "Girasoles": {"precio": 200, "stock": 5},
    "Rosas": {"precio": 200, "stock": 15},
    "Tulipanes": {"precio": 300, "stock": 8},
    "Relojes": {"precio": 300, "stock": 3},
    "Collares": {"precio": 200, "stock": 7}
}

def mostrar_inventario():
    print("\n Bienvenido a la Tienda de Regalos")
    print("Estos son los productos disponibles:")
    for producto, detalles in tienda_regalos.items():
        print(f"- {producto}: ${detalles['precio']} (Stock: {detalles['stock']})")

def elegir_producto():
    carrito = {}
    while True:
        mostrar_inventario()
        producto = input("\n¿Qué producto deseas? (Escribe 'salir' para terminar): ").capitalize()
        
        if producto == "Salir":
            break
        elif producto in tienda_regalos:
            cantidad = int(input(f"¿Cuántos '{producto}' deseas? "))
            if cantidad <= tienda_regalos[producto]["stock"]:
                carrito[producto] = cantidad
                tienda_regalos[producto]["stock"] -= cantidad
                print(f"Has agregado {cantidad} '{producto}' al carrito.")
            else:
                print(f"X No tenemos suficiente stock. Solo hay {tienda_regalos[producto]['stock']} disponibles.")
        else:
            print("X Producto no encontrado. Intenta de nuevo.")
    return carrito

def calcular_total(carrito):
    total = 0
    print("\n Resumen de tu compra:")
    for producto, cantidad in carrito.items():
        precio = tienda_regalos[producto]["precio"]
        total += precio * cantidad
        print(f"- {producto} x{cantidad}: ${precio * cantidad}")
    print(f"\n Total a pagar: ${total}")
    return total

# Función principal
def tienda():
    carrito = elegir_producto()
    if carrito:
        calcular_total(carrito)
        print("\n¡Gracias por tu compra! ")
    else:
        print("No has agregado nada al carrito. ¡Vuelve pronto!")

# Iniciar tienda
tienda()





