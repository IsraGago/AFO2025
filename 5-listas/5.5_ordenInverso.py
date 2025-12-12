numeros = []

while True:
    respuesta = input("Introduce un número (fin para salir): ")
    if respuesta == "fin":
        break;

    respuesta = int(respuesta)
    numeros.append(respuesta)

numeros.sort(reverse=True)

print(numeros)