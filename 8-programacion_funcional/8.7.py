"""
Escribir una función reciba un diccionario con las asignaturas y 
las notas de un alumno y devuelva otro diccionario con las 
asignaturas en mayúsculas y las calificaciones correspondientes
a las notas aprobadas. 
"""

def obtener_calificacion(nota):
    """Convierte notas numéricas en texto (solo para aprobados)."""
    if 5 <= nota < 7:
        return "Aprobado"
    elif 7 <= nota < 9:
        return "Notable"
    elif 9 <= nota < 10:
        return "Sobresaliente"
    elif nota == 10:
        return "Matrícula de Honor"
    return None # Para notas menores a 5

def filtrar_y_procesar_aprobados(notas_alumno):
    """
    Devuelve un diccionario con asignaturas en MAYÚSCULAS 
    y su calificación, solo si la nota es >= 5.
    """
    return {
        asignatura.upper(): obtener_calificacion(nota)
        for asignatura, nota in notas_alumno.items()
        if nota >= 5
    }

# --- Ejemplo de uso ---
cesta_notas = {
    "Física": 4.5,        # Suspenso (será filtrado)
    "Matemáticas": 9.2,   # Sobresaliente
    "Historia": 6.8,      # Aprobado
    "Química": 3.0,       # Suspenso (será filtrado)
    "Programación": 10    # Matrícula
}

solo_aprobados = filtrar_y_procesar_aprobados(cesta_notas)

print("--- Acta de Aprobados ---")
for asignatura, calif in solo_aprobados.items():
    print(f"{asignatura}: {calif}")