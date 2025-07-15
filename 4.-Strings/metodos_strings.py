# Las cadenas (strings) en Python tienen muchos métodos útiles para su manipulación.
# Las cadenas son inmutables, por lo que estos métodos devuelven nuevas cadenas, no modifican la original.

mi_cadena = "  Hola Mundo PYTHON.  "
print(f"Cadena original: '{mi_cadena}'")

# Ejemplo 1: Modificación de mayúsculas/minúsculas y espacios
# `lower()`: Convierte toda la cadena a minúsculas.
print(f"lower(): '{mi_cadena.lower()}'") # '  hola mundo python.  '

# `upper()`: Convierte toda la cadena a mayúsculas.
print(f"upper(): '{mi_cadena.upper()}'") # '  HOLA MUNDO PYTHON.  '

# `strip()`: Elimina espacios en blanco (o caracteres específicos) al inicio y final.
print(f"strip(): '{mi_cadena.strip()}'") # 'Hola Mundo PYTHON.'

# `replace(old, new)`: Reemplaza todas las ocurrencias de una subcadena por otra.
nueva_cadena = mi_cadena.replace("PYTHON", "Python")
print(f"replace('PYTHON', 'Python'): '{nueva_cadena}'") # '  Hola Mundo Python.  '

