# El constructor en Python es un método especial llamado `__init__`.
# Se ejecuta automáticamente cada vez que se crea una nueva instancia (objeto) de una clase.
# Su propósito principal es inicializar los atributos del objeto con los valores proporcionados.

class Libro:
    # Atributo de clase
    tipo_material = "Impreso"

    def __init__(self, titulo, autor, anio_publicacion, paginas):
        """
        Constructor de la clase Libro.
        Inicializa los atributos de cada objeto Libro que se cree.
        `self` se refiere a la instancia del objeto que se está creando.
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.paginas = paginas
        self.leido = False # Atributo inicializado con un valor por defecto

        print(f"Libro '{self.titulo}' creado exitosamente.")

    def marcar_como_leido(self):
        """Método para cambiar el estado de lectura del libro."""
        self.leido = True
        print(f"'{self.titulo}' ha sido marcado como leído.")

    def mostrar_detalles(self):
        """Muestra los detalles del libro."""
        estado_leido = "Sí" if self.leido else "No"
        print(f"\n--- Detalles del Libro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Páginas: {self.paginas}")
        print(f"Material: {Libro.tipo_material}")
        print(f"¿Leído?: {estado_leido}")
        print("--------------------------")

# Ejemplo 1: Creación de objetos usando el constructor
# Cuando llamas a `Libro(...)`, el método `__init__` se ejecuta.
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 432)
libro2 = Libro("1984", "George Orwell", 1949, 328)

# Ejemplo 2: Acceso a atributos inicializados por el constructor
print(f"\nTítulo del libro1: {libro1.titulo}")
print(f"Autor del libro2: {libro2.autor}")
print(f"¿Libro1 leído inicialmente?: {libro1.leido}")

# Ejemplo 3: Uso de métodos que operan sobre atributos inicializados
libro1.marcar_como_leido()
libro1.mostrar_detalles()
libro2.mostrar_detalles()

# Un constructor puede tener valores por defecto para sus parámetros también
class Usuario:
    def __init__(self, username, email, activo=True):
        self.username = username
        self.email = email
        self.activo = activo
        print(f"Usuario {self.username} creado. Activo: {self.activo}")

user1 = Usuario("johndoe", "john@example.com")
user2 = Usuario("janedoe", "jane@example.com", activo=False)