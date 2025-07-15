# Aunque las tuplas son inmutables, sus elementos individuales se pueden acceder
# de manera similar a las listas, utilizando indexado y slicing.

mi_tupla = ("rojo", "verde", "azul", "amarillo", "morado")
print(f"Tupla original: {mi_tupla}")

# Ejemplo: Acceso a elementos individuales por índice
# Los índices comienzan en 0 para el primer elemento.
print(f"Primer elemento: {mi_tupla[0]}")  # "rojo"
print(f"Tercer elemento: {mi_tupla[2]}")  # "azul"

# Índices negativos: -1 se refiere al último elemento, -2 al penúltimo, etc.
print(f"Último elemento: {mi_tupla[-1]}")   # "morado"
print(f"Penúltimo elemento: {mi_tupla[-2]}") # "amarillo"

