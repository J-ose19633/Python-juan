# Los parámetros son las variables listadas dentro de los paréntesis en la definición de la función.
# Los argumentos son los valores que se envían a la función cuando se llama.

# Ejemplo 1: Parámetros posicionales
# Los argumentos se asocian a los parámetros en el orden en que aparecen.
def describir_persona(nombre, edad, ciudad):
    """Imprime una descripción de una persona."""
    print(f"Nombre: {nombre}, Edad: {edad} años, Ciudad: {ciudad}.")

print("--- Parámetros Posicionales ---")
describir_persona("Sofía", 22, "Bogotá")
describir_persona("Pedro", 45, "Lima")

# El orden es importante
# describir_persona(30, "Carlos", "México") # Esto daría un resultado incorrecto

# Ejemplo 2: Parámetros con valores por defecto (Default Arguments)
# Permiten que un parámetro tenga un valor predefinido si no se proporciona un argumento.
def enviar_mensaje(mensaje, destinatario="mundo", saludo="Hola"):
    """Envía un mensaje personalizado."""
    print(f"{saludo}, {destinatario}: {mensaje}")

print("\n--- Parámetros con Valores por Defecto ---")
enviar_mensaje("¿Cómo estás?") # Usa destinatario="mundo", saludo="Hola"
enviar_mensaje("¡Feliz cumpleaños!", destinatario="Ana") # Usa saludo="Hola"
enviar_mensaje("Saludos cordiales.", "Dr. Smith", "Estimado") # Sobrescribe todos los valores por defecto

# Ejemplo 3: Argumentos de palabra clave (Keyword Arguments)
# Permiten pasar argumentos identificándolos por el nombre del parámetro. El orden no importa.
def crear_producto(nombre_producto, precio, stock=0):
    """Crea un producto con su nombre, precio y stock."""
    print(f"Producto: {nombre_producto}, Precio: ${precio:.2f}, Stock: {stock} unidades.")

print("\n--- Argumentos de Palabra Clave ---")
crear_producto(nombre_producto="Camiseta", precio=19.99) # Stock usa valor por defecto
crear_producto(precio=5.50, nombre_producto="Lápiz", stock=150) # Orden diferente, funciona igual
crear_producto("Libro", 25.00, stock=50) # Combinación posicional y palabra clave (posicionales primero)

