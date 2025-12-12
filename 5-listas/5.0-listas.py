a = [1,4,65,"hola",[6,7.6],"hola"]
print(a)
print(a[0])
print(a[1])
print(a[2])
print("La longitud de la lista es: ",len(a))
print("el 4 está en la posición: ",a.index(4)+1)
print("la palabra 'hola' aparecce",a.count("hola"),"veces")

if 1 in a:
	print("1 está en la lista")

a.append("asd")
