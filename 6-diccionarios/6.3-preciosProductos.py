frutas = {
	"plátano" : 1.35,
	"manzana" : 0.80,
	"pera" : 0.85,
	"naranja" : 0.75
}

frutaComprar = input("Introduce la fruta a comprar: ")
kg = int(input("Introduce el peso en kg: "))

if frutaComprar.lower() in frutas:
	precio = frutas.get(frutaComprar.lower()) * kg
	print("precio"+":",precio)
else:
	print("La fruta introducida no está registrada.")
