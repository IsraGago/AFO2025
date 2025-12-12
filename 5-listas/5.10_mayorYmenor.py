precios = [50, 75, 46, 22, 80, 65, 8]

mayor = precios[0]
menor = precios[0]

for precio in precios:
    if precio > mayor:
        mayor = precio

for precio in precios:
    if precio < menor:
        menor = precio

print(precios)
print("mayor:",mayor)
print("menor:",menor)

print("Funciones de python")
print("mayor:", max(precios))
print("menor:", min(precios))
