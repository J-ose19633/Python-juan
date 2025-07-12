# Python proporciona varios métodos integrados para manipular listas.

mi_lista = [10, 20, 30, 40, 50]
print(f"Lista inicial: {mi_lista}")

# Ejemplo 1: `append()`, `insert()`, `extend()`
# `append()`: Añade un elemento al final de la lista.
mi_lista.append(60)
print(f"Después de append(60): {mi_lista}") # [10, 20, 30, 40, 50, 60]

# `insert(indice, elemento)`: Inserta un elemento en una posición específica.
mi_lista.insert(0, 5) # Inserta 5 en el índice 0
print(f"Después de insert(0, 5): {mi_lista}") # [5, 10, 20, 30, 40, 50, 60]

# `extend(iterable)`: Añade los elementos de otro iterable (lista, tupla, etc.) al final.
otra_lista = [70, 80]
mi_lista.extend(otra_lista)
print(f"Después de extend([70, 80]): {mi_lista}") # [5, 10, 20, 30, 40, 50, 60, 70, 80]

