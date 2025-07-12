# La herencia es un pilar de la Programación Orientada a Objetos (POO).
# Permite que una clase (clase hija o subclase) herede atributos y métodos de otra clase (clase padre o superclase).
# Esto fomenta la reutilización de código y la creación de jerarquías de clases.

# Clase Padre (Superclase)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Animal {self.nombre} (edad: {self.edad}) ha sido creado.")

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

# Clase Hija (Subclase) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llama al constructor de la clase padre para inicializar sus atributos
        super().__init__(nombre, edad)
        self.raza = raza # Atributo específico de Perro
        print(f"Perro '{self.nombre}' (raza: {self.raza}) ha sido creado.")

    def ladrar(self):
        print(f"{self.nombre} ({self.raza}) está ladrando: ¡Guau guau!")

    # Se puede sobrescribir (override) un método del padre
    def comer(self):
        print(f"{self.nombre} está comiendo su comida para perros.")

# Otra Clase Hija que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color_pelo):
        super().__init__(nombre, edad)
        self.color_pelo = color_pelo
        print(f"Gato '{self.nombre}' (color: {self.color_pelo}) ha sido creado.")

    def maullar(self):
        print(f"{self.nombre} ({self.color_pelo}) está maullando: ¡Miau!")

# Ejemplo 1: Creación de objetos de las clases hijas
mi_perro = Perro("Anllelo", 3, "criollo")
mi_gato = Gato("Minino", 2, "rallero")

print("-" * 30)

# Ejemplo 2: Usar métodos heredados del padre
mi_perro.dormir() # Método heredado de Animal
mi_gato.dormir()  # Método heredado de Animal

# Ejemplo 3: Usar métodos específicos de la clase hija
mi_perro.ladrar()
mi_gato.maullar()

