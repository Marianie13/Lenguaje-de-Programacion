"""
    Ejercicio 3: 
    Registro de Estudiantes en una Universidad Desarrolla un programa que permita ingresar los nombres de los estudiantes de una universidad hasta que el usuario decida terminar. 
    Luego, muestra en pantalla la cantidad total de estudiantes registrados.
"""
# Inicializar lista de estudiantes
estudiantes = []

# Bucle para registrar estudiantes hasta que ingrese la para fin paara salir del bluque
while True:
    nombre = input("Ingrese el nombre del estudiante (o escriba 'fin' para terminar): ").strip()#.strip elimina espacios para que no se generen errores
    if nombre.lower() == "fin":
        break
    estudiantes.append(nombre)

# Mostrar la cantidad total de estudiantes registrados
print(f"\nTotal de estudiantes registrados: {len(estudiantes)}")