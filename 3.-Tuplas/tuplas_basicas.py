# Las tuplas son colecciones ordenadas e inmutables de elementos.
# Una vez creadas, no se pueden modificar (añadir, eliminar o cambiar elementos).
# Se definen usando paréntesis `()`.

# Ejemplo 1: Creación de tuplas
mi_tupla = (1, 2, 3, "cuatro", 5.0)
otra_tupla = "a", "b", "c" # Los paréntesis son opcionales para tuplas simples

# Tupla con un solo elemento (requiere una coma para ser reconocida como tupla)
tupla_un_elemento = ("elemento_unico",)
no_es_tupla = ("solo_string") # Esto es solo un string entre paréntesis

print(f"Mi tupla: {mi_tupla}, Tipo: {type(mi_tupla)}")
print(f"Otra tupla: {otra_tupla}, Tipo: {type(otra_tupla)}")
print(f"Tupla de un elemento: {tupla_un_elemento}, Tipo: {type(tupla_un_elemento)}")
print(f"Esto no es tupla: {no_es_tupla}, Tipo: {type(no_es_tupla)}")

# Ejemplo 2: Acceso a elementos de tuplas (similar a listas)
# Aunque son inmutables, se puede acceder a sus elementos por índice.
print(f"Primer elemento de mi_tupla: {mi_tupla[0]}") # 1
print(f"Último elemento de mi_tupla: {mi_tupla[-1]}") # 5.0

# Desempaquetado de tuplas
# Asigna los elementos de una tupla a variables individuales.
x, y, z = otra_tupla
print(f"Desempaquetado: x={x}, y={y}, z={z}")

# Ejemplo 3: Intentar modificar una tupla (causará un error TypeError)
# try:
#     mi_tupla[0] = 100 # Esto generará un error: 'tuple' object does not support item assignment
# except TypeError as e:
#     print(f"\nError al intentar modificar tupla: {e}")

# Longitud de una tupla
print(f"Longitud de mi_tupla: {len(mi_tupla)}")