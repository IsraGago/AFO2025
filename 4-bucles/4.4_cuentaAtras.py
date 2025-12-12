n = int(input("introduce un nmero entero positivo: "))
if n <= 0:
    print("el nmero es negativo")
    exit()

mensaje = ""
for i in range(n,0,-1):
    mensaje += ","+str(i)

print(mensaje[1:])
