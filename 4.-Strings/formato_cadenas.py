# El formato de cadenas es crucial para presentar información de manera legible.
# Python ofrece varias maneras de formatear cadenas.

# Ejemplo 1: Formato con el operador `%` (antiguo)
nombre = "Alicia"
edad = 30
saludo_percent = "Hola, mi nombre es %s y tengo %d años." % (nombre, edad)
print(f"Formato con %: {saludo_percent}")

precio = 19.99
descuento = 0.15
mensaje_flotante = "El producto cuesta %.2f y tiene un %.0f%% de descuento." % (precio, descuento * 100)
print(f"Formato con % (flotantes): {mensaje_flotante}")

# Ejemplo 2: Formato con el método `str.format()`
producto = "Laptop"
precio_unitario = 899.99
cantidad = 2
total = precio_unitario * cantidad

mensaje_format = "Compraste {} {} por un total de ${:.2f}.".format(cantidad, producto, total)
print(f"Formato con .format(): {mensaje_format}")

# Posición de argumentos en .format()
mensaje_posicional = "El {0} es {1} y el {1} es {0}.".format("día", "noche")
print(f"Formato con .format() (posicional): {mensaje_posicional}")

# Argumentos por palabra clave en .format()
mensaje_keyword = "Mi nombre es {nombre} y me gusta {hobby}.".format(nombre="Sofía", hobby="programar")
print(f"Formato con .format() (keyword): {mensaje_keyword}")

