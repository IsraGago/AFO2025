nombre= "Israel Benjamín Gago Acuña"
print(nombre.lower())
print(nombre.upper())
palabras = nombre.split(" ")
nombreProcesado = ""
for palabra in palabras:
        nombreProcesado += palabra[0].upper()+palabra[1:].lower()+" "
print(nombreProcesado)