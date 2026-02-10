"""
Escribir una función que reciba una muestra de números y 
devuelva los valores atípicos, es decir, los valores cuya 
puntuación típica sea mayor que 3 o menor que -3. Nota: La 
puntuación típica de un valor se obtiene restando la media y 
dividiendo por la desviación típica de la muestra. 
"""

import math

def detectar_atipicos(muestra):
    if not muestra:
        return []

    # 1. Calcular la media
    media = sum(muestra) / len(muestra)
    
    # 2. Calcular la desviación típica
    # Suma de las diferencias al cuadrado dividida por N
    varianza = sum((x - media) ** 2 for x in muestra) / len(muestra)
    desviacion_tipica = math.sqrt(varianza)
    
    # Si la desviación es 0, todos los números son iguales; no hay atípicos
    if desviacion_tipica == 0:
        return []
    
    # 3. Filtrar valores cuya puntuación típica (z) sea > 3 o < -3
    atipicos = []
    for x in muestra:
        puntuacion_z = (x - media) / desviacion_tipica
        if abs(puntuacion_z) > 3:
            atipicos.append(x)
            
    return atipicos

# --- Ejemplo de uso ---
# Una muestra donde el 1000 es claramente un "outlier"
datos = [10, 12, 11, 13, 12, 11, 10, 12, 11, 1000]
print(f"Valores atípicos detectados: {detectar_atipicos(datos)}")