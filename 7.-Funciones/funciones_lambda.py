# Las funciones lambda (también llamadas funciones anónimas) son pequeñas funciones
# que se definen con la palabra clave `lambda`. Son útiles para tareas cortas
# y sencillas, a menudo usadas como argumentos para funciones de orden superior.

# Sintaxis: `lambda argumentos: expresion`

# Ejemplo 1: Lambda básica para sumar dos números
sumar = lambda a, b: a + b
print(f"Suma de 5 y 3 (lambda): {sumar(5, 3)}") # Salida: 8

# Lambda para el cuadrado de un número
cuadrado = lambda x: x * x
print(f"Cuadrado de 7 (lambda): {cuadrado(7)}") # Salida: 49

# Ejemplo 2: Usando lambda con `filter()`
# `filter()` toma una función (condición) y un iterable, y devuelve los elementos que cumplen la condición.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares (usando filter y lambda): {pares}") # Salida: [2, 4, 6, 8, 10]

# Ejemplo 3: Usando lambda con `map()`
# `map()` toma una función y un iterable, y aplica la función a cada elemento, devolviendo los resultados.
dobles = list(map(lambda x: x * 2, numeros))
print(f"Dobles de los números (usando map y lambda): {dobles}") # Salida: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

