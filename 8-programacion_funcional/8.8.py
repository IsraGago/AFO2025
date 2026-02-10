"""
Una inmobiliaria de una ciudad maneja una lista de inmuebles 
como la siguiente: 

Construir una función que permita hacer 
búsqueda de inmuebles en función de un presupuesto 
dado. La función recibirá como entrada la lista de 
inmuebles y un precio, y devolverá otra lista con los 
inmuebles cuyo precio sea menor o igual que el dado. 
Los inmuebles de la lista que se devuelva deben incorporar un 
nuevo par a cada diccionario con el precio del inmueble, 
donde el precio de un inmueble se calcula con las siguiente
fórmula en función de la zona:
    • Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
    • Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
"""

def buscar_inmuebles(lista_inmuebles, presupuesto):
    resultado = []
    
    for inmueble in lista_inmuebles:
        # 1. Extraer datos para el cálculo
        m = inmueble['metros']
        h = inmueble['habitaciones']
        g = 1 if inmueble['garaje'] else 0  # Convertimos True/False a 1/0
        antiguedad = 2024 - inmueble['año'] # Calculamos los años de antigüedad
        
        # 2. Calcular precio base
        precio = (m * 1000 + h * 5000 + g * 15000) * (1 - antiguedad / 100)
        
        # 3. Aplicar multiplicador según zona
        if inmueble['zona'] == 'B':
            precio *= 1.5
            
        # 4. Filtrar por presupuesto
        if precio <= presupuesto:
            # Creamos una copia para no modificar la lista original
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            resultado.append(inmueble_con_precio)
            
    return resultado

# --- Ejemplo de prueba ---
inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}
]

mi_presupuesto = 150000
busqueda = buscar_inmuebles(inmuebles, mi_presupuesto)

print(f"Inmuebles encontrados para un presupuesto de {mi_presupuesto}€:")
for i in busqueda:
    print(i)