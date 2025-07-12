# Los diccionarios en Python son colecciones no ordenadas, mutables y con claves-valor.
# Cada elemento es un par `clave: valor`. Las claves deben ser únicas e inmutables (ej: strings, números, tuplas).

# Ejemplo 1: Creación de diccionarios
# Usando llaves `{}`
mi_diccionario = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Madrid"
}
print(f"Diccionario inicial: {mi_diccionario}")

# Usando el constructor `dict()`
otro_diccionario = dict(marca="Ford", modelo="Fiesta", año=2020)
print(f"Otro diccionario (con dict()): {otro_diccionario}")

# Diccionario vacío
diccionario_vacio = {}
print(f"Diccionario vacío: {diccionario_vacio}")

