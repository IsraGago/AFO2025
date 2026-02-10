
"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. 
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, 
y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta. 
"""

def aplicar_descuento(precio, porcentaje):
    """Calcula el precio tras aplicar un descuento."""
    return precio * (1 - porcentaje / 100)

def aplicar_iva(precio, porcentaje):
    """Calcula el precio tras añadir el IVA."""
    return precio * (1 + porcentaje / 100)

def calcular_total_cesta(cesta, funcion_calculo):
    """
    Recibe un diccionario {precio: porcentaje} y una función para 
    aplicar a cada par. Devuelve la suma total.
    """
    total = 0
    for precio, porcentaje in cesta.items():
        total += funcion_calculo(precio, porcentaje)
    return total

# --- Ejemplo de uso ---

compra = {100: 10, 250: 20, 1500: 5}

# Calculando con descuentos
total_con_descuento = calcular_total_cesta(compra, aplicar_descuento)

# Calculando con IVA
total_con_iva = calcular_total_cesta(compra, aplicar_iva)

print(f"Total con descuentos: {total_con_descuento}€")
print(f"Total con IVA: {total_con_iva}€")