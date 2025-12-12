letra = input("Introduce tu nombre: ")[0].lower()
sexo = input("Introduce tu sexo (hombre/mujer): ").lower()
grupo = ""

if sexo == "mujer" :
    if letra < "m":
        grupo = "A"
    else:
        grupo = "B" 
elif sexo == "hombre":
    if letra > "n":
        grupo = "A"
    else:
        grupo = "B"

print("Perteneces al grupo:",grupo)