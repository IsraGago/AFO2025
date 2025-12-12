n = int(input("Introduce un número: "))

print("CON UN SOLO BUCLE")
for i in range(n):
	print("*" * i)

print("CON BUCLE ANIDADO")
for i in range(n):
	for j in range(i):
		print("*",end="")
	print()
