# La concatenación es el proceso de unir dos o más cadenas de texto para formar una nueva cadena.

# Ejemplo 1: Concatenación con el operador `+`
cadena1 = "Hola"
cadena2 = "Mundo"
saludo = cadena1 + " " + cadena2 + "!"
print(f"Concatenación con '+': {saludo}") # 'Hola Mundo!'

nombre = "Ana"
apellido = "García"
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}") # 'Ana García'

# Ejemplo 2: Concatenación con f-strings (la forma más recomendada y legible)
# Permite incrustar expresiones dentro de cadenas literales.
ciudad = "México"
pais = "México"
mensaje_fstring = f"Viajando a {ciudad}, {pais}."
print(f"Concatenación con f-string: {mensaje_fstring}")

edad = 25
descripcion = f"Me llamo {nombre} y tengo {edad} años."
print(f"Descripción con f-string: {descripcion}")

