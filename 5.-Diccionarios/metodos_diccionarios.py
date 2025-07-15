# Los diccionarios en Python tienen varios métodos útiles para manipular sus elementos.

mi_diccionario = {
    "nombre": "David",
    "edad": 40,
    "ciudad": "Valencia"
}
print(f"Diccionario inicial: {mi_diccionario}")

# Ejemplo 1: `update()`
# Fusiona otro diccionario o iterable de pares clave-valor en el diccionario actual.
# Si una clave existe, su valor se actualiza; si no, se añade.
mi_diccionario.update({"edad": 41, "profesion": "Desarrollador"})
print(f"Después de update(): {mi_diccionario}") # {'nombre': 'David', 'edad': 41, 'ciudad': 'Valencia', 'profesion': 'Desarrollador'}

mi_diccionario.update(pais="España") # También se puede pasar con argumentos de palabra clave
print(f"Después de update(pais='España'): {mi_diccionario}") # ... 'pais': 'España'}

# Ejemplo 2: `pop()` y `popitem()`
# `pop(clave)`: Elimina el elemento con la clave especificada y devuelve su valor.
valor_ciudad = mi_diccionario.pop("ciudad")
print(f"Después de pop('ciudad') (valor: {valor_ciudad}): {mi_diccionario}") # {'nombre': 'David', 'edad': 41, 'profesion': 'Desarrollador', 'pais': 'España'}

# `popitem()`: Elimina y devuelve el último par (clave, valor) insertado (en Python 3.7+).
# En versiones anteriores, era un elemento arbitrario.
clave_eliminada, valor_eliminado = mi_diccionario.popitem()
print(f"Después de popitem() (clave: {clave_eliminada}, valor: {valor_eliminado}): {mi_diccionario}") # {'nombre': 'David', 'edad': 41, 'profesion': 'Desarrollador'}

