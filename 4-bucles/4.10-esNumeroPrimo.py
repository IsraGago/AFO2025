numero = int(input("Introduce un número para comprobar si es primo: "))

i = 2

while numero % i !=0:
	i = i+1
if i == numero:
	print("Es primo.")
else:
	print("NO es primo.")
