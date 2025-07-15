# Acceder a los valores en un diccionario es fundamental. Se hace principalmente
# usando la clave, pero hay otras maneras más seguras y útiles.

persona = {
    "nombre": "Elena",
    "edad": 35,
    "ciudad": "Barcelona",
    "email": "elena@example.com"
}
print(f"Diccionario de persona: {persona}")

# Ejemplo 1: Acceso directo por clave (usando corchetes `[]`)
# Es la forma más común, pero si la clave no existe, lanzará un `KeyError`.
print(f"Nombre de la persona: {persona['nombre']}")
print(f"Ciudad de residencia: {persona['ciudad']}")

# Ejemplo 2: Acceso seguro con el método `get()`
# `get(clave, valor_por_defecto)`:
#   - Si la clave existe, devuelve su valor.
#   - Si la clave no existe, devuelve `None` (por defecto) o el `valor_por_defecto` que especifiques.
telefono = persona.get("telefono", "No disponible")
print(f"Teléfono (con get): {telefono}") # 'No disponible'

email = persona.get("email") # Sin valor por defecto, devolverá None si no existe
print(f"Email (con get sin default): {email}") # 'elena@example.com'

