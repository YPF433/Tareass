# class Mano:
#     def __init__(self, peso_maximo):
#         self.peso_maximo = peso_maximo

#     def puede_sostener(self, peso):
#         return peso <= self.peso_maximo

# class Persona:
#     def __init__(self):
#         self.fuerza_total = 100
#         self.mano_izquierda = Mano(60)
#         self.mano_derecha = Mano(50)

#     def puede_levantar(self, peso):
#         if self.mano_izquierda.puede_sostener(peso) or self.mano_derecha.puede_sostener(peso):
#             return "Puede levantarlo con una mano"
#         elif peso <= self.fuerza_total and (peso <= self.mano_izquierda.peso_maximo + self.mano_derecha.peso_maximo):
#             return "Puede levantarlo con ambas manos"
#         else:
#             return "No puede levantarlo"

# # Entrada del usuario
# peso_objeto = int(input("Ingrese el peso del objeto: "))

# persona = Persona()
# print(persona.puede_levantar(peso_objeto))

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class MetodoEnvio:
    def calcular_costo(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def tiempo_estimado(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class EnvioEstandar(MetodoEnvio):
    def calcular_costo(self):
        return 5.0

    def tiempo_estimado(self):
        return "5-7 días"

class EnvioExpress(MetodoEnvio):
    def calcular_costo(self):
        return 15.0

    def tiempo_estimado(self):
        return "1-2 días"

class EnvioPersonalizado(MetodoEnvio):
    def __init__(self, distancia):
        self.distancia = distancia

    def calcular_costo(self):
        return self.distancia * 0.5

    def tiempo_estimado(self):
        return f"{self.distancia // 10 + 1} días"

class Pedido:
    def __init__(self, productos, metodo_envio):
        self.productos = productos
        self.metodo_envio = metodo_envio

    def calcular_costo_total(self):
        total_productos = sum(producto.precio for producto in self.productos)
        return total_productos + self.metodo_envio.calcular_costo()

    def mostrar_tiempo_estimado(self):
        return self.metodo_envio.tiempo_estimado()

# Lista de productos disponibles
productos_disponibles = [
    Producto("Laptop", 1000),
    Producto("Smartphone", 700),
    Producto("Tablet", 400),
    Producto("Teclado", 50),
    Producto("Mouse", 30),
    Producto("Monitor", 300),
    Producto("Impresora", 200),
    Producto("Cámara", 500),
    Producto("Auriculares", 100),
    Producto("Cargador", 20)
]

# Mostrar productos disponibles
print("Productos disponibles:")
for i, producto in enumerate(productos_disponibles):
    print(f"{i + 1}. {producto.nombre} - ${producto.precio}")

# Selección de productos por el usuario
selecciones = input("Seleccione los números de los productos separados por comas: ")
productos_seleccionados = [productos_disponibles[int(i) - 1] for i in selecciones.split(",")]

# Mostrar métodos de envío disponibles
print("\nMétodos de envío disponibles:")
print("1. Envío estándar")
print("2. Envío express")
distancia = int(input("Si desea envío personalizado, ingrese la distancia (km), de lo contrario ingrese 0: "))

if distancia > 0:
    metodo_envio = EnvioPersonalizado(distancia)
elif input("Seleccione el método de envío (1 o 2): ") == "2":
    metodo_envio = EnvioExpress()
else:
    metodo_envio = EnvioEstandar()

pedido = Pedido(productos_seleccionados, metodo_envio)

# Mostrar resultado final
print("\nResumen del pedido:")
for producto in productos_seleccionados:
    print(f"- {producto.nombre}: ${producto.precio}")
print(f"Costo de envío: ${metodo_envio.calcular_costo()}")
print(f"Costo total: ${pedido.calcular_costo_total()}")
print(f"Tiempo estimado de entrega: {pedido.mostrar_tiempo_estimado()}")


