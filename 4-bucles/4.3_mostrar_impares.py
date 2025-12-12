numero = int(input("Introduce un número: "))
if numero >= 0:
    mensaje = ""
    for i in range(numero):
        if i % 2 == 0:
            mensaje += ","+str(i)
    print(mensaje[1:])
else:
    print("Debe ser un número positivo")