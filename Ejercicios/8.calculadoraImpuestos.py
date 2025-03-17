# Calculadora Impuestos
"""
Ejercicio 8: 
Calculadora de Impuestos Pide al usuario su salario mensual y, 
en función del monto, calcula el impuesto que debe pagar según la siguiente tabla: 
Menos de $1.500.000 → No paga impuestos Entre $1.500.000 y $3.000.000 → 10% de impuestos 
Más de $3.000.000 → 20% de impuestos Muestra el monto del impuesto a pagar.
"""

# primero pediremos al usuario que ingrese el salario

while True:

    print("CALCULADORA DE IMPUESTO")
    print("1. Calcular impuesto")
    print("2. Salir")
    
    opcion = int(input("digite la opcion: "))
    if opcion == 1:
        salario = float(input("Ingresa el valor de tu salario: "))
        if salario < 1500000:
            print("No debes pagar impuestos")
            
# Generamos una condicion para cada caso y mostramos el resultado.

        elif 1500000 <= salario < 3000000:
            impuesto = salario * 0.1
            print(f"Debes pagar impuesto de 10% que corresponde a {impuesto} pesos")
        elif salario >= 3000000:
            impuesto = salario * 0.2
            print(f"Debes pagar impuesto de 20% que corresponde a {impuesto} pesos")
    elif opcion == 2:
        print("Saliendo del sistema")
        break
    else:
        print("Opcion no valida")
        
