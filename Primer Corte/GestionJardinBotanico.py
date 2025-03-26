#listas y dicionario aplicados en el sistema 
plantas = {}
visitantes = []
ventas = []

#Funciones aplicadas
def registrar_planta():
    nombre = input("Ingrese el nombre de la planta: ").strip().lower()
    tipo = input("Ingrese tipo (árbol, arbusto, flor, planta medicinal, etc.): ").strip().lower()
    
    while True:
        try:
            edad = int(input("Ingrese la edad en años: "))
            tamaño = float(input("Ingrese el tamaño de la planta (en metros): "))
            break
        except ValueError:
            print("Error: Ingrese valores numéricos para edad y tamaño.")

    necesidad_de_riego = input("Ingrese necesidad de riego (diario, interdiario, semanal): ").strip().lower()
    precio_venta = float(input("Ingrese el precio de venta de la planta: "))

    plantas[nombre] = {
        "tipo": tipo,
        "edad": edad,
        "altura": tamaño,
        "necesidad_de_riego": necesidad_de_riego,
        "precio_venta": precio_venta,
    }
    
    print(f"Planta '{nombre}' registrada exitosamente.")

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
    total_ingresos = 0
    while True:
        nombre = input("Ingrese el nombre del visitante (o 'salir' para finalizar): ").strip()
        if nombre.lower() == 'salir':
            break

        tarifas = {"Adultos": 10, "Niños": 5, "Tercera Edad": 7}
        
        try:
            edad = int(input("Ingrese la edad del visitante: "))
        except ValueError:
            print("Error: Ingrese un número válido para la edad.")
            continue

        if edad < 12:
            tarifa = tarifas["Niños"]
            categoria = "Niños"
        elif edad >= 12 and edad < 60:
            tarifa = tarifas["Adultos"]
            categoria = "Adultos"
        else:
            tarifa = tarifas["Tercera Edad"]
            categoria = "Tercera Edad"

        visitantes.append({"nombre": nombre, "edad": edad, "categoria": categoria, "tarifa": tarifa})
        total_ingresos += tarifa

        print(f"Categoría: {categoria} - Tarifa: ${tarifa}")
        print(f"==Gracias por su visita, {nombre}.==")

    print(f"\nTotal de ingresos por visitantes: ${total_ingresos}")

def registrar_venta():
    if not plantas:
        print("No hay plantas registradas para la venta.")
        return

    print("\n=== Plantas Disponibles para Venta ===")
    for nombre, datos in plantas.items():
        print(f"- {nombre.capitalize()} (Precio: ${datos['precio_venta']})")
    
    nombre = input("\nIngrese el nombre de la planta que desea comprar: ").strip().lower()
    
    if nombre in plantas:
        ventas.append(nombre)
        print(f"Venta registrada: {nombre.capitalize()} por ${plantas[nombre]['precio_venta']}")
    else:
        print("La planta no se encuentra registrada.")

def calcular_mantenimiento():
    if not plantas:
        print("No hay plantas registradas.")
        return

    total_costo = 0
    costos_riego = {"diario": 5, "interdiario": 3, "semanal": 1}
    
    for nombre, datos in plantas.items():
        costo_riego = costos_riego.get(datos["necesidad_de_riego"], 0)
        total_costo += costo_riego

    print(f"\nEl costo total de mantenimiento del jardín es: ${total_costo}")

def generar_informe():
    print("\n=== INFORME DEL JARDÍN BOTÁNICO ===")
    print(f"Total de plantas registradas: {len(plantas)}")
    print(f"Total de visitantes: {len(visitantes)}")
    print(f"Total de ventas realizadas: {len(ventas)}")
    calcular_mantenimiento()
    print("===================================")

# Bucle del menú
while True:
    print("\n=== GESTIÓN JARDÍN BOTÁNICO ===")
    print("1 - Registrar una planta")
    print("2 - Consultar información de una planta")
    print("3 - Registrar un visitante")
    print("4 - Registrar una venta")
    print("5 - Calcular mantenimiento")
    print("6 - Generar informe")
    print("7 - Salir del programa")
    print("===============================")

    try:
        opcion = int(input("Seleccione una opción (1-7): "))
    except ValueError:
        print("Error: ingrese un número válido.")
        continue  

    if opcion == 1:
        registrar_planta()
    elif opcion == 2:
        consultar_informacion()
    elif opcion == 3:
        registrar_visitante()
    elif opcion == 4:
        registrar_venta()
    elif opcion == 5:
        calcular_mantenimiento()
    elif opcion == 6:
        generar_informe()
    elif opcion == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Error: opción no válida. Intente de nuevo.")

        