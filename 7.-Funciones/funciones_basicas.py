# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Ayudan a organizar el código, hacerlo más modular y evitar la repetición.

# Ejemplo 1: Definición de una función sin parámetros ni retorno
def saludar():
    """Esta función simplemente imprime un saludo."""
    print("¡Hola! Bienvenido a las funciones de Python.")

# Llamada a la función
saludar()
saludar() # Se puede llamar múltiples veces

# Ejemplo 2: Función con un parámetro
def saludar_personalizado(nombre):
    """Esta función saluda a una persona por su nombre."""
    print(f"¡Hola, {nombre}! Es un placer conocerte.")

# Llamadas a la función con diferentes argumentos
saludar_personalizado("Alicia")
saludar_personalizado("Roberto")

# Ejemplo 3: Función que realiza una operación y devuelve un valor
def obtener_cuadrado(numero):
    """Esta función calcula el cuadrado de un número y lo devuelve."""
    cuadrado = numero * numero
    return cuadrado # La palabra clave 'return' envía el valor de vuelta al llamador

# Llamada a la función y almacenamiento del resultado
resultado1 = obtener_cuadrado(5)
print(f"El cuadrado de 5 es: {resultado1}")

resultado2 = obtener_cuadrado(9)
print(f"El cuadrado de 9 es: {resultado2}")

# El valor devuelto puede usarse directamente en otras expresiones
print(f"El doble del cuadrado de 3 es: {2 * obtener_cuadrado(3)}")