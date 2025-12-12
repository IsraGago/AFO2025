asignaturas = ["Matemáticas","Física","Historia","Lengua"]

notas = []



for i in range(len(asignaturas)):
	notas.append(int(input("introduce tu nota en "+str(asignaturas[i])+": ")))


print("NOTAS")
for i in range(len(asignaturas)):
	print(str(asignaturas[i])+":",notas[i])
