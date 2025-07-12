# Recorrer o iterar una lista significa acceder a cada uno de sus elementos.
# Esto se puede hacer de varias maneras en Python.

# Ejemplo 1: Recorrido básico con un bucle `for`
frutas = ["manzana", "banana", "cereza", "dátil"]
print("Recorriendo la lista de frutas con for:")
for fruta in frutas:
    print(f"- {fruta}")

# Ejemplo 2: Recorrido con `for` y `range(len())` para acceder al índice
numeros = [10, 20, 30, 40, 50]
print("\nRecorriendo la lista de números con for y rango de índices:")
for i in range(len(numeros)):
    print(f"Elemento en índice {i}: {numeros[i]}")

# Ejemplo 3: Recorrido con `enumerate()` para obtener índice y valor
colores = ["rojo", "verde", "azul"]
print("\nRecorriendo la lista de colores con enumerate():")
for indice, color in enumerate(colores):
    print(f"El color '{color}' está en el índice {indice}")

