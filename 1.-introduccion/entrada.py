# La función input() se utiliza para obtener datos del usuario a través de la consola.
# Siempre devuelve el dato como una cadena de texto (string).

# Ejemplo 1: Pedir el nombre del usuario
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola, {nombre}. ¡Bienvenido!")


# Ejemplo 2: Pedir un número decimal y realizar una operación
precio_str = input("Introduce el precio del producto: ")
cantidad_str = input("Introduce la cantidad: ")

precio_float = float(precio_str)    # Convertimos a flotante
cantidad_int = int(cantidad_str)    # Convertimos a entero

total = precio_float * cantidad_int
print(f"El total a pagar es: ${total:.2f}") # Formato a 2 decimales
