"""
    Ejercicio 2: 
    Control de Inventario de un Supermercado Crea un programa que pida el nombre de 5 productos y sus respectivos precios. 
    Luego, usa un ciclo for para calcular el precio total de los productos ingresados. 
    Si el total supera $500.000, muestra un mensaje indicando que se necesita autorización del gerente.
"""

# Almacenamos en una lista vacia los productos y precios
productos = []
precios = []
total = 0

# Usamos un ciclo for que se repite 5 veces con un input para pedir al usurio los datos nombre y precio
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio del producto {producto}: ")) #Convetimos el numero en decimal 
    
    productos.append(producto)#.append no genera los datos imgresados en forma de lista
    precios.append(precio)

# Se recorre la lista creada y se suman los valores
for precio in precios:
    total += precio

# Mostramos el total y verificamos si supera los 500.000
print("\nResumen de productos y precios:")
for i in range(5):
    print(f"{productos[i]}: ${precios[i]:.2f}")

print(f"\nPrecio total: ${total:.2f}")

if total > 500000:
    print("Se necesita autorización del gerente.")
