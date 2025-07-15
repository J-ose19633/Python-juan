# El slicing (rebanado) permite extraer subcadenas de una cadena.
# Es una operación muy común y poderosa en Python.

mi_cadena = "Python es divertido y poderoso"
print(f"Cadena original: '{mi_cadena}'")

# Sintaxis general: `[inicio:fin:paso]`
# - `inicio`: Índice donde comienza el slice (incluido). Por defecto 0.
# - `fin`: Índice donde termina el slice (excluido). Por defecto len(cadena).
# - `paso`: Incremento entre los índices (por defecto 1).

# Ejemplo 1: Slicing básico (inicio y fin)
subcadena1 = mi_cadena[0:6] # Desde el índice 0 hasta antes del 6
print(f"mi_cadena[0:6]: '{subcadena1}'") # 'Python'

subcadena2 = mi_cadena[7:17] # Desde el índice 7 hasta antes del 17
print(f"mi_cadena[7:17]: '{subcadena2}'") # 'es divertido'

# Ejemplo 2: Slicing con omisión de índices
subcadena3 = mi_cadena[:6] # Desde el inicio hasta antes del 6
print(f"mi_cadena[:6]: '{subcadena3}'") # 'Python'

subcadena4 = mi_cadena[7:] # Desde el índice 7 hasta el final
print(f"mi_cadena[7:]: '{subcadena4}'") # 'es divertido y poderoso'

subcadena5 = mi_cadena[:] # Copia completa de la cadena
print(f"mi_cadena[:]: '{subcadena5}'") # 'Python es divertido y poderoso'

# Ejemplo 3: Slicing con índices negativos
subcadena6 = mi_cadena[-8:] # Últimos 8 caracteres
print(f"mi_cadena[-8:]: '{subcadena6}'") # 'poderoso'

subcadena7 = mi_cadena[7:-9] # Desde el índice 7 hasta 9 caracteres antes del final
print(f"mi_cadena[7:-9]: '{subcadena7}'") # 'es divertido'