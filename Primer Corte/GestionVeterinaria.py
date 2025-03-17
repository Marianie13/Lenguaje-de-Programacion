datos_mascotas ={}

while True:
    print("\n===MENU GESTION DE VERINARIA===")
    print("1. Registrar Mascota")
    print("2. Agedar una cita veterinaria")
    print("3. Calcular el costo del servicio")
    print("4. Salir del programa")
    
    try: 
        opcion = int(input("ingrese una opción (1-4): "))
    except ValueError:
        print("Error ingrese numero Válido. ")
        continue
    
    def registar_mascota():
        nombre = input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese la especie(gato, perro, conejo, etc.): ")
        edad = input("Ingrese la edad de la mascota: ")
        dueno = input("Ingrese el nombre del dueño: ")
        datos_mascotas[nombre] = {"especie": especie, "edad": edad, "dueño": dueno}
        print("Mascota registarda exitosamente")
        
        
        