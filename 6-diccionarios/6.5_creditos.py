creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditosTotales = 0

for clave,valor in creditos.items():
    print(clave,":",valor)
    creditosTotales += valor
print("creditos totales:",creditosTotales)