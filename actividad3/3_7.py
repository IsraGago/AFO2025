renta = int(input("Introduce tu renta anual: "))
tipoImpositivo = 0
if renta < 10000:
    tipoImpositivo = 5
elif renta > 10000 and renta < 20000:
    tipoImpositivo = 15
elif renta > 20000 and renta < 35000:
    tipoImpositivo = 20
elif renta > 35000 and renta < 60000:
    tipoImpositivo = 30
elif renta > 60000:
    tipoImpositivo = 45

print("tu tipo impositivo es del "+str(tipoImpositivo)+"%")