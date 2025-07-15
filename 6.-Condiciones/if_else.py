# La estructura `if-else` permite ejecutar un bloque de código si una condición es verdadera,
# y otro bloque de código diferente si la condición es falsa.

# Ejemplo 1: Determinar si un número es par o impar
numero = 7

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Ejemplo 2: Validar acceso según una contraseña
contrasena_guardada = "secreto123"
contrasena_ingresada = input("Introduce la contraseña: ")

if contrasena_ingresada == contrasena_guardada:
    print("Acceso concedido. ¡Bienvenido!")
else:
    print("Contraseña incorrecta. Acceso denegado.")

# Ejemplo 3: Decidir una acción basada en el estado de un interruptor
luz_encendida = False

if luz_encendida:
    print("La luz está encendida.")
    print("Puedes apagarla.")
else:
    print("La luz está apagada.")
    print("Puedes encenderla.")

print("Fin de la verificación de la luz.")