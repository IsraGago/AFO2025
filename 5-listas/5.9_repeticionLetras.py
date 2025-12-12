vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}
palabra = "Esternocleidomastoideo"

for letra in palabra.lower():
    for clave in vocales.keys():
        if letra == clave:
            vocales[clave] +=1

for clave,valor in vocales.items():
    print(clave+":",valor)