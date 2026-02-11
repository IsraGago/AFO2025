# AUTOR: ISRAEL BENJAMÍN GAGO ACUÑA
class Articulo():
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class ShoppingCart():
    def __init__(self):
        self.items = []
        
    def add_item(self,nombre,cantidad):
        self.items.append(Articulo(nombre,cantidad))
        
    def remove_item(self,nombre):
        for item in self.items:
            if item.nombre == nombre:
                self.items.remove(item)
                
    def calculate_total(self):
        total = 0
        for item in self.items:
            total+= item.cantidad
        return total
    
    def mostrarArticulos(self):
        print("Articulos en el carrito:")
        for item in self.items:
            print("Articulo:",item.nombre,"- cantidad:",item.cantidad)
        
        
        
carrito = ShoppingCart()
carrito.add_item("Televisión",2)
carrito.add_item("Tarjeta gráfica",1)
carrito.add_item("Tarjeta gráfica",2)
carrito.remove_item("Tarjeta gráfica") # Esto borra el primer item que tiene como nombre tarjeta gráfica
print("Cantidad de articulos:",carrito.calculate_total())

carrito.mostrarArticulos()