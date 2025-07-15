# Las cadenas en Python son secuencias, lo que significa que puedes acceder
# a sus caracteres individuales usando índices.

mi_cadena = "Programacion"
print(f"Cadena original: '{mi_cadena}'")

# Ejemplo 1: Acceso a caracteres por índice positivo
# Los índices comienzan en 0 para el primer carácter.
print(f"Primer carácter (indice 0): {mi_cadena[0]}")  # 'P'
print(f"Quinto carácter (indice 4): {mi_cadena[4]}")  # 'r'

# Ejemplo 2: Acceso a caracteres por índice negativo
# Los índices negativos cuentan desde el final de la cadena.
# -1 es el último carácter, -2 el penúltimo, etc.
print(f"Último carácter (indice -1): {mi_cadena[-1]}")   # 'n'
print(f"Tercer carácter desde el final (indice -3): {mi_cadena[-3]}") # 'i'

# Ejemplo 3: Inmutabilidad de las cadenas
# No se puede modificar un carácter individual de una cadena directamente.
# Si intentas hacerlo, obtendrás un `TypeError`.
# try:
#     mi_cadena[0] = 'p' # Esto causará un error: 'str' object does not support item assignment
# except TypeError as e:
#     print(f"\nError al intentar modificar un carácter de la cadena: {e}")

# Para "modificar" una cadena, debes crear una nueva cadena basada en la original.
nueva_cadena = "p" + mi_cadena[1:]
print(f"Nueva cadena (modificada): '{nueva_cadena}'") # 'programacion'