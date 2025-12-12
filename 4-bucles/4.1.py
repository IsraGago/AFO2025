palabra = input("introduce una palabra: ")

for i in range(10):
    print(str(i)+".",palabra)

dias = ["lunes","martes","miércoles"]
for dia in dias:
    if dia == "miércoles":
        break
    print(dia)

nombre = "israel"
for letra in nombre:
    print(letra)

frutas =  ["manzana","platano","pera"]
colores = ["rojo","amarillo","verde"]

for fruta in frutas:
    for color in colores:
        print(fruta,color)