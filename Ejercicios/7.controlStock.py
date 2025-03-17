# Control de Stock
"""
Ejercicio 7: 
Control de Stock en una Tienda Crea un programa que pida el nombre de un producto 
y la cantidad disponible en stock. Si la cantidad es menor a 10 unidades, 
muestra un mensaje indicando que es necesario hacer un nuevo pedido.
"""

productos = []
# Creamos un menú de opciones
while True:
    
    print("CONTROL DE STOCK")
    print("1. Ingresar producto")
    print("2. Ver stock")
    print("3. Salir")

    opcion = int(input("digite la opcion: "))

    if opcion == 1:
        while True:
            producto = input("Ingresa el nombre del producto (o 0 para salir): ")
            if producto == "0": # Esta condicion permite que salga de la opcion 1
                break
            productos.append(producto)
            cantidad = int(input("intresa la cantidad de producto: "))
            if cantidad < 10:
# Esta condicion avisa cuando un producto tiene menos de 10 unidades.                
                print("Necesitas hacer un NUEVO pedido") 
            elif cantidad < 0:
                print("Ingresa una cantidad valida")
            else:
                print(f"Ingresaste {cantidad}, {producto}")
    elif opcion == 2:
        for producto in productos:
# Quise incluir la opcion de que el usuario viera cuales son los productos ingresados 
            print(f"la lista de pruductos ingresados es: {producto}")
    elif opcion == 3:
        print("sistema finalizado")
        break
    else:
        print("opcion no valida, intentelo de nuevo")
        




