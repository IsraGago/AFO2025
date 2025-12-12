n = int(input("Introduce un número entero: "))


for i in range(1,n+1,2):
	linea = ""
	for j in range(1,i+1,2):
		linea = str(j)+ " " + linea
	print(linea)
