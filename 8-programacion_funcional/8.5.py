"""
Escribir una función que reciba una frase y devuelva un diccionario 
con las palabras que contiene y su longitud. 
"""

def mapear_longitud_palabras(frase):
    """
    Recibe una frase y devuelve un diccionario donde las claves son 
    las palabras y los valores son sus longitudes.
    """
    # Dividimos la frase en una lista de palabras
    palabras = frase.split()
    
    # Creamos el diccionario usando una comprensión de diccionarios
    resultado = {palabra: len(palabra) for palabra in palabras}
    
    return resultado

# --- Ejemplo de uso ---
texto = "Python es un lenguaje muy versátil"
diccionario_resultado = mapear_longitud_palabras(texto)

print(f"Frase: '{texto}'")
print(f"Resultado: {diccionario_resultado}")