# Las listas en Python son colecciones ordenadas y mutables de elementos.
# Pueden contener elementos de diferentes tipos.

# Ejemplo 1: Creación y acceso a elementos de una lista
frutas = ["manzana", "banana", "cereza", "dátil"]
print(f"Lista original de frutas: {frutas}")

# Acceder a elementos por índice (el índice empieza en 0)
print(f"Primera fruta: {frutas[0]}")  # "manzana"
print(f"Tercera fruta: {frutas[2]}")  # "cereza"

# Acceder al último elemento usando índices negativos
print(f"Última fruta: {frutas[-1]}")  # "dátil"

# Ejemplo 2: Longitud de una lista y verificación de existencia
numeros = [10, 20, 30, 40, 50]
print(f"Lista de números: {numeros}")

print(f"Número de elementos en 'numeros': {len(numeros)}") # Salida: 5

# Verificar si un elemento está en la lista
print(f"¿Está 30 en la lista de números? {30 in numeros}")   # Salida: True
print(f"¿Está 100 en la lista de números? {100 in numeros}") # Salida: False

# Ejemplo 3: Listas con tipos de datos mixtos
mezcla = [1, "hola", True, 3.14, None]
print(f"Lista con tipos mixtos: {mezcla}")
print(f"Primer elemento (entero): {mezcla[0]}, Tipo: {type(mezcla[0])}")
print(f"Segundo elemento (string): {mezcla[1]}, Tipo: {type(mezcla[1])}")