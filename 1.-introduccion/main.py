# Un archivo `main.py` es comúnmente usado como el punto de entrada principal de un programa Python.
# Aquí se orquesta la lógica principal o se llaman a otras funciones/módulos.

def saludar(nombre):
    """Función que imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}! Este es el programa principal.")

def sumar(a, b):
    """Función que suma dos números y devuelve el resultado."""
    return a + b

def mostrar_info_sistema():
    """Función que simula mostrar información del sistema."""
    import sys
    print(f"Versión de Python: {sys.version}")
    print("Programa principal en ejecución...")

# El bloque if __name__ == "__main__": es una buena práctica.
# Asegura que el código dentro de él solo se ejecute cuando el script es ejecutado directamente,
# no cuando es importado como un módulo en otro script.
if __name__ == "__main__":
    print("--- Inicio del Programa Principal ---")

    # Ejemplo 1: Llamada a una función de saludo
    saludar("Mundo Python")