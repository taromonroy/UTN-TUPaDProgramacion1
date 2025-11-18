import archivo as ar
bandera = True
while bandera:
    print("\n=== Gestor de Productos ===")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ar.mostrar_productos()
    elif opcion == "2":
        ar.agregar_producto()
    elif opcion == "3":
        productos = ar.cargar_productos()
        ar.buscar_producto(productos)
    elif opcion == "4":
        print("Adiós...")
        bandera = False
    else:
        print("Opción inválida. Intente nuevamente.")