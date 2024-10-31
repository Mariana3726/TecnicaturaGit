from Orden import Orden
from Producto import Producto



producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalón', 150.00)
producto3 = Producto('Vestido', 320.00)  # tarea
producto4 = Producto('Medias', 45.00)
producto5 = Producto('Campera', 250.00)
producto6 = Producto('Sweter', 95.00)
producto7 = Producto('Blusa', 75.00)

productos1 = [producto1, producto2]  # lista de productos
productos2 = [producto1, producto3]

orden1 = Orden(productos1)  # primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto5)
orden1.agregar_producto(producto1)
print(orden1)
orden2 = Orden(productos2)  # tarea
print(orden2)
print(f'Total de la orden1: {orden1.calcular_total()}')
productos3 = [producto6, producto4]
orden2 = Orden(productos3)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto7)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')