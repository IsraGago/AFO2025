def calcularAreaCirculo(radio):
    return 3.14159*radio**2

def calcularAreaCilindrio(radio1,radio2):
    return calcularAreaCirculo(radio1)+calcularAreaCirculo(radio2)

print(calcularAreaCirculo(10))
print(calcularAreaCilindrio(10,10))
