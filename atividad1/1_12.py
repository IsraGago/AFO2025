PRECIO_PAN = 3.49
DESCUENTO = 0.6
numBarras = int(input("Introduce el número de barras de pan que no son de hoy: "))
precioNormal = PRECIO_PAN * numBarras
print("Precio normal:",round(precioNormal,2),"€")
print("Precio con descuento:", round(precioNormal - precioNormal * DESCUENTO,2),"€")