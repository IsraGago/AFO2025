salir = False
numeros = []
while(not salir):
    respuesta = input("Introduce un número ganador (fin para salir):")
    if respuesta == "fin":
        break;
    
    numPrimitiva = int(respuesta)
    numeros.append(numPrimitiva)

numeros.sort()
print(numeros)