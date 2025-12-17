# AUTOR: ISRAEL BENJAMÍN GAGO ACUÑA
creditos = {"Matemáticas":5,"Física":3,"Química":7,"Inglés":4,"Lengua":8,"EF":10,"Gallego":4,"Plástica":7,"Tecnología":10}
claveMaxCreditos = ""
claveMinCreditos = ""
media = 0
contadorSuspensas = 0
contadorAprobadas = 0
moda = {}

# USO EL MISMO BUCLE PARA TODOS LOS APARTADOS POR OPTIMIZACIÓN
for asignatura,nota in creditos.items():
    if claveMaxCreditos == "":
        claveMaxCreditos = asignatura
    elif creditos[claveMaxCreditos] < nota:
        claveMaxCreditos = asignatura

    if claveMinCreditos == "":
        claveMinCreditos = asignatura
    elif creditos[claveMinCreditos] > nota:
        claveMinCreditos = asignatura

    media+=nota
    if nota < 5:
        contadorSuspensas += 1
    else:
        contadorAprobadas += 1

    #Funcionalidad extra: calcular la moda
    if nota in moda:
        moda[nota] += 1
    else:
        moda[nota] = 1

    print(asignatura,"calificación",nota)

print("")
print("la asignatura",claveMaxCreditos,"tiene la máxima nota:",creditos[claveMaxCreditos])
print("la asignatura",claveMinCreditos,"tiene la mínima nota:",creditos[claveMinCreditos])
print("el número de asignaturas suspensas es:",contadorSuspensas)
print("el número de asignaturas aprobadas es:",contadorAprobadas)

media = media / len(creditos)
print("la media de las asignaturas es:",media)

# apartado G. considero que si el alumno no ha aprobado al menos una no puede tener proyecto,
# ya que se establece en el enunciado que la nota del mismo debe ser la más alta de las notas aprobadas.
if contadorAprobadas > 0:
    creditos["Proyecto"] = creditos[claveMaxCreditos]
    print("Nota del proyecto:", creditos["Proyecto"])

# apartado H: funcionalidad extra. hayar la nota más repetida (moda)
print("la nota más repetida es",str(max(moda))+": aparece",moda[max(moda)],"veces")
