def calcularCuadradosLista(listaNumeros):
    listaCuadrados = []
    for i in range(0,len(listaNumeros)):
        listaCuadrados.append(listaNumeros[i]**2)
    return listaCuadrados

lista = [6,32,2,1,76,4,2]
print("LISTA DE NÚMEROS:")
print(lista)
print("LISTA DE SUS CUADRADOS:")
print(calcularCuadradosLista(lista))
