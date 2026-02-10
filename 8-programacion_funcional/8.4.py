"""
Escribir una función que reciba otra función booleana y una lista,
y devuelva otra lista con los elementos de la lista que 
devuelvan True alaplicarles la función booleana. 
"""

def mi_filtro_personalizado(funcion_booleana, lista):
    """
    Recorre una lista y devuelve una nueva lista solo con los 
    elementos donde la función booleana devuelve True.
    """
    filtrados = []
    for elemento in lista:
        if funcion_booleana(elemento):
            filtrados.append(elemento)
    return filtrados

# --- Ejemplos de uso ---

# 1. Función para detectar números pares
def es_par(n):
    return n % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solo_pares = mi_filtro_personalizado(es_par, numeros)

# 2. Función para detectar palabras largas
def es_larga(palabra):
    return len(palabra) > 5

palabras = ["sol", "computadora", "casa", "programación", "luz"]
palabras_largas = mi_filtro_personalizado(es_larga, palabras)

print(f"Números pares: {solo_pares}")
print(f"Palabras largas: {palabras_largas}")