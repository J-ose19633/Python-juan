# Los operadores lógicos (`and`, `or`, `not`) se utilizan para combinar
# o modificar expresiones condicionales, permitiendo construir condiciones más complejas.

# Ejemplo 1: Operador `and` (ambas condiciones deben ser verdaderas)
# Se usa cuando todas las condiciones deben cumplirse.
edad = 25
ingresos = 30000

if edad >= 18 and ingresos >= 25000:
    print("Cumples los requisitos para el préstamo.")
else:
    print("No cumples los requisitos para el préstamo.")

# Ejemplo 2: Operador `or` (al menos una condición debe ser verdadera)
# Se usa cuando basta con que una de las condiciones se cumpla.
temperatura = 28
hay_sol = True
plan = ""

if temperatura > 25 or hay_sol:
    plan = "Ir a la playa o al parque."
else:
    plan = "Quedarse en casa."
print(f"Plan para hoy: {plan}")

# Ejemplo 3: Operador `not` (niega una condición)
# Invierte el valor booleano de una expresión. `True` se convierte en `False` y viceversa.
saldo_cero = False
usuario_activo = True

if not saldo_cero and usuario_activo:
    print("La cuenta tiene saldo y el usuario está activo.")
else:
    print("La cuenta está en cero o el usuario está inactivo.")

