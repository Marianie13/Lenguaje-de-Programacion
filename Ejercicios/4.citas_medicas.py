"""
     Ejercicio 4: 
     Citas Médicas en una Clínica Simula un sistema de turnos en una clínica. 
     El programa debe permitir que un usuario ingrese su nombre y especialidad médica requerida. 
     Se debe mostrar un número de turno único para cada paciente. 
     Usa un ciclo while para seguir registrando pacientes hasta que el usuario indique que no desea continuar.
    
"""
turno = 1  # Inicializamos el número de turno

#Usamos el ciclo while hasta que el usuario descida salir 
while True:
    nombre = input("Ingrese su nombre: ")
    especialidad = input("Ingrese la cita médica requerida: ")
    
    print(f"\nPaciente: {nombre}")
    print(f"Especialidad: {especialidad}")
    print(f"Su número de turno es: {turno}\n")
    
    turno += 1  # Incrementamos el número de turno para el siguiente paciente

    continuar = input("¿Desea registrar otro paciente? (si/no): ").strip().lower()
    if continuar != "si":
        print("Registro terminado")
        break
