cantidadInvertir = float(input("Introduzca la cantidad a invertir: "))
interesAnual = float(input("Introduzca el interés anual: "))
numAnos = int(input("Introduzca el número de años: "))
capitalFinal = cantidadInvertir * (1 + interesAnual / 100) ** numAnos
print("")

