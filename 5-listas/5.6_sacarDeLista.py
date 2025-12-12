asignaturas = ["mates","fisica","histiora","lengua"]

for asignatura in asignaturas:
    nota = int(input("nota de "+asignatura+": "))
    if nota >= 5:
        asignaturas.remove(asignatura)

print("tienes que repetir",end=" ")
for asignatura in asignaturas:
    print(asignatura,end=" ")