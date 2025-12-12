articulos={}
precioTotal = 0
while(True):
    nombreArticulo = input("Introduce el nombre de un articulo (fin para salir): ")
    if nombreArticulo == "fin":
        break
    precio = float(input("introduce su precio: "))
    precioTotal += precio
    articulos[nombreArticulo] = precio

print(articulos)
print("precio total:",precioTotal)
