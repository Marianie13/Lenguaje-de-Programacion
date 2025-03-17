# Control precios
"""
Ejercicio 10: 
Control de Precios en un Supermercado Desarrolla un programa que permita ingresar 
los precios de varios productos en un supermercado hasta que el usuario ingrese 0. 
Luego, muestra el precio más alto, el más bajo y el promedio de los productos ingresados. 
"""
precios = []

while True:
    precio = float(input("Ingresa el precio del producto (o 0 para finalizar): "))
    
    if precio == 0:
        break  # Sale del bucle si se ingresa 0
    elif precio < 0:
        print("El precio no puede ser negativo. Intenta de nuevo.")
    else:
        precios.append(precio)

if len(precios) > 0:  
    precio_mas_alto = max(precios)
    precio_mas_bajo = min(precios)
    promedio = sum(precios) / len(precios)

    print(f"\nPrecio más alto: {precio_mas_alto}")
    print(f"Precio más bajo: {precio_mas_bajo}")
    print(f"Precio promedio: {promedio:.2f}")
else:
    print("No se ingresaron precios.")
