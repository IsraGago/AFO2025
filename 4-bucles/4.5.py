importe = int(input("Introduce la cantidad a invertir: "))
interesAnual = int(input("Introduce la cantidad de interes anual: "))
numAnos = int(input("Introduce el número de años: "))


for i in range(1,numAnos+1):
	capital = importe * (1 + interesAnual / 100) ** i
	print("El año",i,"se han conseguido",capital,"euros")