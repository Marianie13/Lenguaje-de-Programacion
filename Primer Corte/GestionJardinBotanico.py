plantas = {}

while True:
    print("\n=== GESTION JARDIN BOTANICO ===")
    print("1. Registar una planta")
    print("2. Consultar información de una planta")
    print("3. Registar un visitante")
    print("4. Registar una venta")
    print("5. Calcular mantenimiento")
    print("6. Calcular mantenimiento")
    print("7. Salir del programa")
    
    try: 
        opcion = int(input("Ingrese una opción (1-7)"))
    except ValueError:
        print("Error: ingrese un número válido.")
        continue
    
    if opcion == 7:
        print("Saliendo del programa...")
        break
    
    # Funciones
    def registrar_planta():
        nombre = input("Ingrese el nombre de la planta: ")
        especie = input("Ingrese la especie de la planta: ")
        altura = input("Ingrese la altura de la planta (en metros): ")
        propietario = input("Ingrese el nombre del propietario: ")
        print("Planta registrada exitosamente.")
        
    def consultar_informacion():
        nombre = input("Ingrese el nombre de la planta: ")
        if nombre in plantas:
            print(f"Nombre: {plantas[nombre]['nombre']}, Especie: {plantas[nombre]['especie']}, Altura: {plantas[nombre]['altura']} metros, Propietario: {plantas[nombre]['propietario']}")
        else:
            print("La planta no se encuentra registrada.")
            
    def registrar_visitante():
        nombre = input("Ingrese el nombre del visitante: ")
        telefono = input("Ingrese el número de teléfono del visitante: ")
        print("Visitante registrado exitosamente.")
        
        # Aca me hace faltaural el total de la costo delvisitante depeniendo de la edad
        # y el tipo de visita (entrada o salida)
        """
        costo_visitante = 0
        print(f"Costo del visitante: {costo_visitante}")
        """
    def registar_venta(): # quiero agregar un print para mostar llas palntas dipispoibles para compra en forma de lista 
        nombre = input("Ingrese el nombre de la planta: ")
        if nombre in plantas:
            print(f"Precio de venta: {plantas[nombre]['precio_venta']}")
        else:
            print("La planta no se encuentra registrada.")
     
       
    
    

    
    