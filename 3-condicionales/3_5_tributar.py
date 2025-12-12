edad = int(input("Introduce tu edad: "))
salarioMensual = int(input("Introduce tu salario mensual: "))
if edad > 16 and salarioMensual >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")