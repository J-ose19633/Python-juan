# Las listas anidadas son listas que contienen otras listas como elementos.
# Son útiles para representar estructuras de datos multidimensionales, como matrices o tablas.

# Ejemplo 1: Creación y acceso a elementos en una lista anidada simple
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matriz original:\n{matriz}")

# Acceder a un elemento en una lista anidada: [fila][columna]
# Acceder al 5 (fila 1, columna 1 - índices 0-based)
print(f"Elemento en [1][1]: {matriz[1][1]}") # Salida: 5

# Acceder al 3 (fila 0, columna 2)
print(f"Elemento en [0][2]: {matriz[0][2]}") # Salida: 3

# Ejemplo 2: Iterar sobre una lista anidada
print("\nIterando sobre la matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ") # Imprime cada elemento en la misma línea
    print() # Salto de línea después de cada fila

# Ejemplo 3: Modificar elementos en una lista anidada
matriz_modificable = [
    ["A", "B"],
    ["C", "D"]
]
print(f"\nMatriz antes de modificar: {matriz_modificable}")

# Cambiar 'C' por 'X'
matriz_modificable[1][0] = "X"
print(f"Matriz después de modificar [1][0]: {matriz_modificable}")

# Añadir una nueva fila
matriz_modificable.append(["E", "F"])
print(f"Matriz después de añadir fila: {matriz_modificable}")