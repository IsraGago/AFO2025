divisas = {"Euro":"€","Dollar":"$","Yen":"¥"}

respuesta = input("Introduzca el nombre de una divisa para visualizar su símbolo: ")
respuesta = respuesta.lower()

if respuesta == "euro":
	print("€")
elif respuesta == "dollar":
	print("$")
elif respuesta == "yen":
	print("¥")
else:
	print("La divisa introducida no está registrada.")

