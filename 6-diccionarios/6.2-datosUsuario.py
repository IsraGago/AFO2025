nombre = input("introduce tu nombre: ")
edad = int(input("introduce tu edad: "))
direccion = input("introduce tu dirección: ")
telefono = input("introduce tu número de teléfono: ")

datos = {"nombre":nombre,"edad":edad,"dirección":direccion,"telefono":telefono}

for clave, valor in datos.items():
	print(clave+":",valor)
