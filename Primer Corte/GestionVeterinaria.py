datos_mascotas = {}
citas = []

while True:
    print("\n=== MENU GESTION DE VETERINARIA ===")
    print("1. Registrar mascota")
    print("2. Mostrar mascotas registradas")
    print("3. Agendar una cita veterinaria")
    print("4. Calcular el costo del servicio")
    print("5. Mostrar historial de una mascota")
    print("6. Salir del programa")
    
    try: 
        opcion = int(input("Ingrese una opción (1-6): "))
    except ValueError:
        print("Error: ingrese un número válido.")
        continue
    
    def registrar_mascota():
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese la especie (gato, perro, conejo, etc.): ")
        edad = input("Ingrese la edad de la mascota: ")
        dueno = input("Ingrese el nombre del dueño: ")
        datos_mascotas[nombre] = {
            "especie": especie,
            "edad": edad,
            "dueño": dueno,
            "historial": []  # Se agrega historial vacío al registrar la mascota
        }
        print("Mascota registrada exitosamente.")

    def mostrar_mascotas():
        if not datos_mascotas:
            print("No hay mascotas registradas.")
            return
        print("\n=== Mascotas Registradas ===")
        for nombre, info in datos_mascotas.items():
            print(f"Nombre: {nombre}, Especie: {info['especie']}, Edad: {info['edad']}, Dueño: {info['dueño']}")

    def agendar_cita():
        nombre = input("Ingresar nombre de la mascota: ")
        if nombre not in datos_mascotas:
            print("La mascota no está registrada, por favor regístrela primero.")
            return
        tipo = input("Ingrese el tipo de consulta (vacunación, desparasitación, chequeo general): ").lower()
        fecha = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
        cita = {"mascota": nombre, "tipo": tipo, "fecha": fecha}
        citas.append(cita)
        datos_mascotas[nombre]["historial"].append(cita)  # Se agrega al historial
        print("Cita agendada exitosamente.")

    def calcular_servicio():
        tarifas = {"vacunación": 30, "desparasitación": 25, "chequeo general": 40}
        tipo = input("Ingrese el tipo de consulta: ").lower()
        costo = tarifas.get(tipo, None)
        if costo is not None:
            print(f"El costo del servicio de {tipo} es: ${costo}")
        else:
            print("Tipo de consulta errónea, intente de nuevo.")

    def mostrar_historial():
        nombre = input("Ingrese el nombre de la mascota: ")
        if nombre not in datos_mascotas:
            print("La mascota no está registrada.")
            return
        historial = datos_mascotas[nombre]["historial"]
        if not historial:
            print("No hay historial de consultas para esta mascota.")
        else:
            print(f"\n=== Historial de {nombre} ===")
            for consulta in historial:
                print(f"Fecha: {consulta['fecha']}, Tipo: {consulta['tipo']}")

    if opcion == 1:
        registrar_mascota()
    elif opcion == 2:
        mostrar_mascotas()
    elif opcion == 3:
        agendar_cita()
    elif opcion == 4:
        calcular_servicio()
    elif opcion == 5:
        mostrar_historial()
    elif opcion == 6:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente nuevamente.")
