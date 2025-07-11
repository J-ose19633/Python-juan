# En Python, no existen las constantes en el sentido estricto (valores inmutables forzados por el lenguaje).
# Sin embargo, por convención, se usan variables con nombres en MAYÚSCULAS para indicar que son constantes
# y no deberían ser modificadas durante la ejecución del programa.

# Ejemplo 1: Una constante numérica
PI = 3.14159
RADIO = 5

circunferencia = 2 * PI * RADIO
print(f"La circunferencia de un círculo con radio {RADIO} es: {circunferencia}")

# Ejemplo 2: Una constante de cadena de texto
NOMBRE_APLICACION = "MiGestorDeTareas"
VERSION = "1.0.0"

print(f"Bienvenido a {NOMBRE_APLICACION} v{VERSION}")

