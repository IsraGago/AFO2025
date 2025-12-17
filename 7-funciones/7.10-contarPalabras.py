def frecuenciaPalabras(texto):
    diccionario = {}
    for palabra in texto.split():
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def palabraMasRepetida(diccionario):
    palabraMasRepetida = ""
    maxNumRepeticiones = 0
    for palabra,numRepeticiones in diccionario.items():
        if numRepeticiones > maxNumRepeticiones:
            palabraMasRepetida = palabra
            maxNumRepeticiones = numRepeticiones
    return [palabraMasRepetida,maxNumRepeticiones]


cadena = "A oferta do IES Chan do Monte comprende unha ensinanza a varios niveis tanto de Educación Secundaria Obrigatoria, Bacharelatos, FP Básica  e Ciclos Medios e Ciclos Superiores de Formación Profesional"
diccionario = frecuenciaPalabras(cadena) 
print(diccionario)

masRepetida = palabraMasRepetida(diccionario)
print("La palabra más repetida es",masRepetida[0],masRepetida[1],"veces")