# Pacientes Clinica
"""
Ejercicio 9: 
Búsqueda de Pacientes en una Clínica Crea un programa que almacene los nombres de 
10 pacientes en una lista. Luego, pide al usuario que ingrese un nombre y verifica 
si el paciente está en la lista. Usa un ciclo for y una estructura condicional para 
la búsqueda.
"""
# Primero mostraremos un menú de opciones para el usuario
pacientes = []

while True:
    print("GESTION PACIENTES")
    print("1. Ingrese el nombre del paciente")
    print("2. Buscar paciente")
    print("3. Salir")

    opcion = int(input("digite la opcion: "))

    if opcion == 1:
        if len(pacientes) < 10:
            for _ in range(10 - len(pacientes)):
                paciente = input("Ingresa el nombre del paciente: ")
                pacientes.append(paciente)
            print("Lista completa. Ahora puedes buscar pacientes.")
        else:
            print("Memoria llena")
    elif opcion == 2:
        nombre = input("Ingresa el nombre del paciente a verificar: ").lower()
        encontrado = False #Esta variable surje para saber si encontramos al paciente

        for paciente in pacientes:
            if nombre == paciente.lower():
                encontrado = True
                break
        if encontrado:
            print(f"El paciente {nombre}, está en la lista")
        else:
            print(f"{nombre} no está en la lista") 
    elif opcion == 3:
        print("Salir del sistema")
        break
    else:
        print("Opcion no valida.")

