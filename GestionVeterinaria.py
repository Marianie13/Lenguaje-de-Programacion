
while True:
    print("\n---MENU GESTION DE VERINARIA---")
    print("1. Registrar Mascota")
    print("2. Agedar una cita veterinaria")
    print("3. Calcular el costo del servicio")
    print("4. Salir del programa")
    
    try: 
        opcion = int(input("ingrese una opción (1-4): "))
    except ValueError:
        print("Error ingrese numero Válido. ")
        continue