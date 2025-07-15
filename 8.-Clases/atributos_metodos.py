# Las clases se componen de atributos (variables que almacenan datos) y métodos (funciones que operan sobre esos datos).

# Atributos:
# - Atributos de clase: Compartidos por todas las instancias de la clase.
# - Atributos de instancia: Pertenecen a una instancia específica del objeto.

# Métodos:
# - Métodos de instancia: Operan sobre los datos de una instancia específica (`self`).

class Coche:
    # Atributo de clase: Define una característica común a todos los coches
    ruedas = 4

    def __init__(self, marca, modelo, anio):
        """
        Constructor de la clase Coche.
        Define atributos de instancia.
        """
        self.marca = marca      # Atributo de instancia
        self.modelo = modelo    # Atributo de instancia
        self.anio = anio        # Atributo de instancia
        self.velocidad = 0      # Atributo de instancia con valor inicial

    # Método de instancia: Accede y opera sobre los atributos de la instancia
    def acelerar(self, incremento):
        """Aumenta la velocidad del coche."""
        self.velocidad += incremento
        print(f"{self.marca} {self.modelo} está acelerando. Velocidad actual: {self.velocidad} km/h.")

    # Método de instancia
    def frenar(self, decremento):
        """Disminuye la velocidad del coche."""
        self.velocidad = max(0, self.velocidad - decremento) # Evita velocidad negativa
        print(f"{self.marca} {self.modelo} está frenando. Velocidad actual: {self.velocidad} km/h.")

    # Otro método de instancia
    def mostrar_info(self):
        """Muestra la información del coche."""
        print(f"--- Información del Coche ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Ruedas: {self.ruedas}") # Accediendo a un atributo de clase
        print(f"Velocidad actual: {self.velocidad} km/h")
        print("----------------------------")

# Ejemplo 1: Creación de objetos y uso de atributos/métodos
mi_coche = Coche("Toyota", "Corolla", 2022)
otro_coche = Coche("Honda", "Civic", 2020)

print(f"Ruedas de mi_coche (atributo de clase): {mi_coche.ruedas}")
print(f"Ruedas del otro_coche (atributo de clase): {otro_coche.ruedas}")
print(f"Marca de mi_coche (atributo de instancia): {mi_coche.marca}")

mi_coche.acelerar(50)
mi_coche.frenar(10)
otro_coche.acelerar(70)

# Ejemplo 2: Acceder y modificar atributos directamente
print(f"\nVelocidad de mi_coche antes de modificar directamente: {mi_coche.velocidad}")
mi_coche.velocidad = 80 # Se puede modificar directamente un atributo
print(f"Velocidad de mi_coche después de modificar directamente: {mi_coche.velocidad}")

# Ejemplo 3: Demostración de `mostrar_info`
print("\nMostrando información de los coches:")
mi_coche.mostrar_info()
otro_coche.mostrar_info()