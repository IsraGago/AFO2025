def calcularFactorial(numero):
    factorial = 1
    for i in range (1,numero):
        factorial = factorial * i
    return factorial

print(calcularFactorial(5))