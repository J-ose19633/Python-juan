# Los diccionarios anidados son diccionarios que contienen otros diccionarios
# (o listas, tuplas) como valores. Son muy útiles para representar datos estructurados complejos.

# Ejemplo 1: Creación de un diccionario anidado (información de usuarios)
usuarios = {
    "usuario1": {
        "nombre": "Carlos",
        "edad": 30,
        "email": "carlos@example.com",
        "roles": ["admin", "editor"]
    },
    "usuario2": {
        "nombre": "Laura",
        "edad": 25,
        "email": "laura@example.com",
        "roles": ["viewer"],
        "preferencias": {"tema": "claro", "notificaciones": True}
    }
}
print("Diccionario de usuarios anidado:")
print(usuarios)

# Ejemplo 2: Acceso a valores en diccionarios anidados
# Se encadenan los accesos por clave.
print(f"\nNombre del usuario1: {usuarios['usuario1']['nombre']}") # 'Carlos'
print(f"Edad del usuario2: {usuarios['usuario2']['edad']}")     # 25
print(f"Primer rol del usuario1: {usuarios['usuario1']['roles'][0]}") # 'admin'
print(f"Preferencia de tema del usuario2: {usuarios['usuario2']['preferencias']['tema']}") # 'claro'

# Usar `get()` para acceso seguro en anidamiento
preferencia_inesperada = usuarios.get('usuario2', {}).get('configuracion_adicional', 'No configurado')
print(f"Preferencia adicional (segura): {preferencia_inesperada}")

# Ejemplo 3: Modificar y añadir elementos en diccionarios anidados
# Modificar un valor anidado
usuarios["usuario1"]["edad"] = 31
print(f"\nNueva edad del usuario1: {usuarios['usuario1']['edad']}")

# Añadir un nuevo rol al usuario2
usuarios["usuario2"]["roles"].append("uploader")
print(f"Roles actualizados del usuario2: {usuarios['usuario2']['roles']}")

# Añadir una nueva clave-valor anidada
usuarios["usuario1"]["direccion"] = {"calle": "Calle Falsa 123", "codigo_postal": "28001"}
print(f"Dirección del usuario1 añadida: {usuarios['usuario1']['direccion']}")

# Recorrer un diccionario anidado
print("\nIterando sobre usuarios y sus detalles:")
for user_id, user_data in usuarios.items():
    print(f"ID de Usuario: {user_id}")
    for key, value in user_data.items():
        print(f"  {key}: {value}")
    print("-" * 20)