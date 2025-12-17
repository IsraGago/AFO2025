def calcularMedia(listaNumeros):
    media = 0
    for numero in listaNumeros:
        media+=numero
    return media / len(listaNumeros)

lista = [6,4,2,7,5,10]
print(calcularMedia(lista)) 