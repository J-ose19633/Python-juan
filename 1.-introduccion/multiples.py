# La asignación múltiple permite asignar varios valores a varias variables en una sola línea.

# Ejemplo 1: Asignación simple de múltiples variables
a, b, c = 10, 20, 30
print(f"a: {a}, b: {b}, c: {c}")

# Ejemplo 2: Intercambiar valores de variables sin usar una variable temporal
x = "Hola"
y = "Mundo"
print(f"Antes del intercambio - x: {x}, y: {y}")
x, y = y, x # Intercambia los valores
print(f"Después del intercambio - x: {x}, y: {y}")

