"""
    Ejercicio 1: 
    Descuento en el Supermercado Escribe un programa que solicite al usuario el monto total de su compra en el supermercado. 
    Si la compra es mayor a $100.000, se aplica un 10% de descuento. 
    El programa debe calcular el total a pagar después del descuento y mostrarlo en pantalla.
"""

# Se definen los product
productos = {
    "labial": 35000,
    "polvos": 50000,
    "crema": 30000,
    "rubor": 20000
}

carrito = []  

#Entramos al bluque while hasta que el usuario rompa el ciclo con la opción 5 que ejecutara el breack
while True:
    print("\nMenú:")
    print("1. Ver lista de productos")
    print("2. Seleccionar productos")
    print("3. Eliminar producto del carrito")
    print("4. Ver total y pagar")
    print("5. Salir")

    opcion = input("Elige una opción: ")
    
#Si la opción es 1 se imprime los productos dosponibles con su precio

    if opcion == "1":
        print("\nProductos disponibles:")
        for producto, precio in productos.items():
            print(f"{producto.capitalize()}: ${precio}")# Con .capitalize() conviete la entrada en un string 
            
#El usuario escribe el nombre del producto que decea agregar a la lista
    elif opcion == "2":
        producto_seleccionado = input("Escribe el nombre del producto que quieres agregar: ").lower() #lower convierte el nombre a minuscula parae vitar errores.
        if producto_seleccionado in productos:
            carrito.append(productos[producto_seleccionado])
            print(f"{producto_seleccionado.capitalize()} agregado al carrito.")
        else:
            print("Producto no encontrado.")#Si escribe un producto que no esta en la lista sale el mensaje 

    elif opcion == "3":
        if not carrito:
            print("Tu carrito está vacío.")
        else:
            print("Productos en tu carrito:")#Enmuera los productos que estan en el carrito
            for i, precio in enumerate(carrito):
                print(f"{i + 1}. ${precio}")
            indice = int(input("Ingresa el número del producto a eliminar: ")) - 1
            if 0 <= indice < len(carrito):
                carrito.pop(indice)#Permite selececionar el producto que se quere borrar
                print("Producto eliminado.")
            else:
                print("Opción inválida.")
                
#Se aplica el 10% de descuento sobre la compra si es >= $100.000

    elif opcion == "4":
        total_compra = sum(carrito)
        if total_compra >= 100000:
            total_pagar = total_compra * 0.90  # Aplica el 10% de descuento 
        else:
            total_pagar = total_compra 

        print(f"\nTotal de la compra: ${total_compra}")
        print(f"Total a pagar con descuento: ${total_pagar}")

    elif opcion == "5":
        print("Gracias por tu compra.")
        break