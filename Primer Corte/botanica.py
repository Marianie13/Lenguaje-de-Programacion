# Diccionarios de plantas
plantas = {}
plantas_ornamentales = {
    "Rosa": {"riego": 1, "poda": 3, "fumigación": 5},
    "Margarita": {"riego": 1, "poda": 3, "fumigación": 5},
    "Helecho": {"riego": 1, "poda": 3, "fumigación": 5},   
}
arboles = {
    "Roble": {"riego": 1, "poda": 3, "fumigación": 5},
    "Pino": {"riego": 1, "poda": 3, "fumigación": 5},
    "Bambu": {"riego": 1, "poda": 3, "fumigación": 5},   
}
plantas_medicinales = {
    "Manzanilla": {"riego": 1, "poda": 3, "fumigación": 5},
    "Romero": {"riego": 1, "poda": 3, "fumigación": 5},
    "Lavanda": {"riego": 1, "poda": 3, "fumigación": 5},
}

# Función para registrar una planta
def registrar_planta():
    nombre = input("Ingrese el nombre de la planta: ").strip()
    tipo = input("Ingrese tipo (árbol, arbusto, flor, medicinal, etc.): ").strip().lower()
    edad = input("Ingrese la edad en años: ")
    tamaño = input("Ingrese el tamaño de la planta (en metros): ")
    necesidad_de_riego = input("Ingrese necesidad de riego (diario, interdiario, semanal): ").strip().lower()
    
    plantas[nombre] = {
        "tipo": tipo,
        "edad": edad,
        "altura": tamaño,
        "necesidad_de_riego": necesidad_de_riego,
        "precio_venta": 0,  # Inicializa precio de venta
        "mantenimiento": 0  # Inicializa costo de mantenimiento
    }
    print(f"✅ Planta '{nombre}' registrada exitosamente.")

# Función para consultar información de una planta
def consultar_informacion():
    nombre = input("Ingrese el nombre de la planta: ").strip()
    if nombre in plantas:
        print("\n=== Información de la Planta ===")
        for clave, valor in plantas[nombre].items():
            print(f"{clave.capitalize()}: {valor}")
        print("===============================")
    else:
        print("❌ La planta no se encuentra registrada.")

# Función para registrar un visitante
def registrar_visitante():
    nombre = input("Ingrese el nombre del visitante: ").strip()
    edad = int(input("Ingrese la edad del visitante: "))

    tarifas = {"Adultos": 10, "Niños": 5, "Tercera Edad": 7}

    if edad < 12:
        tarifa = tarifas["Niños"]
        categoria = "Niños (menores de 12 años)"
    elif edad < 60:
        tarifa = tarifas["Adultos"]
        categoria = "Adultos"
    else:
        tarifa = tarifas["Tercera Edad"]
        categoria = "Tercera edad (mayores de 60 años)"

    print(f"✅ Categoría: {categoria} - Costo de la visita: ${tarifa}")
    print("== Gracias por su visita. ==")

# Función para registrar una venta
def registrar_venta():
    if not plantas:
        print("❌ No hay plantas disponibles para la venta.")
        return

    print("\n=== Plantas Disponibles para Venta ===")
    for nombre, detalles in plantas.items():
        print(f"{nombre} - Precio: ${detalles['precio_venta']}")
    print("==============================")

    nombre = input("Ingrese el nombre de la planta vendida: ").strip()
    if nombre in plantas:
        plantas[nombre]['precio_venta'] = float(input(f"Ingrese el precio de venta de {nombre}: "))
        print(f"✅ Venta de '{nombre}' registrada exitosamente.")
    else:
        print("❌ Planta no encontrada.")

# Función para calcular mantenimiento
def calcular_mantenimiento():
    if not plantas:
        print("❌ No hay plantas disponibles para mantenimiento.")
        return

    print("\n=== Plantas Disponibles para Mantenimiento ===")
    for nombre, detalles in plantas.items():
        print(f"{nombre} - Costo mantenimiento: ${detalles['mantenimiento']}")
    print("==============================")

    nombre = input("Ingrese el nombre de la planta para mantenimiento: ").strip()
    if nombre in plantas:
        plantas[nombre]['mantenimiento'] = float(input(f"Ingrese el costo de mantenimiento de {nombre}: "))
        print(f"✅ Mantenimiento de '{nombre}' registrado exitosamente.")
    else:
        print("❌ Planta no encontrada.")

# Bucle del menú
while True:
    print("\n=== GESTIÓN JARDÍN BOTÁNICO ===")
    print("1 - Registrar una planta")
    print("2 - Consultar información de una planta")
    print("3 - Registrar un visitante")
    print("4 - Registrar una venta")
    print("5 - Calcular mantenimiento")
    print("6 - Generar informe (pendiente)")
    print("7 - Salir")
    print("===============================")

    try:
        opcion = int(input("Seleccione una opción (1-7): "))
    except ValueError:
        print("❌ Error: ingrese un número válido.")
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
        print("📊 Generar informe aún no está implementado.")
    elif opcion == 7:
        print("👋 Saliendo del programa...")
        break
    else:
        print("❌ Opción no válida. Intente de nuevo.")
