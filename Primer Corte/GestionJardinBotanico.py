plantas = {}

while True:
    
    print("\n=== GESTION JARDIN BOTANICO ===")
    print("1 - Registar una planta")
    print("2 - Consultar información de una planta")
    print("3 - Registar un visitante")
    print("4 - Registar una venta")
    print("5 - Calcular mantenimiento")
    print("6 - Generar informe")
    print("8 - Ver plantas por altura")
    print("7 - Salir del programa")
    print("===============================")
    
    try:
        opcion = int(input("Seleccione una opción (1-7): "))
    except ValueError:
        print("Error: ingrese un número válido.")
        continue  

    if opcion == 7:
        print("Saliendo del programa...")
        break
    
    # Funciones
    def registrar_planta():
        nombre = input("Ingrese el nombre de la planta: ")
        tipo = input("Ingrese tipo (árbol, arbusto, flor, planta medicinal, etc.): ").strip().lower()
        edad = input("Ingrese la edad en años: ")
        tamaño = input("Ingrese el tamaño de la planta (en metros): ")
        necesidad_de_riego = input("Ingrese necesidad de riego (diario, interdiario, semanal): ").strip().lower()
        print("Planta registrada exitosamente.")
        
        plantas[nombre] = {
            "tipo": tipo,
            "edad": edad,
            "altura": tamaño,
            "necesidad_de_riego": necesidad_de_riego,
        }
        
    def consultar_informacion():
        nombre = input("Ingrese el nombre de la planta: ").strip().lower()
        if nombre in plantas:
            print("\n=== Información de la Planta ===")
            for clave, valor in plantas[nombre].items():
                print(f"{clave.capitalize()}: {valor}")
            print("===============================")
        else:
           print("La planta no se encuentra registrada.")
        
            
    def registrar_visitante():
        nombre = input("Ingrese el nombre del visitante: ").strip().lower()
        tarifas = {"Adultos": 10, "Niños(menores de 12 años)": 5, "tercera edad(mayores de 60 años)": 7}
        edad = int(input("Ingrese la edad del visitante: "))
        if edad < 12:
            tarifa = tarifas["Niños(menores de 12 años)"]
            print("Tarifa: Niños(menores de 12 años)  $10")
            print(f"Costo de la visita: ${tarifa}")
            print("==Gracias por su visita.==")
            return
        elif edad >= 12 and edad < 60:
            tarifa = tarifas["Adultos"]
            print("Tarifa: Adultos  $10")
            print(f"Costo de la visita: ${tarifa}")
            print("==Gracias por su visita.==")
            return
        elif edad >= 60:
            tarifa = tarifas["tercera edad(mayores de 60 años)"]
            print("Tarifa: Tercera edad(mayores de 60 años)  $7")
            print(f"Costo de la visita: ${tarifa}")
            print("==Gracias por su visita.==")
            return
        else:
            print("Error: Edad no válida.")
            
    #Si quiero agregar varios sitantes y sumar el total 
    
        
        
               
    def registar_venta(): # quiero agregar un print para mostar llas palntas dipispoibles para compra en forma de lista 
        nombre = input("Ingrese el nombre de la planta: ")
        if nombre in plantas:
            print(f"Precio de venta: {plantas[nombre]['precio_venta']}")
        else:
            print("La planta no se encuentra registrada.")
     
    if opcion == 1:
        registrar_planta()
    if opcion == 2:
        consultar_informacion()  
    if opcion == 3:
        registrar_visitante()
    if opcion == 4:
        registrar_visitante()
        
    
    

    
    