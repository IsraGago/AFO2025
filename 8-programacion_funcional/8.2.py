"""
Escribir una función que simule una calculadora científica que 
permita calcular el seno, coseno, tangente, exponencial y logaritmo 
neperiano. La función preguntará al usuario el valor y la función a 
aplicar, y mostrará por pantalla una tabla con los enteros de 1 al 
valor introducido y el resultado de aplicar la función a esos enteros. 
"""

import math

def calculadora_cientifica():
    # Diccionario para mapear la entrada del usuario con las funciones de math
    funciones = {
        'seno': math.sin,
        'coseno': math.cos,
        'tangente': math.tan,
        'exponencial': math.exp,
        'logaritmo': math.log
    }
    
    # Solicitar datos al usuario
    print("Funciones disponibles: seno, coseno, tangente, exponencial, logaritmo")
    operacion = input("Introduce la función que deseas aplicar: ").lower()
    
    if operacion not in funciones:
        print("Error: Función no reconocida.")
        return

    try:
        numero_limite = int(input("Introduce un número entero positivo: "))
        if numero_limite < 1:
            print("Por favor, introduce un número mayor o igual a 1.")
            return
    except ValueError:
        print("Error: Debes introducir un número entero.")
        return

    # Cabecera de la tabla
    print(f"\nTabla de resultados para: {operacion.upper()}")
    print(f"{'Entero':<10} | {operacion.capitalize()}")
    print("-" * 25)

    # Cálculo y generación de la tabla
    for i in range(1, numero_limite + 1):
        try:
            resultado = funciones[operacion](i)
            print(f"{i:<10} | {resultado:.4f}")
        except ValueError:
            # Manejo de casos como logaritmo de números que podrían dar error
            print(f"{i:<10} | Error de dominio")

# Ejecutar la calculadora
calculadora_cientifica()