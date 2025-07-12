# Un objeto es una instancia de una clase. Es una entidad del mundo real
# que se modela con las características (atributos) y comportamientos (métodos) definidos en su clase.

class Producto:
    # Atributo de clase (común a todos los productos)
    iva = 0.16 # 16% de IVA

    def __init__(self, nombre, precio, stock):
        """Constructor: inicializa los atributos de un nuevo objeto Producto."""
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.activo = True # Atributo inicializado por defecto

    def calcular_precio_con_iva(self):
        """Calcula y retorna el precio del producto incluyendo el IVA."""
        return self.precio * (1 + self.iva)

    def vender(self, cantidad):
        """Simula la venta de una cantidad de producto."""
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Vendidos {cantidad} unidades de '{self.nombre}'. Stock restante: {self.stock}")
            return True
        else:
            print(f"No hay suficiente stock de '{self.nombre}'. Disponible: {self.stock}")
            return False

    def reabastecer(self, cantidad):
        """Aumenta el stock del producto."""
        self.stock += cantidad
        print(f"Stock de '{self.nombre}' reabastecido. Nuevo stock: {self.stock}")

    def mostrar_estado(self):
        """Muestra el estado actual del objeto producto."""
        estado = "Activo" if self.activo else "Inactivo"
        print(f"\n--- Producto: {self.nombre} ---")
        print(f"Precio (sin IVA): ${self.precio:.2f}")
        print(f"Precio (con IVA): ${self.calcular_precio_con_iva():.2f}")
        print(f"Stock: {self.stock} unidades")
        print(f"Estado: {estado}")
        print("----------------------------")

# Ejemplo 1: Creación de objetos de la clase `Producto`
# Cada llamada a `Producto(...)` crea un nuevo objeto distinto.
laptop = Producto("Laptop Dell XPS", 1200.00, 10)
teclado = Producto("Teclado Mecánico", 85.50, 25)
mouse = Producto("Mouse Inalámbrico", 30.00, 50)

# Ejemplo 2: Interacción con los objetos (llamando a sus métodos)
print("\n--- Operaciones con objetos ---")
laptop.vender(2)
teclado.vender(30) # No hay suficiente stock
teclado.reabastecer(10)
teclado.vender(30) # Ahora sí hay suficiente

# Ejemplo 3: Acceso y modificación de atributos de objetos
print(f"\nStock inicial de mouse: {mouse.stock}")
mouse.stock = 45 # Modificación directa del atributo del objeto
print(f"Stock modificado de mouse: {mouse.stock}")

# Desactivar un producto
mouse.activo = False

