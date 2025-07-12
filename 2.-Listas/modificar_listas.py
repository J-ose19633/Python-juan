# Las listas son mutables, lo que significa que sus elementos pueden ser cambiados
# después de que la lista ha sido creada.

mi_lista = ["uno", "dos", "tres", "cuatro", "cinco"]
print(f"Lista original: {mi_lista}")

# Ejemplo 1: Modificar un elemento individual por su índice
mi_lista[0] = "primer_elemento"
print(f"Después de modificar el primer elemento: {mi_lista}") # ['primer_elemento', 'dos', 'tres', 'cuatro', 'cinco']

mi_lista[3] = "elemento_nuevo"
print(f"Después de modificar el cuarto elemento: {mi_lista}") # ['primer_elemento', 'dos', 'tres', 'elemento_nuevo', 'cinco']

# Ejemplo 2: Modificar un rango de elementos (slicing con asignación)
# Puedes reemplazar una porción de la lista con una nueva lista.
mi_lista[1:3] = ["reemplazo_dos", "reemplazo_tres"]
print(f"Después de modificar un slice [1:3]: {mi_lista}") # ['primer_elemento', 'reemplazo_dos', 'reemplazo_tres', 'elemento_nuevo', 'cinco']

# Si el número de elementos en la nueva lista es diferente, la lista se ajusta.
mi_lista[0:2] = ["a", "b", "c", "d"] # Esto insertará más elementos
print(f"Después de reemplazar un slice con más elementos: {mi_lista}") # ['a', 'b', 'c', 'd', 'reemplazo_tres', 'elemento_nuevo', 'cinco']

