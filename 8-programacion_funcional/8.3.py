"""
Escribir una función que reciba otra función y una lista, 
y devuelva otra lista con el resultado de aplicar la función 
dada a cada uno de los elementos de la lista. 
"""

def mi_map_personalizado(funcion, lista):
    """
    Aplica una función a cada elemento de una lista 
    y retorna una nueva lista con los resultados.
    """
    resultados = []
    for elemento in lista:
        resultados.append(funcion(elemento))
    return resultados

# --- Ejemplos de uso ---

# 1. Elevar al cuadrado
def cuadrado(n):
    return n ** 2

numeros = [1, 2, 3, 4, 5]
lista_cuadrados = mi_map_personalizado(cuadrado, numeros)

# 2. Convertir a mayúsculas
def gritar(texto):
    return texto.upper() + "!"

palabras = ["hola", "python", "función"]
lista_gritando = mi_map_personalizado(gritar, palabras)

print(f"Cuadrados: {lista_cuadrados}")
print(f"Gritos: {lista_gritando}")