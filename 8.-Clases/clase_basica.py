# Las clases son plantillas para crear objetos (instancias).
# Definen un conjunto de atributos (datos) y métodos (funciones) que los objetos tendrán.

# Ejemplo 1: Definición de una clase básica `Persona`
class Persona:
    # Atributo de clase (compartido por todas las instancias de la clase)
    especie = "Homo Sapiens"

    def __init__(self, nombre, edad):
        """
        Método constructor. Se llama automáticamente cuando se crea una nueva instancia de la clase.
        `self` se refiere a la instancia actual del objeto.
        Los parámetros como `nombre` y `edad` se usan para inicializar los atributos del objeto.
        """
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def saludar(self):
        """Método de instancia que imprime un saludo."""
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def describir_especie(self):
        """Método que usa un atributo de clase."""
        print(f"Soy un {self.especie}.")

# Ejemplo 2: Creación de objetos (instancias) de la clase `Persona`
persona1 = Persona("Ana", 30)
persona2 = Persona("Juan", 25)

# Acceder a los atributos de los objetos
print(f"Nombre de persona1: {persona1.nombre}")
print(f"Edad de persona2: {persona2.edad}")

# Llamar a los métodos de los objetos
persona1.saludar()     # Salida: Hola, mi nombre es Ana y tengo 30 años.
persona2.saludar()     # Salida: Hola, mi nombre es Juan y tengo 25 años.

# Acceder al atributo de clase
print(f"Especie de persona1: {persona1.especie}")
print(f"Especie de persona2: {persona2.especie}")
print(f"Especie de la clase Persona: {Persona.especie}")

persona1.describir_especie()

# Ejemplo 3: Modificar atributos de instancia
persona1.edad = 31
print(f"Nueva edad de persona1: {persona1.edad}")
persona1.saludar()