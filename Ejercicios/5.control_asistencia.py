"""
     Ejercicio 5: 
     Control de Asistencia en una Universidad Crea un programa 
     que solicite la cantidad de estudiantes en un curso y luego, usando un ciclo for, pida al usuario ingresar si cada estudiante asistió o no (A para asistió, F para faltó).
     Al final, muestra cuántos estudiantes asistieron y cuántos faltaron.
    
"""
# Solicitar la cantidad de estudiantes en el curso
num_estudiantes = int(input("Ingrese la cantidad de estudiantes en el curso: "))

# Inicializar contadores
asistieron = 0
faltaron = 0

# Ciclo para registrar asistencia
for i in range(1, num_estudiantes + 1):
    asistencia = input(f"Estudiante {i} (A para asistió, F para faltó): ").strip().upper() #strip quita los espacios y upper converte la primera eltra en mayuscula
    
    if asistencia == "A":
        asistieron += 1
    elif asistencia == "F":
        faltaron += 1
    else:
        print("Entrada no válida. Intente de nuevo.")
        i -= 1  # Repetir la entrada para este estudiante

# Mostrar resultados
print(f"\nTotal de estudiantes que asistieron: {asistieron}")
print(f"Total de estudiantes que faltaron: {faltaron}")
