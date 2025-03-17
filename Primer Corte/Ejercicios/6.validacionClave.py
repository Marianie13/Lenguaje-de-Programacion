# Validacion clave
"""
Ejercicio 6: 
Validación de Claves en un Cajero Automático Simula un sistema de cajero automático que 
solicite una clave de 4 dígitos. Si el usuario ingresa la clave incorrecta 3 veces seguidas, 
el programa debe mostrar un mensaje indicando que la tarjeta ha sido bloqueada.
"""
# Primero pediremos al usuario que cree una contraseña.

# Establecemos un menú de opciones para que sea un poco mas dinámico. 

while True:
    print("BIENVENIDO AL CAJERO AUTOMATICO")
    print("1. Crear contraseña")
    print("2. Ingresar contraseña")
    print("3. Salir")

    opcion = int(input("Digite la opcion: "))
   
    if opcion == 1:
        contrasena = int(input("Crea tu contraseña nueva de 4 numeros: "))
        intento = 0

# Esta opcion está para que el usuario ingrese/verifique su contraseña.
    elif opcion == 2:
        for intento in range(3):
            validar = int(input("Ingresa tu contraseña de 4 numeros: "))
# Muestra el resultado.
            if validar == contrasena:
                print("Contraseña correcta, bienvenido.")
                break
            else:
                print(f"Contraseña incorrecta, te quedan: {2 - intento} intentos.")
        if intento == 3:
                print("Tu tarjeta ha sido bloqueda")
                exit()
    elif opcion == 3:
        print ("Sistema finalizado")
        break
    else:
        print("Opcion no valida")




