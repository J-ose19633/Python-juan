# Las condiciones anidadas son estructuras `if`, `elif`, `else` dentro de otras.
# Permiten evaluar condiciones de forma más específica o secuencial.

# Ejemplo 1: Verificación de edad y permiso para conducir
edad = 20
tiene_licencia = True

if edad >= 18:
    print("Eres mayor de edad.")
    if tiene_licencia:
        print("Puedes conducir un coche.")
    else:
        print("Eres mayor de edad, pero necesitas una licencia para conducir.")
else:
    print("Eres menor de edad. No puedes conducir.")

# Ejemplo 2: Acceso a un sistema con roles
usuario_autenticado = True
rol_usuario = "editor" # Puede ser "admin", "editor", "viewer"

if usuario_autenticado:
    print("Usuario autenticado.")
    if rol_usuario == "admin":
        print("Tienes acceso completo al panel de administración.")
    elif rol_usuario == "editor":
        print("Puedes editar y publicar contenido.")
        # Otra condición anidada
        if "premium" in ["basico", "premium"]: # Supongamos una lista de membresías
            print("Además, tienes funciones de editor premium.")
        else:
            print("Eres editor estándar.")
    else:
        print("Tienes acceso de solo lectura (viewer).")
else:
    print("No estás autenticado. Por favor, inicia sesión.")

# Ejemplo 3: Juego simple de adivinanza
numero_secreto = 7
intento_usuario = int(input("Adivina el número (del 1 al 10): "))

if intento_usuario == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print("Lo siento, ese no es el número.")
    if intento_usuario < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    print("Intenta de nuevo.")