productos = {
    "Laptop": {"precio": 2000, "stock": 5},
    "Iphone": {"precio": 1500, "stock": 20},
    "Tablet": {"precio": 1000, "stock": 60},
    "Audifonos": {"precio": 500, "stock": 70},
    "Watch": {"precio": 1200, "stock": 40},
    
}

historialVentas = []
totalVentas = 0  # Variable para almacenar el valor total de las ventas realizadas

while True:
    print("\n--- MENU TIENDA LA SALLETECH ---")
    print("1. Visualizar catálogo de productos")
    print("2. Comprar un producto")
    print("3. Agregar stock a un producto")
    print("4. Consultar historial de ventas y total vendido")
    print("5. Agregar un nuevo producto")
    print("6. Salir")

    try:
        opcion = int(input("Ingrese una opción (1-6): "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue

    if opcion == 1:
        print("\n--- PRODUCTOS DISPONIBLES ---")
        for producto, detalles in productos.items():
            print(f"{producto}: ${detalles['precio']}, Stock: {detalles['stock']} unidades")

    elif opcion == 2:
        print("\n--- PRODUCTOS DISPONIBLES ---")
        for producto, detalles in productos.items():
            print(f"{producto}: ${detalles['precio']}, Stock: {detalles['stock']} unidades")

        producto = input("\nIngrese el nombre del producto que desea comprar: ").strip().capitalize() #Se implementan stip y capitaliza para que el usurio pueda escribir tanto en mayuscula como en misncula y el programa no genere un error

        if producto in productos:
            try:
                cantidad = int(input(f"Ingrese la cantidad de {producto} que desea comprar: "))
            except ValueError:
                print("Error: Ingrese una cantidad válida.")
                continue

            if 0 < cantidad <= productos[producto]["stock"]:
                total = cantidad * productos[producto]["precio"]
                print(f"\nCompra exitosa. Total a pagar: ${total}")
                productos[producto]["stock"] -= cantidad
                historialVentas.append((producto, cantidad, total))
                totalVentas += total  # Sumar al total de ventas
            else:
                print("Error: Stock insuficiente o cantidad inválida.")
        else:
            print("Error: Producto no encontrado.")

    elif opcion == 3:
        print("\n--- PRODUCTOS DISPONIBLES ---")
        for producto, detalles in productos.items():
            print(f"{producto}: ${detalles['precio']}, Stock: {detalles['stock']} unidades")

        producto = input("\nIngrese el nombre del producto al que desea agregar stock: ").strip().capitalize()

        if producto in productos:
            try:
                cantidad = int(input(f"Ingrese la cantidad de stock a agregar para {producto}: "))
            except ValueError:
                print("Error: Ingrese una cantidad válida.")
                continue

            if cantidad > 0:
                productos[producto]["stock"] += cantidad
                print(f"\nStock actualizado. Nuevo stock de {producto}: {productos[producto]['stock']}")
            else:
                print("Error: La cantidad debe ser mayor a 0.")
        else:
            print("Error: Producto no encontrado.")

    elif opcion == 4:
        print("\n--- HISTORIAL DE VENTAS ---")
        if not historialVentas:
            print("No hay ventas registradas.")
        else:
            for venta in historialVentas:
                print(f"Producto: {venta[0]}, Cantidad: {venta[1]}, Total: ${venta[2]}")
            print(f"\nTotal de ventas realizadas: ${totalVentas}")

    elif opcion == 5:
        nuevo_producto = input("\nIngrese el nombre del nuevo producto: ").strip().capitalize()

        if nuevo_producto in productos:
            print("Error: El producto ya existe en el catálogo.")
        else:
            try:
                precio = float(input(f"Ingrese el precio de {nuevo_producto}: "))
                stock = int(input(f"Ingrese la cantidad de stock de {nuevo_producto}: "))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
                continue

            if precio > 0 and stock >= 0:
                productos[nuevo_producto] = {"precio": precio, "stock": stock}
                print(f"\nProducto {nuevo_producto} agregado con éxito.")
            else:
                print("Error: Ingrese valores válidos para precio y stock.")

    elif opcion == 6:
        print("Saliendo del sistema...")
        break

    else:
        print("Error: Opción inválida. Intente de nuevo.")
