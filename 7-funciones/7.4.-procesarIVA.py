def procesarIVA(importe,porcentaje):
    return importe - (importe * porcentaje) / 100

print(procesarIVA(148,20))
