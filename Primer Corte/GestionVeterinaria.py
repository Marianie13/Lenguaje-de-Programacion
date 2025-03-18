
import webbrowser # Se incorporo para poder dar acceso aun link 
from tabulate import tabulate # Para mejorar la visualización de tablas 

# Diccionarios para almacenar datos de mascotas y citas
datos_mascotas = {}
citas = []

# Menú principal
while True:
    print("\n=== MENU GESTION DE VETERINARIA ===")
    print("1. Registrar mascota")
    print("2. Mostrar mascotas registradas")
    print("3. Agendar una cita veterinaria")
    print("4. Calcular el costo del servicio")
    print("5. Mostrar historial de una mascota")
    print("6. Mostrar lenguajes de programación")
    print("7. Salir del programa")
    
    try: 
        opcion = int(input("Ingrese una opción (1-7): "))
    except ValueError:
        print("Error: ingrese un número válido.")
        continue

    if opcion == 7:
        print("Saliendo del programa...")
        break

    # Funciones
    def registrar_mascota():
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese la especie (gato, perro, conejo, etc.): ")
        edad = input("Ingrese la edad de la mascota: ")
        dueno = input("Ingrese el nombre del dueño: ")
        datos_mascotas[nombre] = {
            "especie": especie,
            "edad": edad,
            "dueño": dueno,
            "historial": []  # Historial vacío al registrar la mascota
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
        tipo = input("Ingrese el tipo de consulta:(vacunación, desparasitación, chequeo general): ").lower()
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
        info = datos_mascotas[nombre]
        print(f"\n=== Historial de {nombre} ===")
        print(f"Especie: {info['especie']}, Edad: {info['edad']}, Dueño: {info['dueño']}")
        historial = info["historial"]
        if not historial:
            print("No hay historial de consultas para esta mascota.")
        else:
            for consulta in historial:
                print(f"Fecha: {consulta['fecha']}, Tipo: {consulta['tipo']}")
                
# Se agrega esta función para poder mostrar la otra parte del ejercicio de investigación
    def mostrar_lenguajes():
        print("""
=== Lenguajes de Programación de Alto Nivel ===

Introducción:
Los lenguajes de programación de alto nivel permiten a los desarrolladores escribir código con una sintaxis más comprensible y 
cercana al lenguaje humano. Son independientes del hardware y ofrecen una mayor abstracción en la programación.
""")

        print("""
Características de los Lenguajes de Alto Nivel:
- Legibles y fáciles de entender: Su sintaxis se asemeja al lenguaje humano.
- Independientes del hardware: No están ligados a una arquitectura específica de computadora.
- Manejo automático de memoria: Muchos incluyen garbage collection para administrar la memoria automáticamente.
- Uso de estructuras de alto nivel: Soportan funciones, clases, módulos y estructuras de datos avanzadas.
- Portabilidad: Pueden ejecutarse en diferentes sistemas operativos sin grandes modificaciones.
""")

        tabla = [
            ["Python", "Imperativo, Orientado a Objetos, Funcional", "IA, Ciencia de Datos, Desarrollo Web"],
            ["Java", "Orientado a Objetos", "Aplicaciones empresariales, Android"],
            ["C#", "Orientado a Objetos", "Videojuegos (Unity), Aplicaciones de escritorio"],
            ["JavaScript", "Imperativo, Funcional", "Desarrollo Web, Frontend y Backend"],
            ["Ruby", "Orientado a Objetos", "Desarrollo Web (Ruby on Rails)"],
            ["Swift", "Orientado a Objetos, Funcional", "Desarrollo para iOS y macOS"],
            ["PHP", "Imperativo, Orientado a Objetos", "Desarrollo Web Backend"]
        ]

        print("\n=== Tabla Comparativa de Lenguajes de Alto Nivel ===")
        print(tabulate(tabla, headers=["Lenguaje", "Paradigma", "Usos Principales"], tablefmt="grid"))

        respuesta = input("\n¿Desea visitar un ejemplo de desarrollo avanzado en la web? (s/n): ").lower()
        if respuesta == "s":
            webbrowser.open("https://lusion.co/")

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
        mostrar_lenguajes()
    else:
        print("Opción no válida, intente nuevamente.")