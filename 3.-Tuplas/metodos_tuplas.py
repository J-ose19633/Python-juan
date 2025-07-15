# Debido a que las tuplas son inmutables, tienen menos métodos que las listas.
# Solo hay dos métodos integrados para tuplas: `count()` y `index()`.

mi_tupla = (10, 20, 30, 20, 40, 50, 20)
print(f"Tupla original: {mi_tupla}")

# Ejemplo 1: `count()`
# Devuelve el número de veces que un valor específico aparece en la tupla.
conteo_20 = mi_tupla.count(20)
print(f"El número 20 aparece {conteo_20} veces en la tupla.") # Salida: 3

conteo_100 = mi_tupla.count(100)
print(f"El número 100 aparece {conteo_100} veces en la tupla.") # Salida: 0

# Ejemplo 2: `index()`
# Devuelve el índice de la primera aparición del valor especificado.
indice_30 = mi_tupla.index(30)
print(f"El número 30 se encuentra en el índice: {indice_30}") # Salida: 2

# Si el valor no se encuentra, `index()` lanzará un error `ValueError`.
try:
    indice_100 = mi_tupla.index(100)
    print(f"El número 100 se encuentra en el índice: {indice_100}")
except ValueError as e:
    print(f"Error al buscar 100 con index(): {e}")

# Ejemplo 3: Operaciones comunes no-método
# Concatenación de tuplas (crea una nueva tupla, no modifica la original)
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2
print(f"Tupla concatenada: {tupla_concatenada}") # (1, 2, 3, 4)

# Repetición de tuplas
tupla_repetida = tupla1 * 3
print(f"Tupla repetida: {tupla_repetida}") # (1, 2, 1, 2, 1, 2)

# Slicing de tuplas (extrae una porción, crea una nueva tupla)
porcion_tupla = mi_tupla[1:4]
print(f"Porción de tupla (mi_tupla[1:4]): {porcion_tupla}") # (20, 30, 20)