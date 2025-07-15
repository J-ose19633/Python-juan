# La principal diferencia entre tuplas y listas es su mutabilidad.
# Listas: mutables (se pueden cambiar después de la creación).
# Tuplas: inmutables (no se pueden cambiar después de la creación).

# Ejemplo 1: Mutabilidad vs Inmutabilidad
mi_lista = [1, 2, 3]
mi_tupla = (1, 2, 3)

print(f"Lista inicial: {mi_lista}")
print(f"Tupla inicial: {mi_tupla}")

# Modificar una lista (permitido)
mi_lista.append(4)
mi_lista[0] = 0
print(f"Lista después de modificar: {mi_lista}") # [0, 2, 3, 4]

# Intentar modificar una tupla (causará TypeError)
try:
    mi_tupla.append(4) # Este método no existe para tuplas
except AttributeError as e:
    print(f"\nError al intentar append en tupla: {e}")

try:
    mi_tupla[0] = 0 # No se puede asignar elementos en tupla
except TypeError as e:
    print(f"Error al intentar modificar elemento de tupla: {e}")

# Ejemplo 2: Uso de tuplas en diccionarios (como claves)
# Las tuplas pueden ser claves de diccionario porque son inmutables. Las listas no pueden.
coordenada1 = (10, 20)
coordenada2 = (30, 40)

mapa_puntos = {
    coordenada1: "Punto A",
    coordenada2: "Punto B"
}
print(f"\nDiccionario con claves de tupla: {mapa_puntos}")
print(f"Valor del Punto A: {mapa_puntos[(10, 20)]}")

# Ejemplo 3: Rendimiento y seguridad de datos
# Las tuplas suelen ser ligeramente más rápidas que las listas para algunas operaciones
# y son útiles cuando necesitas una colección de elementos que no debería cambiar.

# Iterar sobre tuplas y listas (similares en sintaxis)
print("\nIterando sobre lista y tupla:")
for item in mi_lista:
    print(f"Lista item: {item}")

for item in mi_tupla:
    print(f"Tupla item: {item}")