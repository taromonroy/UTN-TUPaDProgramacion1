"""
EJERCICIO 2
"""
def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

"""EJERCICIO 3"""
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad: ")
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado con éxito.\n")

"""EJERCICIO 4"""
def cargar_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

"""EJERCICIO 5"""
def buscar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

"""EJERCICIO 6"""
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Archivo guardado.\n")