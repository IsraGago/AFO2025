puntuacion = float(input("Escribe tu puntuacion: "))
nivel = ""
sueldo = 2400

if puntuacion == 0.0:
    nivel = "inaceptable"
elif puntuacion == 0.4:
    nivel = "aceptable"
elif puntuacion >= 0.6:
    nivel = "meritorio"
else: 
    print("Puntuación inválida")
    exit()

sueldo = sueldo + sueldo * puntuacion
print("nivel:",nivel)   
print("sueldo:",sueldo)


