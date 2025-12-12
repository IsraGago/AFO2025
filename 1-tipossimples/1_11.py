PORCENTAJE_INTERES = 0.04

dineroDepositado = float(input("Introduce la cantidad de dinero depositado (€): "))

dineroDepositado = dineroDepositado + dineroDepositado * PORCENTAJE_INTERES
print("Ahorros año 1:", round(dineroDepositado,2),"€")

dineroDepositado = dineroDepositado + dineroDepositado * PORCENTAJE_INTERES
print("Ahorros año 2:", round(dineroDepositado,2),"€")

dineroDepositado = dineroDepositado + dineroDepositado * PORCENTAJE_INTERES
print("Ahorros año 3:", round(dineroDepositado,2),"€")
