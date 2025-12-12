# función sin parámetros
def sumar():
	a = 2
	b = 6
	resultado = a + b
	return resultado

valor = sumar()
print(valor)

# función con parámetros
def multiplicar(m,n):
	return m * n

def restar(a,b):
	return a - b

def operaciones(a,b):
	return {"suma":a+b,"resta":restar(a,b),"multiplicación":multiplicar(a,b)}

print(multiplicar(2,2))
print(restar(b=10,a = 2))
print(operaciones(10,2))
