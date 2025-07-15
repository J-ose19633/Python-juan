# El ámbito (scope) de una variable determina dónde es accesible dentro de un programa.
# En Python, las variables pueden ser locales o globales.

# Variable global
saludo_global = "¡Hola desde el ámbito global!"
contador_global = 0

# Ejemplo 1: Variable local
def funcion_local():
    """Demuestra una variable local."""
    # `mensaje_local` es local a esta función; solo existe dentro de ella.
    mensaje_local = "Soy una variable local."
    print(mensaje_local)
    print(saludo_global) # Las funciones pueden acceder a variables globales

# Llamada a la función
funcion_local()

# Intentar acceder a `mensaje_local` fuera de la función generará un `NameError`.
# try:
#     print(mensaje_local)
# except NameError as e:
#     print(f"\nError: {e}. 'mensaje_local' no es accesible fuera de la función.")

print(f"Variable global accesible aquí: {saludo_global}")

# Ejemplo 2: Modificando una variable global (usando `global`)
def incrementar_contador():
    """Incrementa el contador global."""
    global contador_global # Indica que estamos trabajando con la variable global, no creando una nueva local
    contador_global += 1
    print(f"Contador dentro de la función: {contador_global}")

print(f"\nContador global inicial: {contador_global}")
incrementar_contador() # Incrementa a 1
incrementar_contador() # Incrementa a 2
print(f"Contador global final: {contador_global}")

# Si no usas `global` e intentas asignar, Python creará una variable local con el mismo nombre.
def simular_incremento_sin_global():
    contador_global = 100 # Esto crea una NUEVA variable local `contador_global`
    print(f"Contador LOCAL dentro de simular_incremento_sin_global: {contador_global}")

simular_incremento_sin_global()
print(f"Contador global después de simular_incremento_sin_global (no afectado): {contador_global}") # Sigue siendo 2

# Ejemplo 3: Ámbitos anidados (funciones dentro de funciones) y `nonlocal`
def funcion_externa():
    x = "local externa"
    print(f"\nEn funcion_externa (antes de funcion_interna): {x}")

    def funcion_interna():
        # `nonlocal` se usa para referirse a una variable en el ámbito de la función envolvente,
        # pero que no es global.
        nonlocal x
        x = "modificada por funcion_interna"
        print(f"En funcion_interna: {x}")

    funcion_interna()
    print(f"En funcion_externa (después de funcion_interna): {x}")

funcion_externa()